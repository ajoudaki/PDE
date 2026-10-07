# Control variates for passive moments: a neural symmetry obstruction and its exact averaging repair

2026-10-06. Bounded author continuation in the existing unseen-query study.
No experiments, Git operation, independent review, or promotion.

A control built from linear combinations of training pair tests need not have
vanishing residual variance, even if it is granted the entire exact nonlinear
training history. The example below is an actual depth-two network with two
nonlinear activations, one of them unbounded, positive training-feature gap,
spanning data, zero readout, and motion in both hidden blocks. An unseen
first-layer cross moment has a fixed positive variance distance from the
specified controls. The obstruction persists under every sufficiently
low-relative-entropy posterior row law. Thus it directly concerns the
posterior variance needed by the existing prior-block method, rather than
only variance under the unconditioned Gaussian law.

The obstruction is specific to a control family, not to neural decoding.
Indeed, the initial moment has a closed Gaussian formula. More generally,
the same network symmetry gives an exact, inexpensive conditional Gaussian
averaging rule that retains nonlinear trained fields. That rule removes
integer-period ambiguity but leaves a nonlinear integral over the remaining
row variables. No theorem makes the latter integral uniformly cheap through
the full training source, and no full polylogarithmic-query decoder is proved.

## 1. The unchanged target and the moment being evaluated

The target retains the original width-n network, fixed arbitrary hidden depth
L>=2, independent Gaussian first weights and hidden matrices, exactly zero
initial stored readout, mean squared loss, and mobilities
(n,1,...,1,n). Inputs v=x/sqrt(d) have unit norm; the m>=d training inputs
span the input space. The full original small-label allowance, positive
initial feature-Gram gap, and strip-analytic activations are unchanged.
Activation values may be unbounded. A completed decoder must use its current
retained state without training replay and have one accuracy event for all
sphere inputs, all physical times, and the fitted endpoint, at the inherited
independent-dense upper-certificate scale.

The stable passive moment in RECALIBRATION_FREE_MOMENTS.md is

\[
 b_\ell=\mathbb E_{\nu_c}\left[
 V_\ell\Psi_{\phi_\ell}(U_\ell^TA_\ell b_{\ell-1},\beta_\ell)
 \right],\qquad
 \Psi_\phi(z,\beta)=\mathbb E_g\phi(z+\sqrt\beta g),
 \tag{1}
\]

together with its scalar second moment. The proof-only posterior marginal
nu_c has D(nu_c||mu)<=h, where mu is the Gaussian row-packet prior and
h=polylog(n)/n on the inherited event. The actual algorithm never evaluates
nu_c. In the first layer, the analogous moment pairs a retained first-layer
training mark with the new query activation; that is where the example below
occurs.

For a vector row test X and a computable control C_0, the prior-block
control lemma in FAST_UNIFORM_QUERY.md has error

\[
 e_{\rm ctrl}+4V/\sqrt s,\qquad
 V^2=\sum_i\mathbb E_{\nu_c}(X_i-C_{0,i})^2,
 \tag{2}
\]

using s rows in each block and independently amplified block medians.
Here e_ctrl bounds the error in the supplied control expectation. A
polylogarithmic s at root-width local accuracy requires V^2 of order
polylog(n)/n. Replacing second moments in (2) by the smaller residual
variances would not repair the counterexample below: even that smaller
quantity has a positive lower bound.

## 2. An actual neural symmetry survives the complete training flow

Take L=2 and m=d=2, with training inputs v_1=e_1, v_2=e_2. Fix 0<alpha<1
and use

\[
 \phi_1(z)=\sin z,\qquad \phi_2(z)=z+\alpha\sin z.
 \tag{3}
\]

Both are nonlinear and analytic. Their derivatives are bounded on every
fixed horizontal strip; the second activation has unbounded values. Write
the first matrix as A, the hidden mixer as W, and the stored readout as w,
so

\[
 h_a^{(1)}=\sin(Av_a),\qquad
 z_a^{(2)}=Wh_a^{(1)},\qquad
 h_a^{(2)}=\phi_2(z_a^{(2)}),\qquad
 f_{n,a}=w^Th_a^{(2)}/n.
\]

The residual is r_a=f_{n,a}-y_a and the loss is m^{-1}sum_a r_a^2.
With the original mobilities, the physical equations are

\[
 \dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^T,
 \quad
 \dot W=-\frac2{mn}\sum_a r_a\delta_a^{(2)}h_a^{(1)T},
 \quad
 \dot w=-\frac2m\sum_a r_a h_a^{(2)},
 \tag{4}
\]

where delta_a^(2)=w odot phi_2'(z_a^(2)) and
delta_a^(1)=cos(Av_a) odot W^T delta_a^(2).

Fix a neuron i and an integer k. Add 2pi k to A_{i1}, leaving all other
parameters unchanged. Every training first activation and its derivative
are unchanged, hence so are all later training fields, predictions,
residuals, and the three velocities in (4). The vector field is therefore
equivariant under this translation. Uniqueness of the smooth ODE gives,
throughout the common interval of existence,

\[
 A(t;A_0+2\pi k e_i e_1^T)=A(t;A_0)+2\pi k e_i e_1^T,
 \tag{5}
\]

while W(t), w(t), all training activations, backward fields, weight
velocities, and trained increments remain unchanged. This also identifies
the maximal existence intervals of the translated solutions. On the
inherited all-time existence event it holds at every physical time.
Integration, differentiation in time, and fixed linear combinations of
these unchanged fields preserve the symmetry. Raw first coordinates and
raw first preactivations are affine, rather than periodic, under the shift.

This example has the required gap. Put
q=E sin^2(G)=(1-e^{-2})/2 for a standard Gaussian G. The two initial
first-layer features have population Gram q I_2. The two limiting top
preactivations are independent N(0,q). Since phi_2 is odd, their top
feature Gram is

\[
 \gamma I_2,\qquad
 \gamma=\mathbb E\phi_2(\sqrt qG)^2>0.
 \tag{6}
\]

Positivity follows because phi_2'(z)>=1-alpha>0 on the real axis and
phi_2(0)=0. Choose labels y=(eta,0) with a fixed eta>0 inside the original
allowance for this fixed problem; no width-dependent label reduction is
used.

Both hidden blocks really move. At initialization, w=0 gives
dot A=dot W=0, but differentiation of (4) gives

\[
 \ddot W(0)=\frac{4\eta^2}{m^2n}
 [h_1^{(2)}\odot\phi_2'(z_1^{(2)})]h_1^{(1)T},
 \tag{7}
\]
\[
 \ddot A(0)=\frac{4\eta^2}{m^2}
 \{\cos(Av_1)\odot W^T[h_1^{(2)}\odot\phi_2'(z_1^{(2)})]\}v_1^T.
 \tag{8}
\]

Almost surely W is invertible, every cos(A_{i1}) is nonzero, and
h_1^(1) is nonzero. The Gaussian density and the nonzero determinant
polynomial prove the first assertion; the others exclude countable
zero sets of one-dimensional continuous Gaussian variables. Hence
z_1^(2) is a nonzero vector. Strict monotonicity of phi_2 and positivity
of phi_2' make h_1^(2) odot phi_2'(z_1^(2)) nonzero. Equations (7)--(8)
are consequently nonzero almost surely. The symmetry argument has not
frozen either hidden layer.

## 3. Which controls inherit the symmetry

Let G_1,G_2 be the two initial first-row Gaussian entries. Let Z collect
all other Gaussian packet coordinates, or the remaining initialization
entries in a finite-width proof. Under the prior mu these are independent
of (G_1,G_2). A shift-invariant training mark is a measurable function
F with

\[
 F(g_1+2\pi,g_2,z)=F(g_1,g_2,z).
\]

The exact physical training fields identified in (5) have this property.
A raw first-layer coordinate is g_1 plus a periodic trained increment,
or is unchanged. Thus every linear combination of products of two such
physical marks, allowing constants, single marks, and raw first
coordinates, belongs to

\[
 C(g_1,g_2,z)=\sum_{j=0}^{2}g_1^jF_j(g_1,g_2,z),
 \qquad F_j(g_1+2\pi,g_2,z)=F_j(g_1,g_2,z).
 \tag{9}
\]

The coefficients of a query control are fixed when its row function is
evaluated. They may depend on the current retained scalar prefix and on
the query; (9) permits arbitrary such fixed coefficients. Allowing all
measurable F_j enlarges the physical pair-control class enormously, and
therefore strengthens a lower bound for it. In particular, neither an
increasing number of training times nor arbitrarily many unchanged
nonlinear training marks escapes (9).

There is an essential interface boundary. Formula (9) characterizes
linear pair controls built from these physical marks, and finite row
schemes that preserve their translation symmetry. Arbitrary nonlinear
processing of raw preactivations, artificial raw-coordinate caps, or
extra deliberately nonperiodic control tests can leave the class. An
implementation using those operations needs its own argument. The
claim below does not identify every globally capped compiler node with
an exact physical mark and does not rule out all controls that a more
elaborate current-state decoder might construct.

## 4. A positive variance floor under low-entropy posterior laws

Take the unseen input v=(e_1+e_2)/sqrt(2). Its initial first-layer
cross-moment row integrand against the retained first training activation
is

\[
 X=f(G_1,G_2),\qquad
 f(g_1,g_2)=\sin(g_1)\sin((g_1+g_2)/\sqrt2).
 \tag{10}
\]

This is an actual first-layer pairing required when the passive query
is passed into the second initialized mixer. It is not a freely chosen
generic row test. A constant normalization of the retained training mark
only multiplies the lower bound below by its squared normalization.

**Proposition.** There are constants a_0,d_0>0, independent of width,
the number of control marks, and the dimension of Z, such that every law
nu satisfying D(nu||mu)<=h obeys

\[
 \inf_{C\ \mathrm{of}\ (9)}\operatorname{Var}_\nu(X-C)
 \ge\frac{d_0^2}{64}\left(a_0-\sqrt{h/2}\right)_+.
 \tag{11}
\]

Consequently, for h<=a_0^2/2 the right side is at least
d_0^2 a_0/128>0. The infimum may be taken over only controls for which
the variance exists; infinite second moments cannot improve it.

Here is a complete choice of the constants. Set

\[
 A_*=(e^{i\sqrt2\pi}-1)^3,\quad \psi=\arg A_*,\quad
 g_2^*=\sqrt2(\pi/2-\psi)-\pi/2,
\]
\[
 B_*=[\pi/2-1/4,\pi/2+1/4]\times[g_2^*-1/4,g_2^*+1/4].
\]

Let p(g)=(2pi)^{-1}exp(-|g|^2/2) be the two-dimensional Gaussian
density, and put

\[
 d_0=|A_*|/2=4\sin^3(\pi/\sqrt2),\qquad
 a_0=\frac14\int_{B_*}\min_{0\le k\le3}p(g+2\pi k e_1)\,dg.
 \tag{12}
\]

Both are strictly positive fixed numbers.

**Proof.** On each shift orbit, C in (9) is a polynomial of degree at
most two in the integer shift. Its third finite difference therefore
vanishes. Directly expanding the sine into complex exponentials gives

\[
 \sum_{k=0}^3(-1)^{3-k}{3\choose k}f(g+2\pi k e_1)
 =\sin(g_1)\operatorname{Im}
       [e^{i(g_1+g_2)/\sqrt2}A_*].
 \tag{13}
\]

On B_* its magnitude is at least
|A_*|cos(1/4)cos(1/(2sqrt(2)))>=d_0, by the choices in (12).
Fix any real b and set r=f-C-b. The absolute values of the four
finite-difference coefficients sum to eight. Hence, for every g in
B_* and every external z, at least one of the four translates has
|r(g+2pi k e_1,z)|>=d_0/8.

Let E={|r|>=d_0/8}. Integrate this covering property against the
minimum translated density in (12), then against the independent law
of Z. Each of the four translated integrals is at most mu(E), so

\[
                         \mu(E)\ge a_0.                 \tag{14}
\]

No bound on the control values or their coefficients was used.
Relative entropy implies |nu(E)-mu(E)|<=sqrt(h/2). For completeness,
apply the log-sum inequality to E and its complement. The resulting
binary relative entropy, as a function of its first probability p, has
second derivative 1/[p(1-p)]>=4 and value and first derivative zero
when p is the second probability. It is therefore at least twice the
squared probability difference. This proves the asserted event bound,
including endpoint cases by continuity.

Taking b=E_nu(X-C), equation (14) now gives (11) by integrating r^2
on E. If the variance is infinite, the lower bound already holds.
This proves the proposition.

The same proof with the (p+1)-st finite difference gives a strictly
positive floor for every separately fixed degree p in the raw first
coordinate with arbitrary periodic coefficients. No constant uniform
in p is asserted. Growing-degree or nonpolynomial query-aware controls
are not excluded.

At the inherited h=polylog(n)/n, (11) eventually has a fixed positive
lower bound. It contradicts the proposed deduction that retained
training pair expectations alone ensure the near-1/n residual variance
needed by (2). A positive variance does not itself prove a sampling
lower bound for every possible estimator: it shows that this
variance-based control certificate cannot remove the large block size.
It also does not prove an output-error lower bound. In particular the
readout is zero at the initial prefix, so the prediction there is
already known. A uniform theorem for all intermediate passive moments
cannot use this pair-control argument, but a decoder exploiting a
different observable organization remains possible.

## 5. Exact Gaussian averaging repairs the specific missing information

The very moment in (10) has the explicit prior expectation

\[
 \mathbb E_\mu X=e^{-1}\sinh(1/\sqrt2),                  \tag{15}
\]

by the sine product identity and the Gaussian characteristic function.
Since |X|<=1, the event bound proved above, applied to bounded functions
by integration of their level sets, gives

\[
 |\mathbb E_\nu X-\mathbb E_\mu X|\le\sqrt{2h}.         \tag{16}
\]

Thus this initial posterior moment has a deterministic, constant-size
evaluator within the desired logarithmic root-width scale. The variance
obstruction concerns the chosen controls, not the complexity of this
mean. An algorithm could use C=X and the computable approximate
posterior expectation (15); that control is outside (9).

The symmetry also gives a finite Gaussian averaging rule for nonlinear
trained first-layer fields. Write each initial first-row coordinate as

\[
 G_a=S_a+2\pi K_a,\qquad S_a\in[-\pi,\pi),\quad K_a\in\mathbb Z.
\]

Under the independent Gaussian prior, conditional on S_a=s the integer
K_a has probabilities proportional to exp(-(s+2pi k)^2/2). For real u
define the explicit conditional characteristic function

\[
 M_u(s)=
 \frac{\sum_{k\in\mathbb Z}e^{-(s+2\pi k)^2/2}
                              e^{iu(s+2\pi k)}}
      {\sum_{k\in\mathbb Z}e^{-(s+2\pi k)^2/2}}.
 \tag{17}
\]

It is bounded in magnitude by one. Conditional on all S_a and any
independent remaining root Z, the integer coordinates are independent.
For the orthogonal training inputs and sine first activation, write a
trained first row as A(t)=G+D(t,S,Z). Equation (5) states precisely
that its increment D is independent of the integer representatives.
Therefore, for every sphere query v, every time at which this row is
defined, and every integrable shift-invariant training mark V(S,Z),

\[
 \mathbb E_\mu\left[
 V\sin(A(t)^Tv)\mid S,Z\right]
 =V\operatorname{Im}\left[
       e^{iD(t,S,Z)^Tv}\prod_{a=1}^d M_{v_a}(S_a)\right].
 \tag{18}
\]

This is exact conditional integration, with the complete trained
increment retained. It makes no expansion in the label or in D, and
does not drop a hidden-layer update or transpose response. It is not
yet the final expectation over (S,Z). If the solution is specified only
on its existence domain at that time, that domain is shift invariant
by (5); assign D=0 and V=0 off it before taking the expectation. This
is a proof extension, not an assertion that failure states approximate
the desired network. For a current-state row circuit
that supplies D and V with this symmetry, (18) can be evaluated from
that circuit; the formula does not request the historical flow again.
For the dense finite-network proof D depends on the remaining dense
roots; (18) by itself does not compress those roots.

The sums in (17) are a cheap numerical primitive. On |s|<=pi, their
denominator is at least e^{-pi^2/2}. Omitting |k|>K gives total
absolute tail at most

\[
 2\sum_{k>K}e^{-(2\pi k-\pi)^2/2}
 \le C e^{-c(K+1)^2},\qquad K\ge1,                     \tag{19}
\]

with numerical positive constants c,C. For example, divide each
successive term by its predecessor; the ratio is at most e^{-4pi^2}
for the indicated tail, which bounds it by a geometric series.
The numerator has the same tail bound for real u. The truncated
denominator has the same positive floor, and the numerator magnitude
is at most its corresponding denominator. The quotient error is thus
at most C exp(-c(K+1)^2), uniformly over real u and |s|<=pi.
Taking K=C sqrt(log(Cd/epsilon)) and telescoping the product of factors
of magnitude at most one evaluates (18), apart from V and D, with

\[
 O\bigl(d\sqrt{\log(Cd/\epsilon)}\bigr)
 \tag{20}
\]

scalar exponential/trigonometric calls and O(d) live scalars. If |V| is
bounded by a supplied M, replace epsilon by epsilon/(1+M). The
denominator floor makes the elementary summation and quotient stable
with O(log(d/epsilon)+log(1+M)) guard precision, in addition to the
precision needed to evaluate D and V. Actual exponential, activation,
and data-primitive costs are charged at that precision. No exact
integration oracle is hidden in (20).

This quotient integration does not on its own produce small remaining
variance. At initialization in (10), the conditionally averaged
integrand is

\[
 \sin(S_1)\operatorname{Im}
          [M_{1/\sqrt2}(S_1)M_{1/\sqrt2}(S_2)].           \tag{21}
\]

It is continuous, equals zero at S_1=0, and has the strictly positive
mean in (15). The wrapped Gaussian density is positive everywhere on
the torus. If (21) had zero variance, continuity and that density would
make it constant everywhere; its zero at S_1=0 would contradict (15).
Its variance is therefore a positive fixed number. One can integrate
this particular two-variable function deterministically, or use (15),
but later trained fields still depend on the growing packet Z.

The conditional law used in (18) is the prior law. A posterior based
only on shift-invariant tests preserves the same conditional integer
law, since its likelihood is constant along each orbit. Retained raw
preactivation moments need not have that property. For the actual
posterior, (18) is therefore not silently promoted to an exact identity.
For bounded controls its expectation error can instead be budgeted by
the entropy estimate below. Unbounded normalized history marks require
additional control.

## 6. A usable expectation interface, and the remaining missing theorem

There is a simple sufficient interface for query-aware deterministic
controls that does not require their posterior moments to have been
acquired. Suppose C_0 is a vector control with the pointwise bound
||C_0(z)||_2<=M, a computed vector hat m_mu approximates its prior
expectation within e_quad, and D(nu||mu)<=h. The total-variation event argument and
duality with unit vectors give

\[
 \|\widehat m_\mu-\mathbb E_\nu C_0\|_2
                  \le e_{\rm quad}+M\sqrt{2h}.           \tag{22}
\]

Thus a bounded control with a cheap prior integral is allowed a
posterior-mean bias of the dense root-width scale. If in addition

\[
 \mathbb E_\nu\|X-C_0\|_2^2
                    \le\operatorname{polylog}(n)/n,     \tag{23}
\]

the existing block argument uses only polylogarithmically many rows,
with (22) included in its error propagation. Formula (15) is an actual
neural example with zero residual and bounded C_0. Formula (18) gives a
new explicitly computable part of an analogous construction without
assuming small trained displacement.

Neither (22) nor (18) proves (23) for the full trained source. The
normalized marks V_ell in (1) have a posterior second-moment Gram bound,
not a polylogarithmic pointwise bound. Clipping them does not give a
vanishing clipping bias from that second moment alone. Polynomial
Gaussian controls also need their posterior expectation checked:
having a known Gaussian prior moment is insufficient for an unbounded
control under a mere relative-entropy bound. The finite-dimensional
history Gram does not evaluate the new nonlinear moment or establish
its variance residual.

The most precise surviving branch is a current-state representation of
the remaining integral in (18), or of the corresponding general-data
moment in (1), that supplies both a counted prior expectation and a
posterior-valid remainder of size (23). Arbitrary correlated spanning
data need not possess the product integer-period structure used in
(17)--(18). Even with a square invertible training input matrix, the
induced lattice Gaussian generally has correlated coordinates, so the
product in (18) requires replacement. The present lemma cannot supply
that replacement by changing coordinates and discarding the resulting
correlations.

| Claim | Status and precise limitation |
|---|---|
| Full nonlinear training translation symmetry (5) | Exact for the displayed admissible network; both hidden blocks move |
| Posterior residual-variance floor (11) | Proved for controls (9), arbitrary independent external prior roots, and every low-KL posterior law |
| Near-1/n residual from training pairs alone | Refuted for this control family, even granting arbitrarily many invariant history marks |
| Initial posterior passive moment | Deterministically evaluated within sqrt(2h) by (15)--(16) |
| Conditional averaging of the complete trained first-layer increment | Exact prior identity (18), with the numerical work in (20) |
| Vanishing variance after that conditional averaging | Not automatic; (21) has positive variance already initially |
| Full original all-sphere/all-time efficient decoder | Open; no universal neural impossibility claimed |

## 7. Provenance and author checks

Read completely for this continuation: FAST_QUERY_STRUCTURE.md,
FAST_UNIFORM_QUERY.md, RECALIBRATION_FREE_MOMENTS.md,
DENSE_BUDGET_GEOMETRY.md, SANE_RESPONSE_MEMORY.md, and
SANE_PANEL_EXTENSION.md. The last two had already been read completely
in the same assigned author context; their full line counts were
rechecked. The maintained notation contract was read. The earlier
interrupted author assignment in this same context also read
EFFICIENT_QUERY_DIRECT.md, POPULATION_DECODER.md,
GROWING_PROGRAM_STABILITY.md, and LABEL_SERIES_DECODER.md; no new claim
here imports an unlisted dependency through those notes. No other
study, prior review report, archive, experiment, or external scientific
source was consulted.

The required solve-math-rigorously and investigate-conjectures skills,
with research-contract, evidence-ledger, and adversarial-audit references,
were applied. The canonical-notation skill was initially inaccessible
in the interrupted assignment but became readable in this continuation;
it and its neural-response-memory reference were then read completely.
Part 1 of the shared workflow was read. The supervisor's explicit
no-Git instruction governs this scoped attempt; no index or HEAD
operation was performed. Only this assigned file was written.

A prompt-only subagent derived the finite-difference control lemma and
its low-KL event transfer. Its allowed scientific setup was exactly
(9)--(10), plus required skills and notation. The lead route author
checked the argument and supplied the full neural symmetry,
admissibility and motion calculations, Gaussian quotient averaging,
and interface limitations. This was a collaborating author derivation,
not an isolated independent review. The coefficient factors in
(4), (7), (8), the four finite-difference weights, the posterior event
transfer for unbounded controls, and the denominator/tail bounds in
(17)--(20) were checked algebraically. No numerical check was needed
or run.

Input hashes at the read/write checkpoint:

```text
286cf8b8eaf433bcb2c64d3fea3631b67efb6b547776190b3d8d9a453820a2c1  FAST_QUERY_STRUCTURE.md
e59f805980ddc664794eee8c0f310f51667e94592d4ee502978663e77c64bcd9  FAST_UNIFORM_QUERY.md
710989a20ec43db01612c5957bcc1ca181249cdbd08db3fea6addc3ec1a081ea  RECALIBRATION_FREE_MOMENTS.md
50950e2df4d5d9e9eb20201769da7afee39ef2dee389f1ab97744a25ef88df0e  DENSE_BUDGET_GEOMETRY.md
de3407f4b7dac4e594b58ff261a65fd84cafa9a4c78437ce2240a9e653df7322  SANE_RESPONSE_MEMORY.md
8d570909d6431a2cca7f3c8456eb03344de62c7d12e4eb6bc880300d43d317b6  SANE_PANEL_EXTENSION.md
```

The retained claim is a specific, posterior-robust neural control
obstruction plus an exact partial integration mechanism. It does not
settle the full last-mile query problem or certify fourth/fifth-power
storage and peak workspace for that problem.
