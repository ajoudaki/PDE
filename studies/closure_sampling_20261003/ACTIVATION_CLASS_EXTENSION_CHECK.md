# Internal reconstruction of the linear-growth analytic extension

2026-10-04. Scoped hostile check of
`ACTIVATION_CLASS_EXTENSION_ROUTE.md`, frozen SHA-256
`5c7877faece19eaac50c9fe9e7439027a02176d137ccc3c43a091f1410f4e5ba`.
This is an internal reconstruction, not an isolated promotion review.
The checker previously authored the separate tanh-constant refinement;
none of its new constants is an input to the present extension. No
experiment, Git operation or maintained-file edit was made.

**Nonlinear verdict: PASS relative to the stated inherited local Gaussian
insertion and finite initial-jet construction interfaces.** I reconstructed
the changes needed for unbounded activation values, rather than inferring
the complex theorem from the real theorem's prior PASS labels. In particular
the top carrier, the actual forward-control amplitude, the reverse feedback,
the complex Gaussian moments and the passive-query stop all close. No
additional unproved moment assumption or unclosed feedback inequality was
found. Sections 2--8 below give the reconstruction and its exact boundary.
The affine specialization is assessed separately in Section 9.

This verdict does not supply the existing explicit tanh label or error
constants for the enlarged class. The extension remains qualitative in its
fixed architecture/data constants and uses the conservative source radius
`c log(en)^(-(L+4))`.

## 1. Inputs, scope and normalized objects

The candidate was read completely. The complete scientific sources read
for this reconstruction were:

| Source | SHA-256 |
| --- | --- |
| Current-study `DEEP_COMPLEX_SOURCE.md` | `7a81a04bb3e52a1c60ee83f479238ea1dec54fe2b70277b4f7d513b5eb84c6f2` |
| Current-study `GENERAL_ANALYTIC_COMPRESSION.md` | `4fd314dd28367430cd60fa8b88fe0eb4d9b12f575c61aadd60ff61dff76dec53` |
| Current-study `GENERAL_WEIGHTED_COMPARISON.md` | `1dcb779135b616aa66be4cd830d2bd2f3217a56eeae8f3cdf7394a52262a4306` |
| Current-study `STORAGE_QUADRATIC_IMPROVEMENT.md` | `ec18f54a3e3977bf9c99ce5c26066f48688848f8b5a9c142b75424badeb025e2` |
| Authorized prior `UNBOUNDED_ACTIVATION_CANDIDATE.md` | `e939e971d7a9e1b884b42d73d3ce65f5b1f548d9e25ab9cfe76c0502aa591713` |
| Authorized prior `UNBOUNDED_INSERTION_CHECK.md` | `bec5707fccc99597570ce51c94d3a487fd0b1ede14578617275cb708fdd95578` |
| Authorized prior `UNBOUNDED_ACTIVATION_CHECK.md` | `12884770ecde1f8de5b503ab7d62dadc1fe4e1541f3cf1cf2c7c3b7e9c5954fd` |
| Authorized prior `DEPTH_CAVITY_ROUTE.md` | `e8f9f43c137a9c74b751cbd2e54cf5a2b13f090c560d912b4b17994c53bc1478` |

The four prior files are in
`studies/dense_cutoff_population_rate_20261001/`, explicitly authorized for
this check. No further prior references were followed. The current-study
`DATASET_LABEL_DEPENDENCE.md` and the complete label/source/runtime notes
already read during the immediately preceding scoped task also supplied
notation and deterministic normalization checks. Required notation,
neural-network, rigorous-proof and adversarial-audit instructions remained
current.

The candidate keeps the canonical finite dense model, independent Gaussian
initialization, zero readout and squared mean-loss flow with mobilities
`(n,1,...,1,n)`. Write `v=x/sqrt(d)`, `||v||=1`,
`rho=||y-f_n(v_a)||_2/sqrt(m)`, and `Y=||y||_2/sqrt(m)`.
The physical norm divides first-weight and readout squared Euclidean norms
by `n`, while hidden matrices use Frobenius norm. In mobility coordinates
`Theta=(A,sqrt(n)W^(2),...,sqrt(n)W^(L),w)`, this norm is the ordinary
Euclidean norm divided by `sqrt(n)`. The unnormalized prediction is
`F_a=n f_n(v_a)`.

The activation assumptions are exactly: real values on the real axis,
holomorphy on `|Im z|<a`, finite `b=max_l|phi_l(0)|`, and a bounded strip
derivative `|phi_l'|<=s`, with `s>=1`. The gap is the smallest eigenvalue
of the initialized limiting top-feature Gram, without an extra sample
normalization. It remains explicitly assumed positive.

The theorem concerns fixed `d,L,m`, fixed data and sufficiently small
fixed labels. It gives a high-probability statement at each sufficiently
large width, not an event simultaneous over all widths. Its all-time norm
is the supremum over the whole real query sphere at equal physical times.

## 2. Linear growth, initialization and the real physical tube

Integrating `phi'` along the straight segment from zero gives
`|phi(z)|<=b+s|z|`. This segment stays in the strip. On
`|Im z|<=a/2`, Cauchy's formula for `phi'` on a radius-`a/4` disk gives
the candidate's bounded derivatives of every needed finite order. For an
explicit pole-margin convention in the complex proof, one may take
`b_0=a/32`; full and cavity pole caps `b_0,2b_0`, and their joining
segments then remain strictly inside the derivative strip. This is a
choice of the candidate's unspecified inherited pole margin, not an added
activation assumption.

On an operator tube `||A||/sqrt(n),||W^l||<=K`, normalized feature norms
obey the finite recurrence
\[
 H_1=b+sK,\qquad H_l=b+sKH_{l-1}.
\]
For a complex query input of bounded norm, only the first value changes by
a fixed factor. Thus all feature norms are bounded independently of width,
even though individual coordinates are not. Backpropagation gives
`||delta_a^l||_(2,n)<=s(sK)^(L-l)||w||_(2,n)`.

At initialization, conditioning successively on preceding features makes
the rows centered Gaussian with the preceding empirical covariance.
Linear growth gives bounded conditional fourth moments on bounded
covariance sets. Conditional Chebyshev and continuity under
`Q^(1/2)G` prove the stated covariance convergence. The same argument for
`exp(eta max_a|z_a|)` uses a bounded conditional second moment on those
sets. It proves convergence in probability of the initial empirical
exponential budget; it does not assert an unconditional exponential moment
for a deep finite Gaussian network on rare unbounded-covariance events.

On a normalized readout Gram margin `g>0`, the exact energy identity is
\[
 -\partial_t\rho^2=\|\dot\theta\|_{\rm par}^2,
 \qquad-\dot\rho\ge2g\rho.
\]
Since `||dot theta||^2=2rho(-rho')`, its path length is at most
`Y/sqrt(g)`. Thus readout RMS is at most that number; hidden velocities
are at most `C rho ||w||_(2,n)` and hidden displacement is
`CY^2/g^(3/2)`. Forward Lipschitz propagation controls feature singular
values with the same displacement. Small fixed labels preserve both Gram
and operator margins, including the first-weight operator. This proves
real global fitting, finite path length, and uniform query output tails.

The authorized real unbounded proof supplies the all-time coordinate
maximum, including the top readout. Its use here is legitimate, but it
does not supply the complex source theorem. The remaining sections check
that theorem separately.

## 3. The changed local estimates really use only RMS or logarithmic caps

Let `S` be the candidate's fixed multiple of `Y/g`. Under the stopped
joint budget `H<=2B`, for fixed positive `eta,S,B`,
\[
 Z_i\le C\log(en),\qquad K_i\le CS\log(en),\qquad
 \|k_a^l\|_{p,n}\le CSp(2B)^{1/p}.
\]
The last bound includes `k^L=w`; the separate bounded-readout assumption
from the old proof is no longer used. The deterministic counting-two norm
is `CS` from the physical tube, so its coefficient is independent of `B`.

The explicit Hessian in the bounded cavity source has only:

* two readout/feature cross terms of rank at most `n`;
* mixed hidden-weight terms containing one `delta/sqrt(n)`;
* bounded-map contractions of `diag(phi'' k)`.

A hidden variation acts as `U_H h/sqrt(n)`, of norm at most
`H_{l-1}||U_H||_F`. Thus the first two classes have bounded operator and
normalized Schatten norms using feature and carrier RMS. The third class
is controlled by the joint carrier budget at **every** layer. Consequently
\[
 \|D^2F_a\|_{p,n}\le C[1+Sp(2B)^{1/p}],\qquad
 \|D^2F_a\|_{2,n}\le C,
\]
and its operator norm is `C(1+S log n)`. These statements remain true for
the augmented Hessian endpoint blocks. No coordinate bound on a retained
feature is inserted in place of its RMS.

For deleted neuron `i`, the actual controls have amplitudes
`C(1+Z_i)` and `CK_i`. Direct integration of its learned column and row
gives, respectively,
\[
 \|\Delta W_{:,i}^{j+1}\|_2\le CS^2(1+Z_i)/\sqrt n,
 \qquad
 \|\Delta W_{i,:}^{j}\|_2\le CSK_i/\sqrt n.
\]
After multiplication by their actual controls, the omitted source error
is bounded by
\[
 \frac C{\sqrt n}\sum_{i\in I}
       [S^2(1+Z_i)^2+SK_i^2].
\]
For every fixed deletion count this is `n^(-1/2) polylog(n)`. For a
passive query the extra deleted activation has a polynomial-logarithmic
cap; it changes the logarithmic power only. Adaptive dependence is allowed
for these small source terms because their bound is pathwise.

The nonlinear vector remainder can be checked at each type of node:

* Scalar Taylor terms use bounded second, third or fourth derivatives on
  the safe strip. Their Euclidean remainder is bounded by
  `C[n^(alpha-beta)+n^(-beta)u+u^2]`.
* A reference activation multiplying a changed matrix is controlled by
  its RMS. A product of changed matrix and changed activation keeps its
  `n^(-1/2)` factor.
* In the gradient block `delta h^T/sqrt(n)`, both linear terms use the
  respective RMS bounds, and the quadratic term keeps `n^(-1/2)`.
* Changed gates in reverse probes multiply the reference probe, whose
  Gaussian coordinate bound is small; they do not require delocalization
  of the changed probe.
* In augmented `R,Q,J` recursions, the additional diagonals are precisely
  the stopped forward/angular responses and carriers. Unbounded feature
  values still enter only normalized matrix maps or deleted controls.

With `alpha=.01`, `beta=.1`, and remainder cap `u<=n^(-.04)`, the
largest new residual-weighted term is `n^(2alpha-beta)=n^(-.08)`.
The matrix cross terms are at most `n^(-.48)` before mixed remainder
terms. The weak variational factor `n^(.001)`, integration over bounded
activity or `O(log n)` physical length, and all polynomial logarithms
leave a strict improvement on `n^(-.04)`. The coordinate discrepancy may
therefore retain the looser bound `C_r n^(-1/30)`.

For fixed controls, the enlarged first variations remain complex linear
maps of the independent real Gaussian roots. Splitting real and imaginary
parts preserves the Gaussian tail exponent `n^(.79)` and the analogous
quadratic/bilinear tail. Actual controls have amplitudes `polylog(n)` and
Lipschitz constant `sqrt(n) polylog(n)`. Their one-dimensional contour
net has log cardinality `n^(.625) polylog(n)`; extra time/query grids
are polynomial and add `O(log n)`. The tail still dominates. Thus this
extension does not replace control-uniform insertion by a Gaussian claim
conditional on the actual root-dependent controls.

At the top layer the offset multiplies both the retained gradient and
reverse force. Its magnitudes are respectively `n^(-1/2) polylog(n)`
and `n^(-1) polylog(n)`, so both fit the same remainder. Dropping the
second term would be a false exact identity; the checked candidate keeps
it in equation (17).

## 4. Complex physical tube and the two reciprocal traces

Complex residual decay is obtained by following the real solution to its
real anchor and only then a short vertical segment. On a stopped RMS tube,
the algebraic Gram has bounded operator norm. Its complex residual equation
therefore changes residual magnitude by at most `exp(C r_n)`, not by
`exp(C T)`. Short negative-real or terminal-real pieces are treated in the
same way. This supplies contour activity at most `S`, readout RMS `CS`,
and strict enlarged operator margins. Positivity is invoked on the real
portion only.

In a Dyson product, intervening negative-Gram propagators are contractions
on positive real portions. Their total short non-real/backwards length is
`O(r_n)`, so they cost one factor `exp(Cr_n)`. The residual Hessian's
operator growth is bounded by `CS(1+S log n)`. Taking `S` sufficiently
small gives the same weak `n^(.001)` propagator bound. Its smallness is
independent of the later empirical moment degree.

For the backward reinsertion, the two response endpoints each satisfy
the normalized Schatten bounds of Section 3. A term with `h` Hessians
has the bound
\[
 \frac{(CS)^h}{h!}
       [C(1+S(h+2)(2B)^{1/(h+2)})]^{h+2}.
\]
The `h=0` term uses the two RMS endpoint bounds. Splitting the remaining
power gives a bounded part and a geometric series beginning at `S^4 B`.
The exterior residual integral supplies `S`, and its deleted forward
control remains the actual `C(1+Z_i)`. Thus the shift is bounded by
`CS(1+S^2B)(1+Z_i)` plus a vanishing remainder. The learned-column
contribution `CS^3(1+Z_i)` is included. Independent incoming/outgoing
cross terms are centered, and the adaptive residual rank-one trace
vanishes with width.

For the forward reinsertion, the endpoint maps `D h` have bounded
operator norm and rank at most `n`. The negative-Gram base trace is
therefore bounded; it never takes a Hilbert--Schmidt norm of the whole
parameter-space identity. Assigning Schatten exponent `2h` to each of
`h>=1` Hessians gives
\[
 \|J-U_0\|_{2,n}
 \le\sum_{h\ge1}\frac{(CS)^h}{h!}
            [1+2Sh(2B)^{1/(2h)}]^h
 \le C(S+S^2\sqrt B).
\]
The bounded part sums exponentially. The carrier part is
`sqrt(2B) sum_h (CS^2)^h h^h/h!`, a convergent geometric series for
small fixed `S`. Multiplying the actual reverse control `CK_i` by the
exterior activity `S`, and including the learned row, gives the forward
shift `CS(1+S^2 sqrt(B))K_i`.

Writing `u_i=K_i/S`, the two inequalities are exactly
\[
 u_i\le G_{\delta,i}/S+A(1+Z_i)+o(1),\qquad
 Z_i\le G_{h,i}+D u_i+o(1),
\]
where `A=C_1(1+S^2B)` and `D=C_2S^2(1+S^2 sqrt(B))`.
Choose `B` first, then impose `S^2B<=1` and
`S^2<=1/(8C_1C_2)`. This gives `AD<=1/2` and hence
\[
 Z_i+K_i/S\le C(1+G_{h,i}+G_{\delta,i}/S)+o(1).
 \tag{A}
\]
Its coefficient is independent of `B` and deletion count. At the first
layer the incoming reference is the fixed-dimensional initial row. At
the top `K_i/S<=C(1+Z_i)` follows directly from the readout integral;
substitution into the forward inequality closes the same absorption.
These are actual closed inequalities, not an assumed joint moment law.

## 5. Gaussian references, complex corrections and budget closure

Parameterizing each real cavity by its own normalized residual activity
gives
\[
 \|h(u)-h(u')\|_{2,n}\le CS^2|u-u'|.
\]
For a backward changed gate, split its reference carrier at `SR`. The
low part is `CS^3R v` and the high part is
`CS sqrt(2B) exp(-c_eta R)`, where `v=|u-u'|`. Choosing
`R=C_eta[1+log(e+B)+log(1/v)]` and `S^2 log(e+B)<=1` gives
\[
 \|\delta(u)-\delta(u')\|_{2,n}/S\le C\sqrt v.
\]
The top gate uses the top carrier term of the joint budget. Its readout
increment needs only RMS. The resulting forward and backward Gaussian
metrics have covering numbers at most `C/epsilon` and `C/epsilon^2`.
Dyadic Gaussian increments give all fixed exponential moments with a
base independent of `B`; the initial forward value also has a bounded
Gaussian exponential moment. Both references remain measurable with
respect to their own retained initialization.

On the stopped complex domain, direct differentiation gives
\[
 \|\dot h\|_{2,n}\le C\rho S,\qquad
 \|\dot\delta\|_{2,n}\le C\rho(1+S^2\ell_n).
\]
The only large product in the second bound is
`||dot z||_(2,n) max|k|<=C rho S^2 ell_n`. Thus the
complex-minus-real forward Gaussian coefficient radius is `C r_n`, and
the backward radius after division by `S` is `C r_n ell_n`.
Two-parameter Lipschitz constants are polynomial logarithmic. Chaining
from these shrinking diameters gives mean at most
\[
 C r_n\ell_n\sqrt{\log(e+\ell_n)}=o(1),
 \qquad r_n=c\ell_n^{-(L+4)},
\]
and a fluctuation scale tending to zero. Every fixed exponential moment
of the correction therefore tends to one. This is the essential new
complex moment step; a real carrier maximum alone would not imply it.

Each cavity is frozen/clamped at its own scaled rectangle, and assigned
the zero reference on failed own initialization. These operations are
cavity measurable. Common-cavity differences are projected as entire
paths onto deterministic Euclidean balls of radius `C_p n^(.01)`.
The corresponding Gaussian radius is `C_p n^(-.49)`. Projection preserves
root independence and is nonexpansive; the preceding real moduli and
complex polynomial grids give vanishing pairing errors with every fixed
exponential moment. No full-network survival event is used as a Gaussian
conditioning event.

Combining (A) with these Gaussian estimates gives a finite moment base
`D` independent of empirical degree `p`. For a distinct `p`-tuple,
the incoming/outgoing root pairs are independent conditional on the common
same-layer cavity. A fixed Hölder split treats projected errors at moment
order proportional to `p`; their moments tend to one for each fixed `p`,
so that does not change the main base. Collision tuples have only
`O_p(n^(p-1))` choices and are controlled by higher fixed moments.

Choose `B>2 L D` and larger than the initial budget limit, then choose
`S` for all preceding smallness conditions. This order is noncircular:
the Gaussian and absorbed scalar bases are independent of `B` after the
stated smallness restrictions. Local remainders may have `B`-dependent
thresholds but vanish before the moment-degree limit. The stopped budget
bounds exceptional contributions. Markov then gives, for each fixed `p`,
\[
 \limsup_n\Pr\{\text{joint budget hit}\}\le L(LD/B)^p.
\]
First take width to infinity, then the infimum over fixed `p`. There is
no moment-degree-dependent label restriction.

## 6. Passive query bounds and the suspected circularity

The temporary query-preactivation cap is needed to make passive deleted
activation controls polynomial logarithmic. It is not needed in a
training moment budget, and it does not enter a nonvanishing same-root
query trace. This last point can be checked directly at the row insertion
used to bound layer `p+1`.

The lower query activation `h^p(v)` has no direct dependence on the
deleted layer-`p+1` row or column. For its training-gradient response,
the exact retained observable is
\[
 Q_{b,\mathrm{full}}^p(v)
 =C_v(\Theta)[\nabla F_b(\Theta,e)+C_b(\Theta)^\top q_b],
 \quad C_v=D_\Theta h^p(v).
\]
Its direct reverse observable derivative gives mean
`delta_{b,i}^{p+1} tr(C_v C_b^T)/n`, bounded by the training carrier
maximum. Its only other same-row mean is the residual integral of
`tr(D Q_b^p J C_a^T)/n`, again multiplied by the training reverse
control. Forward-source terms pair the independent incoming/outgoing
roots and are centered. For an angular derivative there is no direct
reverse observable mean, only the latter mixed endpoint trace.

The exact mixed derivative recursion contains diagonals of lower query
`R` or `J`, plus normalized matrix maps. Its normalized Hilbert--Schmidt
bound uses the RMS of `R,J`; its higher Schatten bound has one lower
coordinate cap `A_p`, never the layer-`p+1` cap. The trace series puts
that one factor outside a convergent series. Thus the next-layer
inequalities are precisely the candidate's (24), with factors
`1+A_p` and no next-layer response on the right. Unbounded reference
features in these maps use their already bounded RMS.

Local comparison transfers the full joint budget, preactivation and
response caps to doubled cavity caps with multiplicative `1+o(1)` or
additive `o(1)` errors. The Gaussian and centered-form estimates are
established before substituting the actual passive controls. Successive
layer choices then give strict response bounds
`C_l S ell_n^(l+1)` and `C_l ell_n^(l+1)`.

The whole initialized real query sphere has preactivation maximum
`C sqrt(ell_n)`: condition on lower initialized features and use a
polynomial query mesh, then interpolate using deterministic operator
bounds. The fresh row's Gaussian law is used before imposing its own
operator-norm event. On the stopped domain, integrating real-time query
responses gives `C ell_n^(L+1)` preactivation size; short complex
time/angle segments have imaginary displacement
\[
 C(1+YS)r_n\ell_n^{L+1}=O(\ell_n^{-3}).
\]
This strictly improves both the temporary `ell_n^(L+2)` size cap and
the fixed pole cap. The order is therefore valid: common-prefix local
comparison, triangular response improvement, query size/pole improvement,
then joint-budget removal. Pole-safe estimates are used only on stopped
prefixes and are improved before continuation. I found no use of the
desired query pole exclusion as an unstopped premise.

## 7. Source spaces and deterministic runtime

On the proved domain, passive whole-query backward recursion is
holomorphic and has RMS `CS`, since its input readout has RMS `CS` and
all its gates and mixers are bounded. The four actual source families
therefore have coordinate magnitude at most `C sqrt(n)`. Their image
pairing remains exact under identical scalar coefficient operations.
The larger source magnitude changes only `log(M/epsilon)=O(log n)`.

At `epsilon=n^(-1)`, `T=O(ell_n)` and `r_n=c ell_n^(-(L+4))`, the
time degree is `C ell_n^(L+6)` and each angular degree is
`C ell_n^(L+5)`. Thus source rank is
`C ell_n^[d(L+5)+1]+2m+d+1`. The initialized training features/images,
first-weight columns and constant are included. Finite initial-jet
continuation supplies the coefficients from allowed initial data; the
source theorem does not require a trained-path oracle.

For the corrected metric, `D/4<=H<=D`, source isometry and inclusion of
the constant give `||1||_H=1` and `||1||_D<=2`. Hence
\[
 \|\phi(z)\|_H\le2b+2s\|z\|_H,
 \qquad\|\operatorname{diag}(\phi'(z))\|_{H\to H}\le2s.
\]
The initial first-weight operator is controlled by exact inclusion of
all columns, and initialized mixers are contractions between source
spaces. These inequalities close a selected RMS feature recurrence and
the independent raw-energy/Gram fitting argument, with no minimum-weight
loss. The algebraically corrected readout is controlled in `H` norm by
the same orthogonal decomposition as in the supplied runtime source.

Pairing errors and learned forward/reverse action defects use RMS plus
coordinate source approximation. They never need a uniform bound on
activation values. A changed backward gate is multiplied by the true
selected reference carrier, whose maximum includes the readout by the
real unbounded theorem. The comparison consequently has the same form
\[
 C\epsilon\exp[C(1+M)S],\qquad M\le1+CS\sqrt{\ell_n}.
\]
With `epsilon=n^(-1)`, the fixed coefficient of `sqrt(ell_n)` is
absorbed by the spare half power of width, yielding a fixed `C/sqrt(n)`.
This does not prove a favorable explicit `C`. The effective-readout
derivative, current Gram inverse and query feature derivative use only
these RMS bounds. Both autonomous systems have sphere-uniform exponential
tails, so increasing the fixed horizon constant includes every later
time and the fitted endpoint.

The corrected inventory is `C(R^2+dR)+Cm(d+1)`, and the diagonal
ordinary-gradient alternative is `C R^4+Cm(d+1)`. Substituting the rank
gives the two exponents claimed by the candidate. The corrected system
retains its established non-gradient optimizer; the diagonal alternative
retains ordinary weighted gradient flow. Neither retains original-width
arrays after setup.

## 8. Scope, nonaffinity and corrections

The example `phi(z)=z+epsilon tanh(z)`, with nonzero fixed epsilon,
satisfies the hypothesis on `|Im z|<pi/4` with
`s=1+2|epsilon|` and `b=0`. It is genuinely unbounded and nonaffine.
The finite-difference positivity argument extends because a polynomial
with bounded derivative is affine. Pairwise nonproportional inputs
therefore give the automatic first-layer gap for this example; full
Gaussian support propagates it. The theorem itself only needs its
explicit gap assumption, so this optional criterion is not a hidden
premise in the proof.

Three presentational errors should be repaired without changing any
mathematics: the exponent in candidate equation (6) has a stray comma,
and two prose lines contain literal `+` artifacts before “and” and
“under.” The correct retained exponent is `2[d(L+5)+1]`.

No stronger numerical conclusion follows from this check. In particular,
the `beta^(-62L)` label allowance, `ell_n^(-1/2)` complex radius,
spherical coefficient improvements and folding constants are not supplied
for this enlarged class. Neither the original real response-memory theorem
nor the affine specialization can replace the complex joint-budget proof
above. Exact-real preprocessing and the stochastic width threshold remain
outside the quantitative resource guarantee.

## 9. Affine boundary check

**Affine verdict: PASS under the same positive gap, small fixed labels and
exact-real preprocessing contract.** A separate scoped internal checker
read the complete candidate, `GENERAL_ANALYTIC_COMPRESSION.md` and
`GENERAL_WEIGHTED_COMPARISON.md`, without prior-study inputs or new route
findings. Its full 279-line report was frozen at SHA-256
`61445768e94011700be5e63fcb02547443e368eec1a0cd280d578d922cc076a6`
in temporary scratch before delivery. I read it completely and reconstructed
the following argument. No additional repository report was created.

Write `phi_l(z)=alpha_l z+b_l 1`. Every feature is affine in the query,
\[
 h^l(t,v)=u_{l,0}(t)+\sum_{j=1}^d u_{l,j}(t)v_j,
\]
and every backward response is independent of the query. On the real RMS
tube, the affine vector field has a fixed polynomial bound and a fixed
Lipschitz constant in the maximum norm of
`||A||_op/sqrt(n), ||W^l||_op, ||w||_(2,n)`. For example a hidden
rank-one velocity is divided by `n`, so its operator norm is the product
of its two normalized vector norms. Complexification uses algebraic
transposes; the same absolute-value norm inequalities hold. Picard
iteration therefore gives a complex time disk of a fixed radius around
every real time, with bounded normalized source norms. Overlapping disks
agree by uniqueness. There are no activation poles and no coordinate
carrier bound is needed.

A Hilbert-valued Chebyshev source on this fixed-width time strip has
coefficient norm at most `2M exp(-c r j/T)`, by its contour integral.
Its tail is at most `C(T/r)exp(-c r p/T)`. For
`T=C_T log(en)` and error `epsilon=n^(-1)`, this requires degree
`p=C log(en)^2`. Approximate the `d+1` affine feature coefficient
vectors and one backward vector at each layer. Include the constant,
exact initialized affine coefficients and first-weight columns. Choosing
individual tolerances smaller by a fixed `d`-dependent factor gives
\[
 \sup_{t\le T,\,\|v\|\le1}\|(I-P_l)h^l(t,v)\|_n\le\epsilon,
 \qquad
 \sup_{t\le T}\|(I-P_l)\delta^l(t)\|_n\le\epsilon,
\]
where `P_l` is orthogonal projection onto a space of dimension at most
`(d+2)(p+1)+2d+2`. These are normalized vector errors, not coordinate
errors. The latter are unnecessary for orthogonal projection.

The finite initial-jet construction also works in this norm. Cover
`[0,T]` by a finite chain of Taylor centers separated by less than
`r/4`. A source bounded by `M` on each radius-`r` disk has coefficient
norm at most `M r^(-j)`. Translating a Taylor series by `h` uses
\[
 a_k^{\rm new}=\sum_{j\ge k}{j\choose k}a_jh^{j-k}.
\]
For `|h|<r/4`, every finite set of desired coefficient orders is
approximated to arbitrary accuracy by finite truncation. Select orders
and tolerances backwards along the finite chain. Finite differentiation
of the known polynomial ODE at time zero then supplies all required
initial derivatives, and scalar linear operations approximate the
interpolation values and coefficients. This uses no trained observation;
temporary derivative orders and precision are unrestricted by the contract.

Let `r_l` be the actual source-space dimension and use counting norm
`||u||_(r_l)=||u||_2/sqrt(r_l)` in the reduced layer. A source isometry
can be chosen with `T_l 1_(r_l)=1_n`, because both constants have unit
norm. Its normalized adjoint is
\[
 T_l^*=(r_l/n)T_l^\top,\quad T_l^*T_l=I,\quad
 T_lT_l^*=P_l,\quad T_l^*1_n=1_{r_l}.
\]
These identities prove both affine commutations in the candidate. No
division by an activation slope occurs, so zero slopes are covered
whenever the gap assumption survives.

For adjacent reduced widths the correct weighted adjoint and physical
hidden update are
\[
 B^{l\dagger}=(r_{l-1}/r_l)B^{l\top},\qquad
 \dot B_C^l=\frac2{m r_{l-1}}\sum_a
               c_{C,a}\delta_C^l h_{C,a}^{l-1\top}.
\]
The first-weight and readout equations retain their displayed factor
`2/m`. This is ordinary gradient flow in the fixed parameter norm
\[
 \|\dot A_C\|_F^2/r_1+
 \sum_{l=2}^L(r_{l-1}/r_l)\|\dot B_C^l\|_F^2+
 \|\dot w_C\|_2^2/r_L.
\]
Thus unequal reduced widths do not change physical time accidentally.
Initial operators are contractions of their original counterparts, and
exact inclusion of initialized affine features preserves the whole
initialized training pass and Gram. The independent real fitting proof
of Section 2 applies to the reduced network before any comparison.

For proof only project the full state to
`A_R=T_1^*A`, `B_R^l=T_l^*W^lT_(l-1)`, and `w_R=T_L^*w`.
Projecting the full rank-one velocities gives exactly the preceding
weighted equations driven by projected full features/responses and the
full residual. The normalization identity is
`h^T T_(l-1)/n=(T_(l-1)^*h)^T/r_(l-1)`. The forward defect is
\[
 -T_l^*W^l(I-P_{l-1})h^{l-1},
\]
and the reverse defect is
\[
 -T_l^*W^{l+1\top}(I-P_{l+1})\delta^{l+1}.
\]
Both are `C epsilon` in their reduced normalized norm. Hence initialized
matrix-image source families are not missing: their role in coordinate
sampling is replaced here by the operator bound and orthogonal projection.

The readout is also not a missing source. From zero initialization,
\[
 \|(I-P_L)w(t)\|_n
 \le2\epsilon\int_0^t\rho_n(s)\,ds\le C\epsilon.
\]
This remains true even if `alpha_L=0`, when the top backward response
does not determine the readout. The observation defect is
`< (I-P_L)w,(I-P_L)h^L >_n`, and is in fact `C epsilon^2` under
these two source bounds.

Let `E(t)` be the sum of the normalized parameter distances from this
projected reference. Affine commutation and constant gates give forward
and backward differences `C(E+epsilon)`. Pairing defects then give the
same bound on the actual tangent-Gram difference. With
`u=c_C-c_n`, both initial errors zero, the independent reduced Gram
margin yields
\[
 D^+\|u\|_m\le-\kappa\|u\|_m+C\rho_n(E+\epsilon),
 \quad
 \int_0^t\|u\|_m\le C\int_0^t\rho_n(E+\epsilon).
\]
Parameter subtraction gives
`E(t)<=C int||u||_m+C int rho_n(E+epsilon)`. Integral Gronwall uses
the finite residual activity, not `T`, and proves `sup_(t<=T) E<=C/n`
and uniform sphere output error `C/n`. The independently proved
exponential tails of both affine flows are `C/n` after increasing
`C_T`; this includes all later times and their fitted endpoints.

The inventory is
`d r_1+sum_(l>=2)r_l r_(l-1)+r_L+O(sum_l r_l+m(d+1)+L)`,
therefore `O(log(en)^4)` at fixed data. Full isometries, source vectors,
original matrices and temporary derivatives are discarded after setup.

Finally, affine population covariance has the explicit form
\[
 Q^L=\left(\prod_{l=1}^L\alpha_l^2\right)Q^0+
 \left(\sum_{j=1}^Lb_j^2\prod_{k=j+1}^L\alpha_k^2\right)11^\top.
\]
Thus its rank is at most `d+1`; identity gives exactly `Q^0` and
requires linearly independent training inputs with `m<=d`. This boundary
case supplies no proof for fixed nonlinear perturbations, since the
commutation identities then fail.

## 10. Final status

Both the nonlinear qualitative extension and the separate affine
refinement pass this internal reconstruction under their stated inherited
interfaces. The review does not elevate those interfaces into promoted
book results. It does close the new unbounded-value substitutions and
joint complex-budget/query feedback needed by this candidate. The exact
three formatting repairs in Section 8 do not alter the checked mathematics.
