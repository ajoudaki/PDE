# Independent reconstruction of the square-root-log source radius

2026-10-04. Scoped internal check, not a promotion review.

**Verdict: PASS for the proposed refinement of the stated source
interfaces.** The new maximum stop can be excluded without first removing
the exponential budgets, and the larger radius
\(r_n=c[\log(en)]^{-L/2}\) is justified. The resulting total-storage
power is \(dL+2d+2\), conditional on the inherited quadratic-storage
runtime, exactly as the candidate states. This check does not independently
certify the prior-study insertion theorem or the inherited runtime.

A minor clarification is supplied below: the negative-real part of the
time rectangle is absorbed into the same small Gaussian correction as the
vertical part. It does not change any bound or conclusion.

## 1. Frozen inputs and scope

The reviewed candidate is DEPTH_EXPONENT_ROUTE.md at SHA-256
e95e6875478cacc80fd62ae57cdcfff8e8e173570ba78f5057abec8e519bf2c6.
The complete additional inputs read were:

| File | SHA-256 |
|---|---|
| DEEP_COMPLEX_SOURCE.md | 7a81a04bb3e52a1c60ee83f479238ea1dec54fe2b70277b4f7d513b5eb84c6f2 |
| DEEP_ACTIVATION_EXTENSION.md | b5279562acc5d8ffceaad2d8ac744d43e51c4af91d0508e66804ab12954ef141 |
| DATASET_SOURCE_CONSTANTS.md | 340fae2324747c34225cc3ee4993452549f9296fd3ac7271e35061ae2fcf7ac6 |
| LABEL_SEPARATE_BUDGETS.md | 6800fb4d51cf1adc43cd56d987ef0e13e51b0c8d00c6106452416a624886b594 |
| WHOLE_QUERY_RESPONSE_SOURCE.md | 9222c93f0bb9d0c6943f86192cc4a8ad1bbb6b3f6199dd2b056b15fc3adec0d4 |
| SAMPLE_COUNT_REFINEMENT.md | d1de9321308530b9cd648e3ffd25f4987f42b2a343260d087cae924fd13f7242 |

No linked prior-study proof, prior check report, or other current agent
report was read. Status labels in source introductions were not used as
mathematical evidence. The check reconstructs the new implication using
the actual displayed local insertion, trace, and real-fitting interfaces.
The canonical-notation skill and neural reference, rigorous-solution
skill, and conjecture-investigation skills were already read and applied.

The actual reference, zero readout, Gaussian initialization, squared mean
loss, mobilities, physical time, fixed-data quantifiers, and bounded
strip-holomorphic activations are unchanged. Write
\(\ell_n=\log(en)\), \(\lambda=\min(1,\gamma/m)\),
\(S=C_0Y/\lambda\), and \(T=C\lambda^{-1}\ell_n\).
All new statements use the existing \(Y\le c\lambda\) regime.

## 2. The needed derivative bound does not presuppose the new maximum

On any pole-safe physical tube, bounded feature norms and the exact
updates give
\[
 \|\dot w\|_2/\sqrt n\le C\rho,\qquad
 \|\dot A\|_F/\sqrt n+
 \sum_{\ell\ge2}\|\dot W^{(\ell)}\|_F\le CS\rho,
\]
where \(\rho=\|f-y\|_2/\sqrt m\). Forward differentiation therefore
gives \(\|\dot z_a^{(\ell)}\|_2/\sqrt n\le CS\rho\).
If the carrier coordinate maximum is at most \(M\), then
\[
 \dot\delta_a^{(\ell)}
 =\phi_\ell''(z_a^{(\ell)})\odot
       \dot z_a^{(\ell)}\odot k_a^{(\ell)}
   +\phi_\ell'(z_a^{(\ell)})\odot\dot k_a^{(\ell)}.
\]
The first term has RMS at most \(CSM\rho\).
In \(\dot k=\dot W^\top\delta+W^\top\dot\delta\), the new matrix
term has RMS at most \(CS^2\rho\). Descending through fixed depth,
starting with \(\dot k^{(L)}=\dot w\), proves
\[
 \max_{a,\ell}\|\partial_t\delta_a^{(\ell)}\|_2/\sqrt n
 \le C\rho(1+SM).                                      \tag{1}
\]
The same calculation is algebraic on a complex pole-safe tube.
There \(\rho\le CY\), by the short-contour residual bound.

Consequently the old budget cap \(M=CS\ell_n\) already gives a
polynomial-logarithmic derivative bound. Imposing the stronger stop
\(M=C_*S\sqrt{\ell_n}\) improves that bound, but is unnecessary to
the logical validity of the first Gaussian grid estimate.

## 3. Conditional Gaussian grid and the new stop

For each singleton cavity, define its reference on its own stopped
rectangle. Coordinatewise clamp the containing deterministic rectangle
to this smaller rectangle, and use zero if its retained initialization
conditions fail. The clamping bounds depend only on retained initialization.
It is 1-Lipschitz in the real and imaginary time coordinates; the
reference remains independent of the omitted outgoing root
\(x_i\sim N(0,I/n)\).

The cavity response obeys \(\|\delta_a^{-i}(z)\|_2/\sqrt n\le CS\).
At a fixed grid point, the real and imaginary parts of
\(x_i^\top\delta_a^{-i}(z)\) are centered Gaussians with variance
at most \(C S^2\). Their real-valued root is important: algebraic
transposes do not change this variance bound after taking real and
imaginary parts separately.

A mesh of spacing \(n^{-2}\) in both time coordinates has at most
\(C_{\rm data}n^4\ell_n^C\) points. On
\(\|x_i\|_2\le C\), (1) gives off-grid error at most
\[
 Cn^{-2}\sqrt n\,Y(1+SM)=o(S)
\]
for every fixed positive \(S\). The Gaussian root-norm failure has an
exponential tail. A pointwise Gaussian tail at threshold
\(K S\sqrt{\ell_n}\) is at most \(C e^{-cK^2\ell_n}\).
Union over the grid, \(n\) roots, fixed layers, and fixed samples
therefore succeeds with probability tending to one when the structural
constant \(K\) is sufficiently large. Factors involving fixed
\(m,\lambda,Y\) affect only the width threshold.

This proves the candidate's uniform cavity bound with a structural
constant \(C_G\). The inherited singleton shift,
\[
 |k_{a,i}^{(j)}-x_i^\top\delta_a^{(j+1),-i}|
 \le CS(1+S^2B)+o(1),
\]
then improves the full maximum stop
\(C_*S\sqrt{\ell_n}\), with \(C_*>2C_G\), for sufficiently large
width. Its bounded shift divided by \(S\sqrt{\ell_n}\) tends to zero.
No conditional Gaussian law has been asserted for the adaptive full
response.

The new full stop transfers to every fixed-size cavity: the inherited
coordinate insertion error is \(o(1)\), whereas the cavity cap is
\(2C_*S\sqrt{\ell_n}\). The same insertion comparison transfers
each separate exponential budget, query pole cap, and response cap.
Thus cavity survival is a deterministic continuation statement on the
insertion event, not a conditioning event in the Gaussian calculation.
The singleton grid constant need not grow with the later moment degree.

## 4. The inherited local insertion estimates allow the larger radius

The source and its activation supplement explicitly retain strict powers
of \(n\) in the following places:

- linear root-coordinate tolerance \(n^{-1/10}\);
- linear variation norm \(n^{1/100}\);
- remainder stop \(n^{-1/25}\);
- propagator bound \(n^{1/1000}\);
- control-net logarithm \(n^{5/8}\) times a fixed polylogarithm;
- Gaussian quadratic-tail exponent of order \(n^{0.79}\).

Replacing one fixed inverse-polylogarithmic contour width by another
does not close any of those power gaps. The contour's non-real and
negative-real length remains \(O(r_n)=o(1)\). Products of the bounded
base propagators therefore cost one factor \(e^{Cr_n}\), not one
factor per Dyson insertion. The long positive-real portion is the
unchanged contractive part.

The augmented graph uses only bounded gate derivatives, explicitly
normalized matrix actions and pairings, and fixed polylogarithmic
coordinate caps. Smaller carrier and response caps preserve these
hypotheses. The source includes forward applications of the incoming-row
adjoint probes and the top-neuron residual offset, so neither direction
of the deletion is silently omitted.

This verifies applicability of the stated local insertion interface.
It is not a new proof of its prior-study Gaussian/control theorem.

## 5. Response powers and exclusion of query poles

The two source trace recurrences on common stopped prefixes are
\[
 \max|R_b^{(p+1)}|
 \le C\{M+S\sqrt{\ell_n}+SM(1+A_p)+S^2M\}+o(1),
\]
\[
 \max|J_j^{(p+1)}|
 \le C\{\sqrt{\ell_n}+SM(1+A_p)+SM\}+o(1).
                                                               \tag{2}
\]
Here the lower-layer response maximum \(A_p\) has the appropriate
forward or angular type. These formulas are obtained from lower query
gates and training responses; they do not require the next query gate
to have already been proved safe.

The first forward response is a bounded input pairing times
\(\delta_b^{(1)}\), so its maximum is \(CS\sqrt{\ell_n}\).
For the first angular response, Gaussian first-weight rows have norms
\(C\sqrt{\ell_n}\). Integrating the first-weight equation along total
activity \(CS\) adds at most \(CSM\) per row. Thus its maximum is
\(C\sqrt{\ell_n}\).

Substitute \(M=C_*S\sqrt{\ell_n}\) into (2). If
\(A_p=C_pS\ell_n^{p/2}\) in the forward recursion, its largest
power comes from \(SM A_p=C_*C_pS^3\ell_n^{(p+1)/2}\).
For angular responses it is \(C_*C_pS^2\ell_n^{(p+1)/2}\).
Choosing successive fixed layer constants with strict slack proves
\[
 \max|R_b^{(\ell)}|\le C_\ell S\ell_n^{\ell/2},
 \qquad
 \max|J_j^{(\ell)}|\le C_\ell\ell_n^{\ell/2}.          \tag{3}
\]
There is no requirement that \(S\sqrt{\ell_n}\) be small.

At a real time and real query the preactivation is real. Move vertically
in time and then in the \(d-1\) angle coordinates. The exact equation
\(\dot z=-(2/m)\sum_b r_bR_b\), Cauchy--Schwarz in the normalized
sample sum, and (3) show that the imaginary displacement is at most
\[
 Cr_nSY\ell_n^{L/2}+C_dr_n\ell_n^{L/2}
 =Cc(1+SY).
\]
The structural constants may depend on fixed depth. Choose \(c\)
small enough for a strict fixed pole margin. A bound tending to zero
is not required for this continuation step.

## 6. Exponential budgets on the enlarged domain

After imposing the new maximum stop, (1) and \(Y/S=C\lambda\le C\)
give the normalized complex-response derivative bound
\[
 \|\partial_t\delta_a\|_2/(S\sqrt n)
 \le C(1+S^2\sqrt{\ell_n})\le C\sqrt{\ell_n}.
\]
The vertical correction therefore has Gaussian radius bounded by
\[
 D_n=Cr_n(1+S^2\sqrt{\ell_n})
 \le C\ell_n^{-(L-1)/2}.                              \tag{4}
\]
Its horizontal and vertical Lipschitz constants are at most
\(C\sqrt{\ell_n}\), by subtracting the two first derivatives for
the horizontal direction. A second time derivative is unnecessary.
Clamping preserves these bounds.

To include negative real time explicitly, take the real anchor to be
\(\max(\Re z,0)\). The segment from that anchor to \(z\) has length
at most \(2r_n\) in the left portion of the rectangle. It contributes
the same bound (4), up to a fixed constant. The positive real reference
has the inherited single-sample activity-clock modulus, including
freezing at its own stop. The small negative segment therefore needs
no extension of that positive-time modulus.

At normalized Gaussian resolution \(\epsilon\), the complex correction
has covering number at most
\((C\lambda^{-1}\ell_n^C/\epsilon)^2\). Starting a dyadic net at
radius \(D_n\), the expected Gaussian supremum is bounded by
\[
 CD_n\sqrt{\log(C\lambda^{-1}\ell_n^C/D_n)}.
\]
For every fixed \(L\ge2,\lambda>0\), this tends to zero; for the
borderline \(L=2\) it is bounded by
\(C\ell_n^{-1/2}\sqrt{\log\ell_n+\log(1/\lambda)}\).
The dyadic Gaussian tail has scale \(CD_n\), so every fixed
exponential moment of the correction tends to one.

Combine that moment with the real single-sample moment by
Cauchy--Schwarz. Choose its structural bound first, then a structural
budget \(B\), then small structural \(S\). The new maximum constant
comes from physical RMS bounds and the polynomial grid; it introduces
no dependence on \(m\) or the later moment degree into this choice.

The common-cavity difference projection and its Gaussian grid estimate
remain valid because their radii have a strict negative power of \(n\)
and all Lipschitz constants remain polynomial. The fixed-sample
moment expansion therefore gives, for each fixed integer \(p\),
\[
 \limsup_{n\to\infty}
 \Pr\{\text{some full budget hits }B\}\le m\vartheta^p,
 \qquad 0<\vartheta<1.
\]
Width tends to infinity before the infimum over \(p\). This closes the
last stop under the original \(Y\le c\lambda\) condition.

The order is noncircular: impose all stops; use the singleton Gaussian
grid to improve the maximum; use triangular traces to improve response
and pole caps; use the shrinking Gaussian correction to remove budgets.
Each Gaussian reference is always defined on its own stopped domain.

## 7. Approximation, autonomy, and count

Bounded complex gates, bounded mixer operators, and readout RMS
\(CS\) give coordinate bound \(C\sqrt n\) for all four whole-query
source families and their paired initialized images. This uses only
operator/RMS bounds for passive backward queries; no new query-carrier
maximum is inserted into the dynamical comparison.

Set \(q_n=\ell_n+\log(e/\lambda)\) and approximation tolerance \(n^{-1}\).
The time and angular degree bounds are
\[
 p\le C(T/r_n)q_n
   =C\lambda^{-1}\ell_n^{L/2+1}q_n,\qquad
 J\le Cr_n^{-1}q_n=C\ell_n^{L/2}q_n.
\]
Their product yields
\[
 R\le C(p+1)(2J+1)^{d-1}
 \le C\lambda^{-1}\ell_n^{dL/2+1}q_n^d.
\]
The exact initialized vectors cost \(O(m+d)\) and are absorbed by
\(m\lambda\le B_\phi^2\). Identical scalar coefficient operations
on each initialized matrix-image pair preserve the required exact pairing.
Finite initialization-jet preprocessing remains valid on the enlarged
holomorphic rectangle.

The inherited runtime retains \(O(R^2)\) reals, giving
\[
 C\lambda^{-2}\ell_n^{dL+2}q_n^{2d}+Cm(d+1).
\]
For \(\ell_n\ge\log(e/\lambda)\), this is
\(C\lambda^{-2}\ell_n^{dL+2d+2}+Cm(d+1)\).
Only source spaces change. The own-residual optimizer, physical clock,
actual finite-n reference, source accuracy, one-reference stability
estimate, and tail continuation all remain their inherited versions.
Thus the same all-time, whole-sphere \(C_{\rm data}/\sqrt n\)
comparison follows as an implication from that runtime bridge.

No depth-independent exponent, unrestricted storage lower bound,
growing-data result, or efficient preprocessing theorem follows here.
