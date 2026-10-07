# Scoped check of the finite-order insertion reduction

2026-10-07. Independent isolated check of
`QUANTITATIVE_INSERTION_WIDTH.md`. The first frozen version had SHA-256
`609609dab3a25672f2dcc5f576b641e8e933882e03aba795c91173a848d19b4c`.
The corrected version checked after the author addressed the findings has
SHA-256
`40fc026d7e0d18b968ae1526a94792290dc25cd56f97972db526dfd3e8aeb31b`.
Section 6 records that final reconciliation. Section 1 retains the exact
findings against the first version; they are resolved in the corrected
version, including the distinction between proved finite-net statements
and explicitly outstanding continuum estimates.

The collision bound, the Hölder correction bound, the fixed-control
Gaussian bounds, and the amplitude-scaled identities and linear recurrences
in Section 6 check under their stated stopped-source hypotheses. This is
not a blanket validation of a local insertion theorem or a stochastic
success-width theorem. The corrected candidate specifies centering in (18),
includes the full multiplier of (19) in the coefficient controlled by (20),
and distinguishes a finite control-net union from its extension to every
admissible control. It supplies the linear control interpolation modulus
and root-norm event while leaving the quadratic and terminal-time moduli
open. No defect remains in the conditional statements checked here.

## 1. Exact interface qualifications

**Quadratic centering, candidate lines 274–288.** Let
\(\xi\sim N(0,I_{2pn}/n)\) and let \(R\) be deterministic after
conditioning on the retained cavity and fixing the controls. Equation (18)
is a bound for
\[
 \Pr\{|\xi^\top R\xi-\operatorname{tr}(R)/n|>n^{-b}/4\},
\]
not for the uncentered quadratic form. For independent-root bilinear forms
the mean is zero. The candidate's Gaussian-square calculation is the
centered calculation, but the event being bounded is not written. Stating
it explicitly is necessary: \(R=I\) would otherwise give a quadratic
form with mean \(2p\), which does not have the asserted small uncentered
tail. For complex absolute-value events, splitting into real and imaginary
parts also requires the corresponding two tests and union factor; retaining
them as separate tests, as the candidate suggests, is valid.

**Unnamed remainder multiplier, candidate lines 298–314.** Suppose the
literal assertion preceding (19) means that the integrated remainder is
bounded by
\[
 C_0A_JA_R\ell_n^k n^\kappa
 [n^{-8/100}+u^2+Tn^{-48/100}+A_{\rm src}n^{-1/2}].
\]
For \(n\ge1\) and \(u\le n^{-1/25}\), the bracket is at most
\(2(1+T+A_{\rm src})n^{-8/100}\). Therefore (20), as written,
implies only the bound \((C_0/4)n^{-1/25}\). An unrestricted unnamed
\(C_0\) prevents the claimed strict improvement. The direct repair is to
define \(A_R\) to include every multiplicative remainder constant and
replace “a fixed multiple of” by an actual upper bound. With that
normalization, (20) gives the stronger cap \(n^{-1/25}/4\). Alternatively,
include \(C_0\) in (20). This is a coefficient-normalization issue in the
conditional interface; no nonlinear coefficient is being certified here.

**Finite net versus all controls, candidate lines 241–296.** The
cardinality (16) and fixed-control tails (17)–(18) give a finite-net event.
To obtain an event uniform over the continuous control class, specify and
pay the norm of the change in every tested map when each scalar control
changes by at most the net accuracy. A bound on each map's operator norm
alone does not bound that change. The union over terminal times likewise
requires a terminal-time modulus, already identified as outstanding by the
candidate.

For the linear maps of Section 6 the missing interpolation step can be
made concrete without a new scientific assumption. Put
\(\tau=n^{-1/8}\). For two fixed control collections at sup distance at
most \(\tau\), the difference of their parameter response operators has
norm at most
\[
 \sqrt p\,J_n\tau
 (2T\Gamma\tau_*+M_\delta+Sf_*).
 \tag{C1}
\]
This follows by replacing both control amplitudes in (26) by \(\tau\),
because the reference coefficients in (25) do not depend on the controls.
The analogous forward/backward map moduli follow from (27) with the same
replacement. To turn these operator moduli into pathwise interpolation
errors, multiply by the Euclidean norm of the concatenated Gaussian roots.
For example,
\[
 \Pr\{\|\xi\|_2>2\sqrt{2p}\}\le e^{-pn}
 \tag{C2}
\]
follows from the Gaussian norm concentration proof in the fitting note,
since \(\mathbb E\|\xi\|_2\le\sqrt{2p}\) and its Lipschitz
constant in standard Gaussian roots is \(n^{-1/2}\). On this event the
parameter interpolation error is bounded by
\[
 2\sqrt2\,pJ_n\tau
 (2T\Gamma\tau_*+M_\delta+Sf_*).
\]
An explicit gate must put each resulting error below its allocated fraction
of \(n^{-b}\). The root event must be unioned over the deletion sets.
For quadratic forms the corresponding error is bounded by
\(\|R-R'\|\|\xi\|_2^2\), and its centered version also includes
\(|\operatorname{tr}(R-R')|/n\). Their control moduli still need the
separate quadratic-response calculation. Thus (16)–(18) are verified as
fixed-control and finite-net interfaces; they are not by themselves a
completed adaptive-control event.

## 2. Collision and correction factors

Here \(p\) is a positive integer and \(D\ge1\). With the candidate's
source constants, \(\max_j\tau_j=\tau_1=V_1\) and \(s\ge1\) give
\(W_{\rm G}\ge128\max(1,H_{\max},\max_j\tau_j)\). Consequently
\[
 2\eta K_{\rm src}
 \le\frac{1+C_G}{32W_{\rm G}}
 \le\frac{33}{4096}<\frac1{100}.
\]
Since \(\sqrt{\ell_n}\le\ell_n\) for \(n\ge1\), this proves
the stated cap \(W_n=e^{1/100}n^{1/100}\) on the stopped maximum event.
The event's own failure probability is not removed by this argument.

For an ordered tuple with \(k\) distinct labels, retain one factor for
each label and bound its repeated factors by \(W^{p-k}\). Its expected
contribution after multiplication by the event indicator is at most
\(D^kW^{p-k}\). A partition into \(k=p-j\) blocks maps injectively
to its \(j\)-edge collection of stars centered at each block's least
element. There are therefore at most
\(\binom{\binom p2}{j}\le\binom p2^j/j!\) such partitions. Counting
at most \(n^k\) choices of distinct labels proves (7) exactly, without
independence or higher moments of a repeated root.

For \(n\ge4p^3\), its exponent is at most
\[
 \binom p2\frac{W_n}{Dn}
 \le\frac{e^{1/100}}{2\,4^{99/100}}p^{-97/100}<1.
\]
Thus the factor \(e\), the sample/layer union in (8), and the confidence
choice (9) are valid at every displayed width. For a budget hit, one layer
average must reach \(\mathcal B/L\); this accounts for the factor
\(mL\) and the ratio \(16L/\mathcal B\). The assumed distinct-root
moment bound through order \(p\) remains an input.

For (12), Cauchy–Schwarz followed by Hölder gives explicitly
\[
 \mathbb E[\mathbf1_E\prod_i B_i]
 \le D_0^k
 \left(\prod_{i=1}^k
   [\mathbb E e^{2akE_i}]^{1/k}\right)^{1/2}
 \le D_0^k e^{ak\mu+a^2k^2v^2}.
\]
No correction independence is used, and the sufficient condition involving
\(a\mu+a^2pv^2\) has the correct power of \(p\). Conditional
Gaussian concentration gives the unconditional version of (11) when its
mean and radius bounds hold uniformly in the retained initialization.
Projecting the entire independently stopped difference path preserves
the required omitted-root independence. The physical Euclidean projection
radius \(C_pn^{1/100}\) becomes Gaussian radius
\(C_pn^{-49/100}\) after division by \(\sqrt n\).

The entropy estimate (14) also has the stated dependence. At level \(j\),
the number of increments is bounded by
\(C(1+2^jA/v)^2\), and each increment has standard deviation at most
\(2^{1-j}v\). Bounding the expected maximum by its Gaussian tail and
summing the resulting geometric series gives (14). For example, a loose
universal coefficient \(C_{\rm num}=32\) covers a supremum of absolute
values, including the initial level. The degenerate case \(v=0\) is
deterministic and should be interpreted separately. The bound used after
(15) is correct: with \(u=\log x\ge0\),
\((3+u)^{3/2}e^{-u/2}\) is nonincreasing and has maximum \(3\sqrt3\).
This does not supply the missing complex-contour metric coefficients.

## 3. Net size and Gaussian normalization

Sampling each scalar control at at most
\(2+4TDn^{5/8}\) time points and quantizing to a mesh of spacing
\(\tau/2\) uses at most \(1+4M/\tau\) values per point. Linear
interpolation has error below \(\tau\), proving (16). Zero amplitude
or zero speed is handled by a constant control, without division by zero.
For an interior deletion there are two controls per sample and omitted
neuron, hence \(2mp\) real controls. Complex segments require the real
and imaginary control count separately.

For a real linear map \(R\) on the roots with
\(\|R\|\le A n^\kappa\ell_n^k\), each coordinate of \(R\xi\)
has variance at most \(A^2n^{-1+2\kappa}\ell_n^{2k}\). The scalar
Gaussian tail at \(n^{-b}/4\) is exactly bounded by (17). Further,
\[
 \mathbb E\|R\xi\|_2
 \le \|R\|_F/\sqrt n
 \le\sqrt{2p}\,A n^\kappa\ell_n^k.
\]
The Frobenius estimate uses the input dimension \(2pn\), not the
possibly much larger output dimension. If this mean is at most
\(n^{1/100}/2\), concentration gives the upper tail
\[
 \exp\left[-\frac{n^{1+2/100-2\kappa}}
                   {8A^2\ell_n^{2k}}\right],
\]
which is stronger than (17). This mean gate is an additional width gate;
it is not implied merely by the scalar-coordinate tail.

For the centered quadratic form, diagonalize the symmetric part. The
Gaussian-square moment generating function gives
\[
 \Pr\{|\xi^\top R\xi-\operatorname{tr}(R)/n|>u\}
 \le2\exp\left[-\min\left\{
       \frac{n^2u^2}{16\|R\|_F^2},
       \frac{nu}{4\|R\|}\right\}\right].
\]
Using \(\|R\|_F^2\le2pn\|R\|^2\) and \(u=n^{-b}/4\)
gives coefficients \(1/512\) and \(1/16\) in the two exponents.
Thus the candidate's common smaller coefficient \(1/1024\) is safe.
The \(p\) in the first denominator is required. The block-matrix
representation of independent-root bilinear forms is correct.
There are at most \(Lp n^p\) nonempty same-layer deletion sets of
size at most \(p\), giving the stated logarithmic union cost.

## 4. Scaled flow and linear coefficients

Keep the candidate's notation, assume \(Y>0\), and use the unchanged
source allowance \(S=16Y/\lambda\le1\). The following statements
are conditional on the source's stopped operator, feature, carrier,
activity, and contour bounds. They do not prove survival of these stops.
The incoming-row and outgoing-column formulas concern interior deletion;
the first layer has no incoming Gaussian reverse source, and the top
layer has no outgoing Gaussian column.

Since \(r_a=S\bar r_a\), \(q_a=S\bar q_a\), and
\(\Theta=\Theta_0+S\bar u\), the chain rule gives
\[
 \nabla_{\bar u}\overline{\mathcal F}_a
   =\nabla_\Theta\mathcal F_a,\qquad
 D_{\bar u}h=S D_\Theta h.
\]
Dividing the original retained equation by \(S\) therefore gives (21),
including its reverse-force factor, and the three blocks in (22). Zero
initial readout gives \(\overline{\mathcal F}_a=\bar u_w^\top h_a^{(L)}\)
exactly. Neither a reverse-source scalar nor its derivative is added to
the forward residual.

The source's total activity and pointwise residual bounds give
\(2\int\bar\rho\,|dt|\le1\) and \(\bar\rho\le\lambda/8\).
In particular no lower bound on \(S\) is used. Physical differentiation
gives
\[
 \|\dot z_a^{(j)}\|_{2,n}\le2S^2\bar\rho V_j,
\]
and, for \(j<L\),
\[
 \|\dot{\bar\delta}_a^{(j)}\|_{2,n}
 \le10s\|\dot{\bar\delta}_a^{(j+1)}\|_{2,n}
 +2sS^2\bar\rho\tau_{j+1}^2H_j
 +2tM_nS^2\bar\rho V_j.
\]
At the top, the first term is replaced by \(2s\bar\rho H_L\).
Using \(S^2\le1\), then converting RMS speeds to coordinate speeds,
proves exactly (23). The factor \(\sqrt n\) in its control Lipschitz
bound is necessary.

The zero-source variational generator is unchanged because
\[
 D^2_{\bar u}\overline{\mathcal F}_a=S D^2_\Theta\mathcal F_a,
 \qquad \bar r_a=r_a/S.
\]
Thus the residual Hessian retains its original coefficient, as does the
negative Gram. The source allowance implies the two numerical exponents
in (24). Its complex factor two still requires the source's deterministic
short-contour gate; the calculation does not make that gate automatic.

The external derivatives (25) follow from
\(D_{e_a}\overline{\mathcal F}_a=\bar\delta_a^{(j+1)}\) and
\(D_{\bar u}\bar\delta_a^{(j+1)}=D_\Theta\delta_a^{(j+1)}\).
The augmented Hessian yields \(\|B_a\|\le M_\delta\), while
\(\|C_a\|\le Sf_*\). In the rank-one term,
\[
 \|\nabla_{\bar u}\overline{\mathcal F}_a\|_2\le\sqrt n\,\Gamma,
 \qquad \|\bar\delta_a^{(j+1)}\|_2\le\sqrt n\,\tau_*.
\]
Their product cancels the displayed \(1/n\), giving
\(\|\bar P_a\|\le2\Gamma\tau_*/m\). Summing over samples
removes \(1/m\); the residual-weighted terms instead use
\(m^{-1}\sum_a|\bar r_a|\le\bar\rho\). This accounts for every
sample factor in (26).

For each outgoing root, integration bounds its operator coefficient by
\(J_nA_n(2T\Gamma\tau_*+M_\delta)\); for each incoming root it gives
\(J_nSf_*B_n\). Cauchy–Schwarz over root blocks proves (26), since
\(\sqrt{a^2+b^2}\le a+b\). All controls are fixed for this linear
Gaussian interpretation; substituting adaptive controls requires the
uniform event discussed above.

For (27), an insertion-induced \(\bar u\) variation changes the
physical mobility coordinates by \(S\) times that variation. The
augmented preactivation derivative therefore gives
\(Z_j=P_j(SV_n+\sqrt p A_n)\). A changed backward gate is multiplied
by the reference scaled carrier, whose coordinate maximum is \(M_n\).
The changed-mixer contribution satisfies
\[
 \|(S\Delta\bar u_{H^{(j+1)}}/\sqrt n)^\top
                 \bar\delta_a^{(j+1)}\|_2
 \le S\tau_{j+1}\|\Delta\bar u_{H^{(j+1)}}\|_F.
\]
This proves the \(S\tau_{j+1}V_n\) term and the rest of (27).
Adding a reverse-port bound at every lower layer only enlarges the bound.
The recurrences depend on \(p\) through \(\sqrt p\). After multiplying
by a root norm of order \(\sqrt p\), a coarse full-image or interpolation
bound can scale as \(p\); the operator statement must not be read as
a \(\sqrt p\) bound for every random image.

Finally the physical mixer update has coefficient \(S^2\bar r_a\)
times a scaled backward response. Integration using total normalized
activity at most one gives precisely the two learned-row/column bounds
preceding (28). Multiplication by the relevant control and summation over
the \(p\) omitted neurons gives (28), with \(pS^2/\sqrt n\), not
\(\sqrt pS^2/\sqrt n\). At the top,
\(w_i/S=\bar u_{w,i}\) has modulus at most \(M_n\); hence the
scaled prediction offset is at most \(pM_nA_n/n\), and it multiplies
both retained force terms. No factor \(1/S\) is missing in these bounds.

These checks certify the displayed conditional identities and coefficient
recurrences. They do not certify the separate quadratic response maps,
uniform interpolation/terminal-time gates, normalized nonlinear insertion
error, projected common-cavity coefficient, or finite-confidence source
success. Those remain the candidate's open local obligations.

## 5. Frozen input record

The required rigorous-math skill, canonical-notation skill, and its neural
reference were read. The complete scientific inputs were only the frozen
candidate and the following seven assigned files; no links to additional
research were followed. No README, history, other review of this candidate,
maintained book, experiment, or Git operation was used. The only write is
this report.

- `EXPLICIT_FITTING_WIDTH.md`:
  `62d018c6448b0e6af6085827a856667ba58747810c6b284452dea21ce800919d`.
- `UNBOUNDED_COMPRESSOR_BRIDGE.md`:
  `e018f0291b4456913a6541d5db7d90a678c4564928edcd5f47dd8c5326336f5d`.
- `UNBOUNDED_ACTIVATION_CANDIDATE.md`:
  `e939e971d7a9e1b884b42d73d3ce65f5b1f548d9e25ab9cfe76c0502aa591713`.
- `UNBOUNDED_INSERTION_CHECK.md`:
  `bec5707fccc99597570ce51c94d3a487fd0b1ede14578617275cb708fdd95578`.
- `DEPTH_CAVITY_ROUTE.md`:
  `e8f9f43c137a9c74b751cbd2e54cf5a2b13f090c560d912b4b17994c53bc1478`.
- `DEPTH_INSERTION_CHECK.md`:
  `77c51e725629e736a33c16dbe4ec179b5aa859b527539815f55422a818a1e977`.
- `DEPTH_CAVITY_PROBABILITY_CHECK.md`:
  `e8ec625d60753186ee5a74e67458e1f048c7edc313dc0155de54cf193e307993`.

## 6. Author-correction reconciliation

After the first-version findings were delivered, the author made the
identified corrections. The complete intermediate version at hash
`0c69b40d2ca603644b3ca7e3cdef8331ea035ce6e01edb70acff33d7766dfdd5`
was reread. The final real/complex bookkeeping patch was then read and
verified at final hash
`40fc026d7e0d18b968ae1526a94792290dc25cd56f97972db526dfd3e8aeb31b`.
The supporting scientific inputs are unchanged.

The corrected text now explicitly centers the quadratic form, incorporates
every fixed multiplier into \(A_R\), and calls the probability union a
finite-grid estimate. Its new (18a) is exactly (C2) above. Its new (18b)
uses the maximum of the recurrences (26)–(27) with only the two control
amplitudes replaced by the control difference \(\tau\). Keeping
\(M_n,M_\delta,J_n\) and the reference bounds unchanged is correct:
the controls change, but the reference trajectory and its derivatives do
not. This supplies the explicit linear interpolation gate.

For quadratic interpolation the new factor \(10p\) is correct. On
the root-norm event the quadratic difference costs at most
\(8p\|R-R'\|\), while its normalized trace difference costs at most
\(2p\|R-R'\|\). Their sum gives \(10p\|R-R'\|\). The numerical
bound on \(\|R-R'\|\), and the analogous terminal-time moduli, remain
explicitly identified as missing inputs.

The final patch correctly treats (17)–(18) as real scalar tests. For a
complex modulus threshold \(u\), testing both components at \(u/2\)
is sufficient. It changes the linear leading factor to four and the
denominator from 32 to 128. Reducing the quadratic exponent constant by
four safely covers both its quadratic and linear threshold regimes.
For complex controls, \(q=4mp\) real components at component accuracy
\(\tau/2\) give complex accuracy at most \(\tau\), and the stated
entropy becomes
\[
 q(2+8TDn^{5/8})\log(1+8Mn^{1/8}).
\]
These are the necessary numerical split factors.

The resulting verdict is limited to the collision and Hölder lemmas,
the fixed-control/finite-grid Gaussian interfaces with the displayed
interpolation obligations, the correctly normalized closing gate
conditional on its coefficient, and the exact scaled flow and linear
recurrences. A quantitative nonlinear insertion theorem, the complete
complex common-cavity estimates, and polynomial stochastic success width
are still unproved and are not claimed by the corrected candidate.
