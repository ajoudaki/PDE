# Constructive audit: remote spike corridors for linearly bounded activations

## 1. Question and verdict

For the established `q=1`, two-hidden-layer ascent network, write

\[
 \Delta_t(h)=F_{2t}(h)-F_t(2h),\qquad
 \mathcal C_\phi(t,\rho)=
 \sup_{0<|h|\le \rho/t}
 \frac{|\Delta_t(h)-\kappa_t h^3|}{|h|^5}.
\]

The literal coefficient \([h^5]\Delta_t\) is not a possible source of a
counterexample: whenever the width-first fifth jet exists, it is a polynomial
of degree at most four in `t`.  Thus the only meaningful negative target is

\[
 \limsup_{t\to\infty}\frac{\mathcal C_\phi(t,\rho)}{t^5}=\infty.       \tag{1.1}
\]

This note audits the most promising constructive route: a fixed smooth
activation which is flat on the Gaussian bulk and contains remote,
high-frequency Markov corridors.  It establishes three facts.

1. A single spike cannot establish (1.1) if its relevant Gaussian derivative
   moment is finite.  The analogous claim for two spikes is false: a first
   spike can transport Gaussian mass to a remote second spike whose height is
   not charged at its initialization Gaussian probability.
2. There are two coherent scalar mechanisms which evade the one-spike
   obstruction while preserving linear growth and all initialization Gaussian
   derivative moments: a two-scale transported-tail ladder and a many-branch
   Markov corridor.
3. The scalar mechanism is **not yet a theorem for the full `L=2` OMFP**.  The
   unproved bridge is an all-time lower comparison for the reused term
   \(n^{-1/2}W H^+\).  Linear growth and initialization derivative moments do
   not supply this comparison.  Consequently this route does not presently
   constitute a valid full-network counterexample.

The last boundary is substantive; dropping the reused term silently replaces
the requested network by a one-hidden-layer scalar surrogate.

## 2. The exact finite-width identity that every construction must survive

At one step put

\[
 H_j=\phi(u_j),\quad z_i=n^{-1/2}\sum_jW_{ij}H_j,\quad
 c_i=a_i\phi'(z_i),\quad
 b_j=n^{-1/2}\sum_iW_{ij}c_i,
\]

and make the simultaneous update

\[
 a_i^+=a_i+h\phi(z_i),\qquad
 W_{ij}^+=W_{ij}+\frac h{\sqrt n}c_iH_j,\qquad
 u_j^+=u_j+h\phi'(u_j)b_j.
\]

Writing \(H_j^+=\phi(u_j^+)\), direct substitution, with no limit and no
Taylor expansion, gives

\[
 \boxed{
 z_i^+=G_i^+ + h a_i\phi'(z_i)Q_n,
 \qquad
 G_i^+=\frac1{\sqrt n}\sum_jW_{ij}H_j^+,
 \qquad
 Q_n=\frac1n\sum_jH_jH_j^+.}                    \tag{2.1}
\]

If \(\phi\ge m>0\), then \(Q_n\ge m^2\) deterministically.  This makes
nonnegative flat-background activations attractive: the direct spike term in
(2.1) has a definite sign.  It does **not**, however, control \(G_i^+\).
Because \(H^+\) depends on the reused column action through `b`, a proof must
bound the conditional lower tail of \(G_i^+\) along every selected corridor
history.  At later steps the inverse-free OMFP recursion has further response
descendants of precisely this term.

Equation (2.1) is the exact point at which a scalar construction either becomes
a full-network construction or fails.

## 3. What an isolated spike can and cannot do

Consider first the frozen-feature tagged-row map

\[
 a^+=a+h\phi(z),\qquad z^+=z+h a\phi'(z).        \tag{3.1}
\]

If \(|\phi(x)|\le K(1+|x|)\), then

\[
 |a^+\phi(z^+)|
 \le K\bigl(|a|+|h|K(1+|z|)\bigr)
 \bigl(1+|z|+|h|\,|a|\,|\phi'(z)|\bigr).        \tag{3.2}
\]

Thus a one-use spike enters the terminal first moment only linearly.  For a
remote derivative plateau of height \(L_n\), width \(w_n\), and center
\(R_n\), its contribution is bounded by a polynomial in \(R_n,a,h\) times

\[
 w_ne^{-R_n^2/2}L_n.                             \tag{3.3}
\]

If the next iterate lands in an affine region and one more step is taken, the
largest new contribution is quadratic in the *same* \(L_n\), hence bounded by a
polynomial times

\[
 w_ne^{-R_n^2/2}L_n^2.                           \tag{3.4}
\]

This rules out one isolated spike, and a bounded collection of comparable
spikes whose heights are all charged at the same initialization tail scale.
It does **not** rule out a transported-tail ladder.  Suppose a first plateau at
`R` has slope `L_0` and sends a positive-mass set to `S`, while a second plateau
at `S` has slope `L_1`.  The second height is multiplied by the mass initially
present at `R`, not by the Gaussian mass at `S`.  Thus finiteness of
\(\mathbb E|\phi'(G)|^p\), which charges `L_1` by \(e^{-S^2/2}\), gives no
bound on the dynamically transported contribution

\[
 e^{-R^2/2}L_1.                                  \tag{3.5}
\]

This distinction invalidates any attempted proof which controls every
adaptive derivative query by an initialization Gaussian moment.

This is the elementary reason the tempting choice

\[
 \phi(x)=x+\epsilon\sin(x^3)
\]

does not by itself prove a counterexample.  Its derivatives are large in the
tails, but one still needs a positive-mass set of paths which sees a favorable
later phase.  That may be achieved either by repeated Markov branching or by a
two-scale transport construction.

### 3.1 The two-scale scalar parameter calculation

Take \(t_n=\lceil e^{R_n}\rceil\), \(h_n=t_n^{-1}\), and put

\[
 S_n=t_n,\qquad L_{0,n}=t_nS_n=t_n^2,
 \qquad L_{1,n}=e^{S_n}.                          \tag{3.6}
\]

For `a` in a fixed positive interval and `z` in a favorable first-shell
branch near `R_n`, (3.1) gives

\[
 z_1=R_n+h_naL_{0,n}\asymp S_n.                 \tag{3.7}
\]

Place a high-frequency sawtooth of favorable slope `L_{1,n}` throughout a
fixed-relative-width shell around `S_n`; the reset pieces keep the activation
value of order `S_n`.  A fixed conditional fraction of the transported
population then has

\[
 z_2=z_1+h_na_1L_{1,n}\asymp
 T_n:=\frac{e^{S_n}}{t_n}.                        \tag{3.8}
\]

Put a nonnegative flat output plateau of height comparable to `T_n` around
the landing range.  After one further update, `a` has increased by order
\(h_nT_n\); if the activation has a positive background, this creates a
persistent positive output of order \(h_nT_n\), even if the preactivation
subsequently leaves the plateau.

The initialization moment tests are nevertheless harmless.  At the first
shell, for every fixed `p`,

\[
 L_{0,n}^pe^{-R_n^2/2}
 =\exp\{2pR_n-R_n^2/2+o(R_n)\},                  \tag{3.9}
\]

and at the second shell

\[
 L_{1,n}^pe^{-S_n^2/2}
 =\exp\{pS_n-S_n^2/2\}.                          \tag{3.10}
\]

Both are summable after taking the shells sufficiently separated.  At the
second fine output, the transported favorable contribution has the scale

\[
 e^{-R_n^2/2}\frac{L_{1,n}}{t_n}
 =\exp\{S_n-R_n-R_n^2/2\},                       \tag{3.11}
\]

which diverges super-exponentially.  A step of size `2h_n` lands near
`2S_n`, so a narrow second shell can make the coarse path miss the second
amplifier.

At the much later terminal horizon one uses the next update to store the
large plateau value in the readout.  The persistent contribution is smaller
by one factor of `t_n`, namely

\[
 e^{-R_n^2/2}\frac{L_{1,n}}{t_n^2}
 =\exp\{S_n-2R_n-R_n^2/2\},                      \tag{3.12}
\]

and still diverges super-exponentially.

As with the Markov corridor below, (3.6)--(3.12) are exact scalar parameter
relations.  A sawtooth (many favorable microbranches plus narrow reset
branches) is necessary: using one narrow `L_1` plateau forces an initial
`a`-window of order `L_1^{-1}` and cancels the gain in (3.11).

## 4. A feasible all-order scalar corridor

The following parameter calculation explains why a many-branch corridor can
evade Section 3.  It is a construction principle, not a claim about (2.1).

Fix a mesh \(h=\rho/t\), a multiplier \(\lambda>1\), and set

\[
 r=\frac{h}{\lambda-1},\qquad
 s=\frac{(\lambda-1)^2}{h^2}.                    \tag{4.1}
\]

At a center \((a,z)=(rR,R)\), prescribe

\[
 \phi(R)=R,\qquad \phi'(R)=s.                    \tag{4.2}
\]

Then the scalar map (3.1) sends the center exactly to

\[
 (a^+,z^+)=(r\lambda R,\lambda R).               \tag{4.3}
\]

The coarse step of size \(2h\) instead sends its `z` coordinate to

\[
 z^{\rm coarse}=(2\lambda-1)R,                   \tag{4.4}
\]

which is separated by \((\lambda-1)R\) from the next fine center.  Narrow
corridors can therefore be made resonant for the fine mesh and flat at the
coarse landing point.

A single affine plateau is not enough.  Its local Jacobian is

\[
 \begin{pmatrix}1&hs\\hs&1\end{pmatrix},
 \qquad hs=\frac{(\lambda-1)^2}{h},               \tag{4.5}
\]

so an isolated branch loses too much initial volume.  The repair is to fill a
thin shell near `R` with a sawtooth residual.  The activation value remains
between fixed multiples of `R`, but it has slope `s` on many narrow rising
pieces and a compensating negative slope on still narrower reset pieces.
There are on the order of

\[
 s\asymp h^{-2}                                  \tag{4.6}
\]

rising branches in a shell of relative width independent of `h`.  Meanwhile
the absolute Jacobian determinant of one affine branch is

\[
 |1-h^2s^2|\asymp h^{-2}.                         \tag{4.7}
\]

Thus the number of branches exactly matches the two-dimensional volume
expansion.  This is the missing feature of a lone spike.  By putting the reset
piece in the least-mass part of each microcell, one can retain a fixed
conditional fraction \(\delta>0\) of a nonatomic scalar population at each
level.  On the surviving set, after `m` levels,

\[
 z_m\asymp \lambda^mR,qquad
 a_m\asymp h\lambda^mR,qquad
 \mathbb P(\text{survival})\gtrsim p_R\delta^m.   \tag{4.8}
\]

The positive output contribution is consequently of size

\[
 p_RhR^2(\delta\lambda^2)^m.                     \tag{4.9}
\]

Choosing \(\delta\lambda^2>1\) gives exponential growth.  Equation (4.4)
allows the coarse mesh to be sent into the flat complement.

This calculation is why a high-frequency *Markov corridor*, rather than an
isolated oscillatory bump, is the plausible negative mechanism.

## 5. One fixed smooth linearly bounded activation can contain all corridors

There is no activation-envelope obstruction to placing the preceding scalar
corridors at remote scales.  Choose recursively

\[
 R_n\uparrow\infty,\qquad t_n=\lceil e^{R_n}\rceil,
 \qquad h_n=\rho/t_n,                             \tag{5.1}
\]

and put the `n`th corridor in a compact interval beginning at `R_n` and ending
before `R_{n+1}`.  Use smooth sawtooth pieces with value bounded by a constant
multiple of `x`, slope of order \(t_n^2\), and transition derivatives of
order at most \(C_m t_n^{2m}\) at derivative order `m`.  The intervals can be
chosen locally finite and odd-reflected, or added to a positive constant
background.

For every fixed `m,p`, the initialization Gaussian moment contributed near the
left endpoint is bounded by

\[
 C_{m,p}\,t_n^{2mp}e^{-R_n^2/2}
 \le C_{m,p}\exp\{2mpR_n-R_n^2/2+o(R_n)\}.        \tag{5.2}
\]

After making `R_n` increase sufficiently fast, the series in (5.2) converges
for every pair `(m,p)`.  The activation is `C^infty`, has linear growth, and
has every initialization Gaussian derivative moment finite.  At the same
time

\[
 t_n\gg R_n^2,                                   \tag{5.3}
\]

so an exponential-in-\(t_n\) scalar corridor gain dominates the initial
Gaussian penalty \(e^{-R_n^2/2}\).

This verifies that “all Gaussian derivative moments finite” does not itself
rule out an all-order tail mechanism.

For the two-scale route, a more explicit smooth candidate is preferable to a
corner-smoothed sawtooth.  Let `chi` be a nonnegative Gevrey-2 cutoff, equal to
one on the middle half of `[-1,1]`, and choose disjoint positive shells
\(I_{R,n},I_{S,n},I_{T,n}\) of relative widths bounded below.  Up to harmless
positive interpolation ramps, put

\[
\begin{aligned}
 \phi(x)&=x+\epsilon R_n
   \sin(\omega_{0,n}x+\theta_{0,n}),
 &&x\in I_{R,n},\\
 \phi(x)&=x+\epsilon S_n
   \sin(\omega_{1,n}x+\theta_{1,n}),
 &&x\in I_{S,n},\\
 \phi(x)&=T_n,
 &&x\in I_{T,n},
\end{aligned}                                      \tag{5.4}
\]

with

\[
 \omega_{0,n}=\frac{L_{0,n}}{\epsilon R_n},
 \qquad
 \omega_{1,n}=\frac{L_{1,n}}{\epsilon S_n}.       \tag{5.5}
\]

Outside all shells take a fixed positive constant and join the pieces with
nonnegative Gevrey cutoffs.  For sufficiently small fixed `epsilon`, (5.4) is
positive and bounded by `C(1+x)` on the positive axis.  At derivative order
`m`, the oscillatory part on a shell of scale `X` and slope `L` is bounded by

\[
 C_m\frac{L^m}{X^{m-1}}.                           \tag{5.6}
\]

Equations (3.9)--(3.10), with `p` replaced by `mp`, prove every fixed Gaussian
derivative moment finite.  The terminal plateau can have width comparable to
`T_n`; its transition derivatives are bounded by constants times
\(T_n^{1-m}\), and its Gaussian moment contribution is negligible.

The Gevrey choice is not cosmetic.  If `q` is a Gevrey-2 density/cutoff on a
bounded rescaled shell, then its Fourier transform obeys

\[
 |\widehat q(\xi)|\le C_qe^{-c_q\sqrt{|\xi|}}.     \tag{5.7}
\]

Consequently signed response integrals containing one unsquared oscillatory
factor at frequency \(\omega_{1,n}\) are smaller than every power of
`L_{1,n}`.  Positive quantities such as
\(\mathbb E[a_1^2\phi'(z_1)^2]\) do not cancel; those give exactly the
backward RMS recorded in (6.0b).  A full proof must verify, node by node in the
two-step OMFP DAG, that every potentially adverse reused response has an
unsquared phase to which (5.7) applies.  This finite response-ledger check has
not been completed here.

## 6. Why this is not yet a full `L=2` proof

The two-scale ladder has a favorable power-counting which makes it more than a
pure scalar curiosity.  Put

\[
 p_n\asymp e^{-R_n^2/2},\qquad L_{0,n}=t_n^2.
\]

At initialization the backward RMS generated by the first shell has scale
\(L_{0,n}\sqrt{p_n}=t_n^2\sqrt{p_n}\).  A lower particle in that same shell
therefore moves, during the first update, by at most the characteristic scale

\[
 h_nL_{0,n}\bigl(L_{0,n}\sqrt{p_n}\bigr)
 =t_n^3\sqrt{p_n}=o(1).                          \tag{6.0a}
\]

After the top population has reached the second shell, its backward RMS has
scale \(L_{1,n}\sqrt{p_n}\).  The corresponding second displacement of the
first-shell lower particles has scale

\[
 h_nL_{0,n}L_{1,n}\sqrt{p_n}
 =t_nL_{1,n}\sqrt{p_n}.                          \tag{6.0b}
\]

Only a fraction `p_n` of the lower population moves on that scale.  Under
linear growth its contribution to the fresh forward RMS is therefore at most
of order

\[
 t_nL_{1,n}p_n.                                  \tag{6.0c}
\]

The direct selected-row jump has scale \(h_nL_{1,n}=L_{1,n}/t_n\), so the
ratio suggested by this ledger is

\[
 t_n^2p_n\longrightarrow0.                       \tag{6.0d}
\]

Thus the ordinary fresh-field variance need not kill the ladder.  What is not
controlled by (6.0a)--(6.0d) is the aggregate reused-adjoint response.  A
piecewise-linear sawtooth has roughly `L_1` corners, and smoothing all of them
can create large \(\phi''\)-response terms.  A sinusoidal shell

\[
 \phi(x)=v_n(x)+\epsilon S_n
 \sin(\omega_nx+\theta_n),\qquad
 \omega_n=\frac{L_{1,n}}{\epsilon S_n},          \tag{6.0e}
\]

has the same favorable-phase fraction and the same linear-growth envelope.
It also exposes the only plausible response estimate: integrate the
oscillatory \(\phi''\)-terms against the smoothed conditional Gaussian density
before taking absolute values.  An absolute derivative-envelope estimate
loses a factor of order \(\omega_n\) and cannot close.

To transfer (4.8)--(4.9) to the two-hidden-layer network one would need, for
the selected histories and every corridor level, quantitative constants
\(q_*>0\), \(K_*<\infty\) such that the width-first version of (2.1) obeys

\[
 Q_s\ge q_*,\qquad
 \mathbb P\left(
   |G_s^+|\le K_*(1+|z_s|+|a_s|)
   \mid\text{the selected source history}
 \right)\ge p_*>0,                               \tag{6.1}
\]

with `q_*`, `K_*`, and `p_*` uniform over the growing number of levels.  A
positive flat background gives the first inequality at finite width.  It does
not give the second.  The random vector \(H^{s+1}\) contains descendants of

\[
 b_j^s=n^{-1/2}\sum_iW_{ij}^sa_i^s\phi'(z_i^s),  \tag{6.2}
\]

and the selected population has exponentially growing \(a_s\).  Hence the
conditional variance and response shift of \(G_s^+\) can grow at the same or
a larger rate as the direct corridor term.  Initialization estimates such as
\(\mathbb E|\phi^{(m)}(G)|^p<\infty\) do not imply (6.1) at these adaptive
queries.

There are two further bridges:

1. the fixed-step width-first identification previously proved under bounded
   derivative envelopes does not automatically cover this globally unbounded
   derivative activation; it needs a truncation plus uniform-integrability
   proof at every fixed `(t,h)`;
2. even if the fine output has a positive corridor contribution, one must
   bound all negative contributions and prove that the coarse trajectory stays
   out of every later corridor.  Neither follows from the scalar center
   calculation.

Any argument omitting (6.1), the fixed-step truncation bridge, or the signed
coarse-output estimate is conditional.

## 7. Adversarial conclusion

The audit rejects the following purported counterexamples:

- a single smooth spike;
- \(x+\epsilon\sin(x^3)\) supported only by a large-derivative observation;
- a scalar corridor with the term \(G_s^+\) deleted;
- an argument that bounds only the favorable rows and ignores the signed
  remainder of the output.

It leaves two viable negative programs: a positive flat-background activation
with either a two-scale transported-tail ladder or remote full-branched
corridors, together with a new aggregate-adjoint lower-comparison theorem
proving (6.1).  The transported-tail ladder is the simpler candidate because
only its first three fine steps need amplification.  The comparison theorem is
presently absent.
Accordingly, no rigorous `C^infty`, linearly growing, all-Gaussian-moment
counterexample for the actual reused-matrix `L=2` OMFP has been obtained here.
Conversely, this failure is not evidence for the universal \(O(t^5)\) claim:
the scalar Markov calculation shows exactly why initialization moment bounds
alone are too weak to prove it.
