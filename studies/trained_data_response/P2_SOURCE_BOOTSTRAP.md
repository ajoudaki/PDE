# Named-source continuation around the trained reference

Author: `/root/p2_continuation`.
Status: internally checked author proof of H through physical time 40;
not independently reviewed or promoted. The proof uses the established
fresh-query source extraction argument, not a deduction of source derivatives
from unforced value tails.

This is a mature, root-suggested alternative, not a fresh blind attempt. The
new input scope adds the complete C.2 response proof and the relevant complete
P1 response/source proofs to this author's earlier scope. The explicitly
authorized mature comparison inputs are P2_VARIATION.md,
P2_REFERENCE_COMPARISON.md, and P2_REACHED_TAILS.md. No other author report,
review, history, or study was read. P2_CONTINUATION.md and
P2_COMBINED_TAIL_CONTRACT.md remain frozen. No training, parameter sweep,
maintained-code change, or Git operation was performed.

The proof first reduces an all-nearby-law coefficient bound to a reference
coefficient bound, then proves that anchor by fresh-query forcing in physical
clock Euler programs and differentiated raw-to-clock consistency.

## 1. Contract and proof architecture

Use the exact model, common carriers, and physical normalization of the frozen
reports. Thus `u=x/sqrt(2)` lies on the unit circle, `|y|<=Y`, `Y>=1`,
`phi=tanh`, and the population initialization is `w=g`, `A=A0`, `c=0`.
The reference is

\[
 \nu_*={1\over2}\delta_{(e_1,1)}+{1\over2}\delta_{(e_2,-1)}.
\]

Write `A=A0+K` on the actual Gaussian action/adjoint carrier. Retain the
entire first row in L2, the entire HS increment K, and c in L2. Throughout
this report `T=40`; constants may depend on T and Y. An Euler program has
positive deterministic steps `h_k`, with total length at most T. Its training
law has finitely many positive weights `p_a` summing to one. Residuals in the
program are the actual population residuals. They are frozen, together with
all contractions, covariance laws, and deterministic response coefficients,
in each named-source derivative.

Let `beta_(ku,sb)` be the expected forward-slot derivative defined in §2.
When the output is a passive query u, separate its current direct slot from
all earlier training slots. Put

\[
 {\cal B}_k=\sup_{u\in S^1}\left\{
    |\beta_{ku,ku}|+\sum_{s<k,b}|\beta_{ku,sb}|\right\}.
 \tag{1}
\]

The supremum includes all passive inputs, but there is no random supremum
inside an expectation. Appending finitely many unused query instructions
defines each row; their earlier unused slots have zero response coefficient.
The deterministic functions of u obtained below extend continuously to the
whole circle.

**Reference source-coefficient statement RSC.** There are `h_*>0` and
`B_*<infinity` such that every two-atom reference **raw Euler** program with
`max h_k<=h_*` satisfies `sup_(t_k<=T) B_k<=B_*`.

**Theorem.** There are a radius `rho>0`, a
step bound `h_0>0`, and a finite constant B such that every finite training
law lambda with `W1(lambda,nu_*)<rho`, every raw Euler mesh with
`max h_k<=h_0`, and every node through T satisfy `B_k<=B`. Consequently all
their passive Q fields have a uniform Gaussian marginal tail. In particular
they satisfy H of P2_CONTINUATION.md. The frozen H reduction then supplies
the population completion/capture conclusion, and the frozen combined
report supplies the variation uniform integrability conclusion.

Section 4 first proves this conclusion assuming RSC. Section 5 controls the
raw-to-clock Euler defects, including their named-source derivatives. Section
6 proves a physical clock Euler source bound by the exact fresh-query
extraction mechanism of C.4.5.2 (R5)--(R15), and uses those defects to prove
RSC. This closes the stated theorem. The constants are finite and may be
extremely large; no useful numerical size of rho is asserted.

## 2. Exact depth-two equations and construction order

Set

\[
 m_{ka}=h_kp_a,\qquad \gamma_{ka}=-2m_{ka}r_{ka},\qquad
 a(z)=\phi'(z),\quad b(z)=\phi''(z).
\]

Use `h_(ka)=phi(w_k.u_a)`, `Z_(ka)=A_k h_(ka)`,
`H_(ka)=phi(Z_(ka))`, `delta_(ka)=c_k a(Z_(ka))`, and
`Q_(ka)=A_k^* delta_(ka)`. A subscript ku denotes an arbitrary passive
query at the current node. The exact Euler updates are

\[
 \begin{split}
 w_{k+1}&=w_k+\sum_a\gamma_{ka}a(w_k\cdot u_a)Q_{ka}u_a,\\
 c_{k+1}&=c_k+\sum_a\gamma_{ka}\phi(Z_{ka}),\\
 K_{k+1}&=K_k+\sum_a\gamma_{ka}\delta_{ka}\otimes h_{ka}.
 \end{split}                                                   \tag{2}
\]

The two Gaussian orientation families are denoted xi and zeta. Their exact
source covariances are

\[
 E\xi_{ka}\xi_{sb}=E h_{ka}h_{sb},\qquad
 E\zeta_{ka}\zeta_{sb}=E\delta_{ka}\delta_{sb}.                  \tag{3}
\]

The orientation families are independent; the lower population uses g and
zeta and the upper population uses xi. Within each family, times and inputs
need not be independent. Singular covariance is allowed. The two populations
are not paired finite-neuron coordinates.

With all deterministic objects frozen as above, define

\[
 \alpha_{ka,sb}=E\partial_{\zeta_{sb}}h_{ka}\quad(s<k),\qquad
 \beta_{ka,sb}=E\partial_{\xi_{sb}}\delta_{ka}\quad(s\le k).
 \tag{4}
\]

Specializing the complete C.2 response rule, including its signs, gives

\[
 \begin{split}
 F_{ka,sb}&=\alpha_{ka,sb}+\gamma_{sb}E(h_{ka}h_{sb}),\quad s<k,\\
 D_{ka,sb}&=\beta_{ka,sb}
              +\mathbf1_{s<k}\gamma_{sb}E(\delta_{ka}\delta_{sb}),\\
 Z_{ka}&=\xi_{ka}+\sum_{s<k,b}F_{ka,sb}\delta_{sb},\\
 Q_{ka}&=\zeta_{ka}+\sum_{s\le k,b}D_{ka,sb}h_{sb}.
 \end{split}                                                   \tag{5}
\]

Here F and D are scalar coefficient arrays, not a replacement for A or A*.
All current forward calls precede the current reverse calls. In particular

\[
 \beta_{ka,kb}=\mathbf1_{a=b}E[c_k b(Z_{ka})].                  \tag{6}
\]

For a freshly appended passive query replace the right side by its one
distinguished current slot. Current c and w use only earlier steps; current
Z has only its own direct current xi. This proves (6), including at a
singular or duplicated query. There is no sum of unweighted current
coefficients over all the other inputs.

For a fixed past backward pulse `p=(s,b)`, put
`v_(k;p)=partial_(zeta_p) w_k`. It is zero for `k<=s`. Differentiating (2)
and (5) gives exactly

\[
 \begin{split}
 v_{k+1;p}=v_{k;p}+\sum_a\gamma_{ka}u_a\bigg[
 &b(w_k\cdot u_a)Q_{ka}(u_a\cdot v_{k;p})\\
 &+a(w_k\cdot u_a)\bigg\{\mathbf1_{(k,a)=p}
       +\sum_{q\le k}D_{ka,q}a(w_{t(q)}\cdot u_q)
                         (u_q\cdot v_{t(q);p})\bigg\}\bigg],\\
 \alpha_{ku,p}&=E[a(w_k\cdot u)\,u\cdot v_{k;p}].
 \end{split}                                                   \tag{7}
\]

The notation `q<=k` sums named training slots through time k and `t(q)`
is the time index of q. The direct pulse at step s has magnitude at most
`2R m_p`; this is where both its atom mass and its step enter.

For an upper forward pulse p, define

\[
 U_{ku;p}=\partial_{\xi_p}Z_{ku},\quad
 C_{k;p}=\partial_{\xi_p}c_k,\quad
 V_{ku;p}=\partial_{\xi_p}\delta_{ku}.
\]

The exact upper equations are

\[
 \begin{split}
 C_{k;p}&=\sum_{q<k}\gamma_q a(Z_q)U_{q;p},\\
 U_{ku;p}&=\mathbf1_{(k,u)=p}+\sum_{q<k}F_{ku,q}V_{q;p},\\
 V_{ku;p}&=a(Z_{ku})C_{k;p}+c_k b(Z_{ku})U_{ku;p},\\
 \beta_{ku,p}&=EV_{ku;p}.
 \end{split}                                                   \tag{8}
\]

These are finite causal derivative equations, not a derivative of an
ambient L2 vector field. No covariance, contraction, residual, alpha, or
beta is differentiated.

Every fixed finite graph is defined before a uniform cap is sought.
Chronological construction gives a finite Gaussian innovation list;
Q is a Gaussian plus finitely many bounded first features with already
finite coefficients. Lower source derivatives at the next instruction
have a finite polynomial envelope in that finite Gaussian list, and the
bounded upper gates/readout preserve their finite moments. This inductive
argument supplies the finite coefficients in (4), even on a long graph;
it asserts no bound uniform in its number of instructions.

## 3. Consequences of a temporary backward coefficient cap

The following bounds are useful without assuming an infinite-horizon
bootstrap. They hold for every prefix on which the already constructed
backward rows have a specified cap B. At a new node the lower estimates
use only past rows; the upper estimates then construct the current row.

For all raw Euler programs through T, independently of a coefficient cap,

\[
 \|c_k\|_\infty\le C:=Y(e^{2T}-1),\qquad |r_{ka}|\le R:=Y+C.
 \tag{9}
\]

Indeed `||c_(k+1)||infty <= (1+2h_k)||c_k||infty+2h_kY`, since
`|phi|<=1` and `|f|<=||c||2<=||c||infty`; the product bound
`prod(1+2h_k)<=exp(2T)` proves (9). The raw RMS/HS/operator ball and speed
bounds in the frozen continuation report therefore apply to every prefix.

Suppose the beta row cap is B. Define

\[
 D_0=B+2RC^2T.
\]

Then (5) gives `sum_q |D_(ku,q)|<=D0`, and hence

\[
 Q_{ku}=\zeta_{ku}+J_{ku},\qquad |J_{ku}|\le D_0,
 \qquad E\zeta_{ku}^2\le C^2.                                \tag{10}
\]

The J in this display includes both response and learned contributions.
For every `lambda>=0` and every prefix,

\[
 E\exp\left(\lambda\sum_{j<k,a}h_jp_a|Q_{ja}|\right)
 \le 2\exp\{\lambda TD_0+\lambda^2T^2C^2/2\}.                 \tag{11}
\]

To verify this, use (10), the scalar bound
`E exp(lambda|G|)<=2exp(lambda² Var(G)/2)`, and Jensen with weights
`h_jp_a/sum_(i<k)h_i`. No temporal or input independence and no maximum of
a Gaussian history is used.

Put `M_(k;p)=max_(s<j<=k)|v_(j;p)|`. Since `|a|<=1`, `|b|<=2`, (7)
and discrete Gronwall give

\[
 {M_{k;p}\over m_p}
 \le2R\exp\left\{2RD_0T+
                      4R\sum_{j<k,a}h_jp_a|Q_{ja}|\right\}.
 \tag{12}
\]

The direct source appears only once, at time s; every later term is
bounded by `2Rh_j(D0+2 sum_a p_a|Q_ja|) M_(j;p)`. Iterating this
scalar inequality proves (12). Thus, for each `p>=1`,

\[
 \|M_{k;p_0}/m_{p_0}\|_{L^p}
 \le L_p(B):=4R\exp\{6RD_0T+8R^2pT^2C^2\}.                 \tag{13}
\]

Here p0 denotes the slot and p the moment order. In particular

\[
 |\alpha_{ku,sb}|\le A_B h_sp_b,\qquad
 |F_{ku,sb}|\le f_Bh_sp_b,\quad
 A_B=L_1(B),\quad f_B=A_B+2R.                                \tag{14}
\]

There is also a **past-source density bound for beta**, stronger than its
row bound for handling law transport. Put `d0=2RT+2C`. From (8), the
full derivative row sum of c is at most
`2R sum_(j<k) h_j U_j`, where
`U_j=max_(i<=j,a) sum_p |U_(ia;p)|`. Hence the row sum of V is at most
`d0 U_k`, and

\[
 U_k\le1+f_Bd_0\sum_{j<k}h_jU_j
       \le e^{f_Bd_0T}.                                    \tag{15}
\]

These inequalities hold pointwise. Consequently

\[
 \sum_{p\le k}|\beta_{ku,p}|\le d_0e^{f_Bd_0T}.              \tag{16}
\]

For completeness fix a single past forward slot `p0=(s,b)`. At time s
only `U_(sb;p0)=1` is nonzero, so only `V_(sb;p0)=c_s b(Z_sb)` is
nonzero and its magnitude is at most 2C. For k>s, (8) then yields

\[
 |C_{k;p_0}|\le2Rm_{p_0}
       +2R\sum_{s<j<k}h_j\max_a|U_{ja;p_0}|,
\]
\[
 \max_a|U_{ka;p_0}|
 \le f_Bd_0m_{p_0}
       +f_Bd_0\sum_{s<j<k}h_j\max_a|U_{ja;p_0}|.
\]

In the second inequality the c-memory double sum is bounded by T times
the single sum. Thus

\[
 |\beta_{ku,sb}|\le b_Bh_sp_b\quad(s<k),\qquad
 b_B=2R+d_0^2f_Be^{f_Bd_0T},\qquad
 |\beta_{ku,ku}|\le2C.                                     \tag{17}
\]

All constants in (10)--(17) are independent of the number of atoms,
minimum atom weight, number of steps, and covariance rank. The equations
also give, for each fixed finite p,

\[
 \|\sup_{j\le k}|w_j|\|_{L^p}+\sup_{j,a}\|Q_{ja}\|_{L^p}
       +\sup_{j,a}\|Z_{ja}\|_{L^p}\le C_{B,p}.               \tag{18}
\]

For w use its accumulated update, (10), and Minkowski with weights
`h_jp_a`. For Z use `|delta|<=C`, (14), and the forward innovation of
variance at most one. This does not claim a moment bound for a supremum
of Q or Z over all times and inputs.

The absolute estimates alone do not continue the C.2 cap to T. For example
they offer only the sufficient inequality

\[
 B\ \ge\ \Psi_T(B):=d_0\exp\{d_0T(L_1(B)+2R)\}.             \tag{19}
\]

With the overestimates (9) at T=40 the right side already grows faster
than B with a larger positive value at zero; (19) cannot select a cap.
This is a failure of this absolute estimate, not a demonstration that
the actual coefficients diverge.

## 4. Law transport and the coefficient-difference mechanism

This section proves the conditional reduction in §1. Its purpose is to
make the role of RSC precise, including the source weights and the use
of passive queries.

Take a finite optimal coupling of a finite lambda and the two-atom
reference. Split atoms according to its nonzero pairs and write it as
`p_a,(u_a,y_a),(v_a,z_a)`. Then

\[
 q=W_1(\lambda,\nu_*)=\sum_ap_ae_a,\qquad
 e_a=|u_a-v_a|+|y_a-z_a|.                                   \tag{20}
\]

Both programs now have the same source names and masses. Splitting a
reference atom does not enlarge its beta row cap: for every old slot,
its alpha, F, and beta coefficients split in proportion to the new atom
mass, while the current coefficient remains its one distinguished direct
coefficient (6). To check this claim, the lower pulse in (7) is linear in
its initial `gamma_(sb)` and identical repeated reference queries have
identical scalar values. Its normalized derivative is therefore unchanged
by splitting. Equation (5) then splits F in the same proportion. The
single upper pulse equations (8), starting with its one current impulse,
split every later coefficient in that proportion as well. Induction in
time proves the claim. Zero coupling weights are discarded.

Run both programs on the same mesh and on their joint Gaussian-source
realization. The fixed-program response theorem applied to their union
gives, for matched slots,

\[
 \|\xi_i-\bar\xi_i\|_{L^p}
      =\|N(0,1)\|_{L^p}\|h_i-\bar h_i\|_2,
\quad
 \|\zeta_i-\bar\zeta_i\|_{L^p}
      =\|N(0,1)\|_{L^p}\|\delta_i-\bar\delta_i\|_2.          \tag{21}
\]

Indeed the cross covariances are the corresponding cross contractions;
subtracting them gives the squared source difference in (21). This is a
coupling by the source covariance rule, not a Lipschitz claim for an
arbitrary matrix square root or an inverse Gram matrix.

Let eta bound the maximum raw distance between the two programs through
the prefix. The elementary forward/action subtractions on their common
ball give

\[
 |r_{ka}-\bar r_{ka}|
 +\|h_{ka}-\bar h_{ka}\|_2+\|Z_{ka}-\bar Z_{ka}\|_2
 +\|\delta_{ka}-\bar\delta_{ka}\|_2+\|Q_{ka}-\bar Q_{ka}\|_2
 \le C(\eta+e_a),
\]
\[
 |\gamma_{ka}-\bar\gamma_{ka}|
                  \le C h_kp_a(\eta+e_a).                  \tag{22}
\]

For Q subtract `A*delta` directly; c is uniformly bounded pointwise,
so the upper gate difference is L2 Lipschitz. No first-layer multiplier
occurs in Q itself. At the same passive input u replace `e_a` by zero.

Define the coefficient discrepancy at a common passive query by

\[
 E_k=\sup_u\left\{|\beta_{ku,ku}-\bar\beta_{ku,ku}|
          +\sum_{s<k,b}|\beta_{ku,sb}-\bar\beta_{ku,sb}|\right\}.
 \tag{23}
\]

The current slots are paired as distinguished query slots. Earlier
training slots use the coupling (20). Comparing the current coefficient
of a far contaminant with a reference *axis* current coefficient would
give an O(1) difference even at arbitrarily small contamination mass.
The same-passive-input convention in (23) avoids that invalid norm.

Here is the quantitative comparison needed for the bootstrap. If both
programs' previously constructed beta rows are at most B, then

\[
 E_k\le C_B\left\{(\eta+q)^{1/16}
                              +\sum_{j<k}h_jE_j\right\}.
 \tag{24}
\]

Constants can be enlarged to cover `eta+q>=1`; only its approach to zero
matters. The current bound in (24) uses only past nearby-law beta caps.
The rest of this section gives the derivative estimates proving (24).

First, within either capped program the beta row is Lipschitz in its
current passive input, with a constant depending only on B. For alpha,
differentiate only the displayed input in (7), or use the mean-value
bound
`|a(w.u)u-a(w.v)v|<=C(1+|w|)|u-v|` and (13). This gives
`|alpha_(ku,p)-alpha_(kv,p)|<=C_B m_p |u-v|`.
The same estimate holds for F by its contraction formula. For the
upper rows, all past V and the row C are identical at the two passive
queries. In (8), the past part of U differs by at most
`sum_p |F_(ku,p)-F_(kv,p)| sum_l |V_(p;l)|`, which is bounded by
`C_B|u-v|` using (15). The current a(Z), b(Z) factors differ in L2 by
`C||Z(u)-Z(v)||2<=C_B|u-v|`; tanh has bounded third derivative.
Multiplying by the pointwise derivative row bound (15) proves the
asserted beta row bound. Thus a matched active-output row costs at most
`E_k+C_B e_a`, in addition to the learned contraction discrepancy in
(22).

Second, subtraction of (7) has a causal linear propagation part using
the nearby-law coefficients and a source part. The propagation coefficient
for the maximum norm of a pulse difference is bounded by

\[
 2Rh_k\left(D_0+2\sum_ap_a|Q_{ka}|\right).                 \tag{25}
\]

The source part consists exactly of the differences of gamma, the two
input vectors, the gates a and b, Q, and D, each multiplied by an
unchanged reference pulse. In particular there is no derivative of D in
this subtraction. The D difference is

\[
 \Delta D_{i,p}=\Delta\beta_{i,p}
 +\mathbf1_{t(p)<t(i)}\left[
  \Delta\gamma_p E(\bar\delta_i\bar\delta_p)
       +\gamma_p\Delta E(\delta_i\delta_p)\right],          \tag{26}
\]

where unbarred gamma is used in the second term. This also verifies that
learned-memory errors retain m_p.

All unchanged normalized pulses have every fixed finite moment by (13).
Gate and field differences needed in the source part have an L12 bound
`C_B(eta+e_a)^(1/16)`. For bounded gates interpolate the L2 bound (22)
with their pointwise bound. For w or Q interpolate their L2 difference
with the uniform L24 bounds (18); interpolation gives exponent 1/11,
which implies the weaker displayed exponent on a bounded distance range.
For the input factors themselves use `|u_a-v_a|<=e_a`.
Products of up to three factors are bounded in L4 by Hölder with L12
norms. The random integrating factor obtained from (25) has every fixed
moment by (11); Cauchy--Schwarz bounds its product with each forcing
term. Minkowski sums the time/atom masses. Discrete Gronwall therefore
gives, for every past pulse p=(s,b),

\[
 {\|\max_{j\le k}|v_{j;p}-\bar v_{j;p}|\|_2\over m_p}
 \le C_B\left\{(\eta+e_b)^{1/16}+q^{1/16}
                              +\sum_{j<k}h_jE_j\right\}.   \tag{27}
\]

One way to verify the averaging in this estimate is to retain each
`e_a^(1/16)` until the last step and use
`sum_a p_a e_a^(1/16)<=q^(1/16)`. The direct pulse uses (22) and has
the same factor m_p; dividing by it does not leave `1/p_b`.
In the D term, its row variation multiplies the reference maximum pulse
norm from (13); its active-output discrepancy is bounded just above.
There is also a term in which D is unchanged and a *past source's* gate
or input changes. This is where (17) is essential: its old-source
coefficient satisfies `|D_(ka,sb)|<=C_B h_sp_b`, so

\[
 \sum_{s<k,b}|D_{ka,sb}|e_b^{1/16}
             \le C_BT\sum_bp_be_b^{1/16}\le C_BTq^{1/16}.
 \tag{27a}
\]

The one current coefficient costs `C_B e_a^(1/16)` and is averaged
with the outside update weight p_a. A row bound without the past-source
density bound would not justify this step.
These account for every term from the two sums in (7). Importantly no
maximum of the `e_a` and no unweighted sum over source indices is taken.

By the second line of (7), (27), and Hölder for the difference of its
outside gate, at a common passive input

\[
 \sum_{p<k}|\Delta\alpha_{ku,p}|
 \le C_B\left\{(\eta+q)^{1/16}
                              +\sum_{j<k}h_jE_j\right\}.   \tag{28}
\]

Here `sum_(p<k) m_p<=T`; the contribution depending on the source
`e_b` averages as in (27). The identical estimate holds for the F-row
difference by (5) and (22). For a matched active output add
`C_B e_a` using the passive-input estimate. Entrywise versions keep the
factor m_p and its `e_b` term.

Finally, the exact upper differences are

\[
 \begin{split}
 \Delta U_{i;p}
    &=\sum_{q<i}\Delta F_{i,q}\bar V_{q;p}
                       +\sum_{q<i}F_{i,q}\Delta V_{q;p},\\
 \Delta C_{k;p}
    &=\sum_{q<k}\{\Delta\gamma_q a(\bar Z_q)\bar U_{q;p}
             +\gamma_q\Delta a(Z_q)\bar U_{q;p}
             +\gamma_q a(Z_q)\Delta U_{q;p}\},\\
 \Delta V_{i;p}
    &=a(Z_i)\Delta C_{k;p}+\Delta a(Z_i)\bar C_{k;p}
          +c_kb(Z_i)\Delta U_{i;p}
          +\{\Delta c_k b(\bar Z_i)+c_k\Delta b(Z_i)\}
                                                        \bar U_{i;p}.
 \end{split}                                               \tag{29}
\]

The direct U impulses cancel after pairing the distinguished current
slots. To keep output errors weighted, set

\[
 G_k=(\eta+q)^{1/16}+\sum_{j<k}h_jE_j,\qquad
 L_k=\sum_ap_a\left\|\sum_p|\Delta V_{ka;p}|\right\|_2.
\]

Every barred upper derivative row is bounded pointwise by (15).
The F propagation coefficients have density `f_Bh_jp_a`, and gamma
retains its original mass. Summing (29) over source indices, taking L2,
then averaging its active output index gives

\[
 L_k\le C_BG_k+C_B\sum_{j<k}h_jL_j.                         \tag{29a}
\]

In this estimate the F-row forcing at a matched active output is at most
`C_B(G_k+e_a)` by (28); the field factors at that output cost
`C_B(eta+e_a)` by (22). Both are averaged with p_a. In the C-row,
which does not depend on the output query, the same factors are already
multiplied by `h_jp_a`. These are all appearances of an output transport
cost in (29). Since G_k is nondecreasing, discrete Gronwall yields
`L_k<=C_B G_k` after increasing C_B. For a common passive output there
is no e_a term, and the same equations give

\[
 \left\|\sum_p|\Delta V_{ku;p}|\right\|_2
                 \le C_BG_k+C_B\sum_{j<k}h_jL_j\le C_BG_k.
 \tag{29b}
\]

Taking expected absolute values proves (24). The current diagonal
contributes at most `C eta` directly from (6). There is no current
unknown E_k on the right: (28) uses only earlier lower updates, and all
upper memory terms in (29) are strictly earlier. No supremum over the
matched active-output costs e_a was used.

For clarity, the raw discrepancy eta used above is available without
RSC. The common raw ball, the HS transport estimate of the frozen
comparison report, and the established Gaussian tails of the actual
reference flow give, for every finite raw Euler program lambda,

\[
 \sup_{k:t_k\le T}d_{\rm raw,1}(\theta_{\lambda,k},\theta_*(t_k))
       \le \omega_T(q+h_{\max}),\qquad \omega_T(s)\to0.     \tag{30}
\]

To see the mesh term, interpolate the Euler path affinely; its speed is
uniformly bounded by the crude raw ball. Apply the transport estimate
with the actual reference as its tail-bearing endpoint. The distance
from the interpolated Euler state to its left endpoint is at most
`V_T h_max`, so the cutoff inequality acquires
`C(1+R_cut)h_max`. Integrating gives
`C exp(CR_cut){(1+R_cut)(q+h_max)+exp(-cR_cut²)}`. Choosing the cutoff
as in the reference comparison proves (30). This is a comparison to one
existing flow, not a construction of a changed-law flow.
Applying (30) to lambda and to the reference raw Euler program gives a
valid eta tending to zero with `q+h_max` in (24).

Assume now RSC. Its reference Euler Q tails are Gaussian by (10).
For the two raw programs on the **same** mesh, the transport estimate
therefore gives, at a fixed cutoff Rcut, the recurrence

\[
 d_{k+1}\le[1+Ch_k(1+R_{\rm cut})]d_k
          +Ch_k\{(1+R_{\rm cut})q+e^{-cR_{\rm cut}^2}\}.
\]

Both start at the same state. Iteration and cutoff choice give

\[
 \sup_k d_k\le\Phi_{B_*}(q),\qquad
 \Phi_{B_*}(q)\longrightarrow0\quad(q\downarrow0),          \tag{30a}
\]

uniformly over admitted meshes; there is no mesh defect in this
comparison. One can take `Phi(q)=Cq exp(C sqrt(log(e/q)))` for small q
after enlarging constants. The crude ball for the nearby program
suffices; only the reference endpoint of the transport estimate
requires tails.

Set `B=B_*+1` and use its invariant duplication property.
At the first potential failed row, all prior nearby-law rows are at
most B. Estimates (10)--(29) apply in their causal order. Discrete
Gronwall in (24) gives

\[
 E_k\le C_B e^{C_BT}
                 \{\Phi_{B_*}(q)+q\}^{1/16}.                \tag{31}
\]

Choose positive rho small enough that the right side is at most 1/2
whenever `q<rho`, and put `h0=h_*`.
The current row is then at most `B_*+1/2<B`, contradicting first failure.
The zero-readout initialization has beta=0, so induction starts. This
proves the claimed uniform cap. Formula (10) converts it to a uniform
Gaussian tail for every passive Q; (9) controls c. H follows with slack
from the Gaussian tail. No convergence of positive-radius laws has been
inferred merely from their proximity to the reference.

More explicitly, once the cap is fixed, `Q=G+J`, `Var(G)<=C²`,
`|J|<=D0`. For `Rcut>=2D0`, the event `|Q|>Rcut` implies
`|G|>Rcut/2`. Integrating the scalar Gaussian tail and absorbing its
polynomial prefactor gives `tau_Rcut(Q)<=M exp(-a Rcut²)` with finite
positive a,M depending only on the fixed caps. Enlarge M to cover the
remaining `Rcut>=1` and the bounded readout. Averaging over any training
law proves H, with the same constants on each smaller radius. A state
on an affine Euler segment is obtained by appending one shorter final
step; the same bound applies to its recomputed fields. This is a
marginal-in-time statement, not an exponential bound for a path maximum.

## 5. Raw-to-clock mesh errors, including named derivatives

The reference clock conversion is a real simplification, but it does not
by itself prove RSC. This section checks that its Euler defect is not a
separate unsummable obstruction once a temporary cap is available.

Let

\[
 {\cal F}(w)=w/2+\sinh(2w)/4,\quad {\cal F}'(w)=1/a(w),
\quad R_h(w,b_0)={\cal F}(w+hb_0a(w))-{\cal F}(w)-hb_0.
\]

Here b0 is a scalar velocity coefficient, not the function b=phi''.
Put `Delta=hb0 a(w)`. Taylor's integral identity gives

\[
 R_h=h^2b_0^2a(w)^2
                \int_0^1(1-s){\cal F}''(w+s\Delta)\,ds.
 \tag{32}
\]

The elementary hyperbolic identities imply

\[
 a(w)^2|{\cal F}''(w+z)|\le2e^{2|z|},\qquad
 a(w)^2|{\cal F}'''(w+z)|\le4e^{2|z|},\qquad |a'|\le2a.
\]

For example `|sinh(2(w+z))|<=e^(2|z|)cosh(2w)` and
`a(w)^2 cosh(2w)<=2`; the bound for the third derivative follows in
the same way. Differentiating the explicit integral (32), rather than
separately estimating the large terms before cancellation, yields

\[
 |R_h|\le Ch^2 b_0^2e^{2h|b_0|},
\]
\[
 |\partial_wR_h|\le Ch^2b_0^2(1+h|b_0|)e^{2h|b_0|},\qquad
 |\partial_{b_0}R_h|\le Ch^2|b_0|(1+h|b_0|)e^{2h|b_0|}.
 \tag{33}
\]

Every named derivative consequently obeys

\[
 |\partial_p R_h|
 \le Ch^2e^{2h|b_0|}(1+h|b_0|)
                \{b_0^2|\partial_p w|+|b_0||\partial_p b_0|\}.
 \tag{34}
\]

On the reference, including any split representation, the row-coordinate
update has precisely this form with

\[
 b_{0,a,k}=-2\sum_{j:v_j=e_a}p_jr_{kj}Q_{kj}.
 \tag{35}
\]

Under the temporary cap its scalar marginals have uniformly bounded
Gaussian norms, by (10) and the total atom mass. Formula (11) or the
scalar Gaussian exponential moment controls the factor in (33)--(34).
Therefore `sum_k ||R_(h_k)||p<=C_(B,p)h_max` for every fixed finite p.

For a backward source p0=(s,j), at the direct injection step
`|partial_(p0)b0|<=2Rp_j` and `partial_(p0)w_s=0`.
Dividing that step's estimate (34) by `m_(p0)=h_sp_j` costs at most
`C_(B,p)h_s`. At every later step, (7), (13), and the D-row cap give

\[
 \|\partial_{p_0}w_k/m_{p_0}\|_{L^p}
 +\|\partial_{p_0}b_{0,a,k}/m_{p_0}\|_{L^p}\le C_{B,p}.
\]

Using Hölder in (34) and `sum h_k²<=T h_max` now proves

\[
 {1\over m_{p_0}}\sum_{k\ge s}
               \|\partial_{p_0}R_{h_k}\|_{L^p}
                                  \le C_{B,p}h_{\max}.     \tag{36}
\]

This proves summability of the named backward-pulse clock defect with
its correct mass normalization. A local lower-population function is
independent of the upper xi slots when deterministic coefficients are
frozen; there is no additional xi derivative of its clock defect.
The c/K updates are the same in raw and clock formulations.

## 6. The physical reference source anchor and its transfer

### 6.1. Uniform reference clock Euler coefficients by fresh queries

Use the two reference clocks `X_a=F(w_a)-F(g_a)` and the scalar solution
`w_a=J(X_a,g_a)` of `J_X=sech²J`, `J(0,g)=g`. Thus
`|J_X|<=1`. Its active first features have `|H_X|=sech⁴J<=1`.
The physical reference clock equations are

\[
 \dot X_a=-r_aQ_a,\qquad
 \dot K=-\sum_{a=1}^2r_a\delta_a\otimes h_a,\qquad
 \dot c=-\sum_{a=1}^2r_aH_a.                                \tag{37}
\]

Their raw fields are the established reference flow. On the common
carrier these equations are Lipschitz on the bounded sets used below,
by the explicit subtractions that follow; Euler convergence here needs
no raw first-gate estimate.

For the auxiliary source extraction use finite initialized matrices
with `||A0||op<=10` and **zero readout**. This is an auxiliary fixed
program used to identify the zero-readout population coefficients; it
does not alter the finite random readout in the frozen finite-GF
capture theorem. Use normalized finite L2 norms and unnormalized HS
increment norm. By (9) and bounded activations, at all nodes,

\[
 \|c_k\|_\infty\le C,\quad |r_{ka}|\le R,\quad
 \|K_k\|_{HS}\le2TRC,\quad \|A_k\|_{op}\le M:=10+2TRC.
 \tag{38}
\]

These bounds also hold if a fresh root is added to one forward or
reverse query and all descendants, including residuals, are recomputed.
Forward tanh and its gate remain bounded, so every subsequent c and K
increment obeys the same estimate. Reverse forcing changes only the
clock increment directly. Thus there is no assumption that a forced
program retains a gradient-flow energy identity.

For two unforced subsequent clock states on this ball set
`x=sum_a||Delta X_a||2`, `k=||Delta K||HS`, `z=||Delta c||2`,
and `d=x+k+z`. The same-root scalar bound for J gives

\[
 \begin{split}
 \sum_a\|\Delta h_a\|_2&\le x,\qquad
 V:=\sum_a\|\Delta Z_a\|_2\le Mx+2k,\\
 D:=\sum_a\|\Delta\delta_a\|_2&\le2z+2CV,\qquad
 P:=\sum_a\|\Delta Q_a\|_2\le MD+2Ck,\\
 S:=\sum_a|\Delta r_a|&\le2z+CV.
 \end{split}                                               \tag{39}
\]

The three velocity differences in (37) are at most

\[
 MC S+RP,\qquad CS+R(D+Cx),\qquad S+RV.                    \tag{40}
\]

For example subtract `r delta tensor h` into its residual, upper
field, and lower feature differences; the rank norm is the product of
its L2 factors. Equations (39)--(40) give a bound `L d` with the fixed
overestimate

\[
 L=100(1+M+C+R)^4,
 \qquad E=\exp(LT).                                        \tag{41}
\]

Hence any post-pulse Euler difference is amplified by at most E,
independently of width, step count, and step sizes. Splitting an atom
retains these equations after summing its identical descendants.

Insert `epsilon e` into the complete reverse answer at slot (s,b).
Its only immediate state change is in the clock corresponding to
`v_b=e_a`, with norm at most

\[
 2R h_sp_b|\epsilon|\|e\|_2.                               \tag{42}
\]

For a passive first feature
`h(u)=phi(u_1J(X_1,g_1)+u_2J(X_2,g_2))`, the difference is at most x.
The subsequent passive feature difference is therefore bounded by
`2R E h_sp_b |epsilon| ||e||2`.

Instead insert the root into one complete forward answer `Z_(sb)`.
At that node its activation, delta, residual, and reverse answer change
by at most, respectively,

\[
 |\epsilon|\|e\|_2,\quad 2C|\epsilon|\|e\|_2,\quad
 C|\epsilon|\|e\|_2,\quad 2MC|\epsilon|\|e\|_2.
\]

Use the old Q and the bounded new residual when subtracting the clock
update. The three immediate state increments have total norm at most
`P0 h_sp_b |epsilon| ||e||2`, where

\[
 P_0=2\{MC^2+2RMC+C^2+2RC+C+R\}.                          \tag{43}
\]

The terms arise from `Delta(rQ)`, `Delta(r delta tensor h)`, and
`Delta(rH)`, respectively. A passive later delta satisfies

\[
 \|\Delta\delta(u)\|_2\le z+2C(Mx+k)\le K_0d,
 \qquad K_0=1+2C(M+1).                                    \tag{44}
\]

Thus its post-pulse change is at most
`P0 K0 E h_sp_b |epsilon| ||e||2`.

Extract the named coefficients by the full mechanism of C.4.5.2
(R5)--(R15). Here are the hypotheses and the order of limits needed
for this application. At each fixed graph clip the Gaussian first
roots smoothly. The passive feature's derivatives with respect to X
are bounded uniformly in the root clipping level; its root
derivatives are bounded at each fixed level. A readout clip equal to
the identity on a neighborhood of `[-C,C]` is inactive. Thus the
fixed-program theorem and its complete source extension apply to
forced and unforced graphs, including singular covariance and
variance-zero slots. At a fixed graph all source derivatives have a
finite deterministic bound independent of root clipping: the clock
derivatives are bounded, the readout is bounded, and every matrix
answer is a source plus a finite sum with fixed coefficients.
Chronological convergence and this derivative bound remove root
clipping and make all coefficients continuous as epsilon tends to
zero, exactly as proved in C.4.5.2 §2. No mesh-uniform source cap was
used in this fixed-graph step.

Fix the mesh and nonzero epsilon and first let width tend to infinity.
The initialization operator event and `||e_n||2/sqrt(n)->1` have
probability tending to one. The joint value theorem transfers
(42)--(44) and their pairing with the fresh Gaussian root. In the
source coordinate expression that root enters only in the specified
slot as `slot+epsilon e`. The selected residuals and covariance laws
may depend on epsilon but are deterministic, and all Gaussian source
groups are independent of this local new root. Conditional
one-dimensional Gaussian integration by parts therefore gives

\[
 E[eV^\epsilon]=\epsilon E[\partial_{\rm slot}V^\epsilon].
 \tag{45}
\]

The unforced expression is independent of e. Cauchy--Schwarz in the
joint limit, division by `|epsilon|`, then the fixed-graph
zero-forcing continuity just proved yield

\[
 |\alpha^{\rm cl}_{ku,sb}|\le2REh_sp_b,
 \qquad |\beta^{\rm cl}_{ku,sb}|\le P_0K_0Eh_sp_b\quad(s<k),
 \qquad |\beta^{\rm cl}_{ku,ku}|\le2C.                     \tag{46}
\]

The argument works for each passive u with the same constants.
Consequently every reference physical clock Euler program through T
has the cap

\[
 B_{\rm cl}=2C+TP_0K_0E.                                   \tag{47}
\]

This proves a bound for the specified named coefficients. It does
not infer a derivative transverse to a singular source support from
the unforced value law. The fresh root and the width-first,
forcing-second order in (45) are essential.

### 6.2. Transfer from clock Euler to raw reference Euler

Compare the reference raw and clock Euler programs on the same mesh
and common Gaussian source carrier. Write
`X^r_a=F(w^r_a)-F(g_a)` for the transformed raw program and `X^c`
for clock Euler. The raw program satisfies the exact clock update
with the extra vector of defects (32). Its lower first-feature
expression is the same function of X and g as in the clock program.

Define E_k by (23) for this raw/clock pair, with no change of data
law, and assume a temporary cap B on all preceding raw beta rows.
Let eta_h bound the raw discrepancy of their fields. There is an
eta_h tending to zero with h_max independently of that cap: (30)
compares raw Euler with the actual reference, while (39)--(41), the
bounded clock speed, and the integrated Euler error compare clock
Euler with the same reference in clock/HS/L2 norm. The scalar bound
`|J_X|<=1` converts the latter distance to raw distance. In particular
all the field differences in (22) are `O(eta_h)`.

For a backward pulse p0=(s,b), put
`chi^r_(k;p0)=partial_(zeta_p0) X^r_k` and define chi^c similarly.
For a lower first feature let `J_q^r` and `J_q^c` denote its two
clock derivatives. Each has norm at most two, and their difference
in L2 is at most `C eta_h`, since each is a product of bounded tanh
gates with bounded derivatives. At reference active slots one can
use the sharper bound one. Differentiating the two clock recursions
gives the exact pair

\[
 \chi^r_{k+1;p_0}=\chi^r_{k;p_0}
   +\sum_a\gamma^r_{ka}v_a\left\{\mathbf1_{(k,a)=p_0}
             +\sum_{q\le k}D^r_{ka,q}J_q^r\chi^r_{t(q);p_0}\right\}
   +\partial_{p_0}R_k,
\]
\[
 \chi^c_{k+1;p_0}=\chi^c_{k;p_0}
   +\sum_a\gamma^c_{ka}v_a\left\{\mathbf1_{(k,a)=p_0}
             +\sum_{q\le k}D^c_{ka,q}J_q^c\chi^c_{t(q);p_0}\right\}.
 \tag{48}
\]

Here v_a is the reference axis of that atom, and the lower feature
derivative is a row vector applied to chi. The clock reference cap
(47) bounds its D rows by `Dcl=Bcl+2RC²T`. Since the clock gates
are bounded, its pulses satisfy the **pointwise** bound

\[
 \max_{j\le k}|\chi^c_{j;p_0}|/m_{p_0}
                        \le2R\exp(4RD_{\rm cl}T).         \tag{49}
\]

Subtract (48). Its raw propagation coefficients have a deterministic
bound depending only on B and (9); there is no random Q multiplier.
Differences of gamma and the clock gates cost `C eta_h`, multiplied
by the bounded normalized reference pulse (49). The D-row difference
is at most `E_j+C eta_h` by (26). Finally (36) bounds the sum of
the normalized defect derivatives in L2 by `C_B h_max`. Discrete
Gronwall gives

\[
 {\|\max_{j\le k}|\chi^r_{j;p_0}-\chi^c_{j;p_0}|\|_2\over m_{p_0}}
    \le C_B\left\{\eta_h+h_{\max}
                                  +\sum_{j<k}h_jE_j\right\}.
 \tag{50}
\]

The maximum on the left is controlled by the sum of the forcing
norms and a deterministic integrating factor. It does not require
an L2 bound on a supremum of the raw field discrepancy.

Take expected first-feature derivatives to obtain the same bound for
the alpha row difference, after summing its source masses. For a
passive output its derivative outside chi differs in L2 by
`C eta_h` and is bounded, so the statement remains uniform in u.
The upper source equations (8) are identical in the two schemes;
subtracting them as in (29), using the source density bounds and
discrete Gronwall, proves

\[
 E_k\le C_B\left\{\eta_h+h_{\max}
                                  +\sum_{j<k}h_jE_j\right\}.
 \tag{51}
\]

Set `B=Bcl+1`. At any first potentially failed raw row, all previous
rows obey this cap. The defect estimate (36) uses only those previous
raw Q fields. The current alpha then obeys (50), and the current
beta obeys (51), whose right side has no current beta. Gronwall
yields `E_k<=C_B exp(C_BT)(eta_h+h_max)`. Choose h_* positive and
small enough that this is at most 1/2 whenever `h_max<=h_*`.
Then the current raw row is at most `Bcl+1/2<B`, so induction cannot
fail. Both zero-readout initial programs have beta=0. This proves RSC
with `B_*=Bcl+1`. Section 4 now proves the all-nearby-law cap and H.

The two bootstraps are separate: the first uses one fixed, independently
proved clock anchor to control reference raw Euler; the second uses
that raw anchor and weighted law transport to control all nearby finite
laws. Neither bootstrap takes a supremum of far-atom transport costs
or assumes the tails of the not-yet-controlled current query.

## 7. Claim checks and provenance

The following claims are established internally in this report:

1. Equations (2)--(8) are the exact depth-two specialization of the
   complete established source rule, with the physical loss factor two.
2. Under a temporary past beta cap, all individual past alpha and beta
   coefficients retain their original step/atom mass. There are no
   constants depending on atom count or inverse atom mass.
3. The weighted coefficient comparison (24), together with the already
   available raw reference comparison, reduces the all-law cap to RSC.
   It does not assume a raw Frechet derivative or treat fixed positive
   reference proximity as a Cauchy condition.
4. Raw-to-clock value and named-pulse defects are O(max step) in each
   required fixed moment under that temporary cap.
5. Fresh reverse and forward query forcing, followed by the exact
   width-first/forcing-second coefficient extraction, gives the physical
   reference clock Euler cap (47) without assuming a source cap.
6. The differentiated consistency bootstrap (48)--(51) proves RSC;
   the weighted law bootstrap (24), (30a)--(31) then proves H through T.

No conclusion is asserted for an arbitrary
supremum inside an exponential moment, growing-depth programs, a
covariance inverse, or useful numerical constants. The unchanged frozen
continuation and combined-tail reports provide the remaining implications
from H to the full raw-state population theorem, finite-GF capture with
arbitrary simultaneous limits, and the response remainder. This report
supplies their previously open hypothesis at the level of an internally
checked author argument; independent complete review is still required.

Scientific source coverage is the previous complete authorized coverage
recorded in P2_CONTINUATION.md and P2_COMBINED_TAIL_CONTRACT.md, with
the complete C.2 proof additionally used for (3)--(8) and (11)--(16).
The full relevant P1 source/clock/capture proofs were read. Section 6
uses the complete C.4.5.2 (R5)--(R15) fresh-query argument, with the
physical-time bounds and changed residuals checked explicitly here. No
external theorem or web source was added. Hashes of scientific inputs
and shared instructions at this author's reading snapshot follow.

| Input | SHA-256 |
|---|---|
| AGENTS.md | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| RESEARCH_WORKFLOW.md | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
| docs/NOTATION.md | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| docs/global_nonlinear.md | `3f32122dea7915e25e4abc7abe9d74017d535badfa5abbe1939e84fe2b100bdf` |
| Complete C.2 lines 2924--3440 | `cf223a3eed88b3755d0379948316534fb44febc9fa1d6f0bb5d282ff8be4ac94` |
| C.4 introduction through C.4.6 | `135e9a5f7e949ae93c3eb6191f34e98e8b7c766d11483fb493833154b1c59d19` |
| P1_SECTION.md | `33c819282d83f7f4704cbd3a90e87b445d17ce161cc922c1ad786b5eb0d9de38` |
| P1_DEPENDENCIES.md | `ca696bc4ed14ea337028eb1e6ef9c7f729ed2a0153bc210de8e16dea18f5ee79` |
| P1_MANIFEST.json | `f9f3ac7dd834429f2afd1b2d819e20cf04da37446311405943332300ca4fa53d` |
| P2_CONTINUATION.md | `fe59ffe02281be549d6d7815d9c3b58bfe9b51545236cbffb9899339838669d2` |
| P2_COMBINED_TAIL_CONTRACT.md | `818d2885fa706d6ceae1101afc3cee2e91afea27ec49c431a4d87f6321e3f994` |
| P2_VARIATION.md | `ef28df6745758adc1c587a4d73442c3a49db575026ac2bee86708a24de44c5fd` |
| P2_REFERENCE_COMPARISON.md | `869415030167bf422c5a0a5fad05cd35fafc5bbe5221e40968e8ae4db4cafba3` |
| P2_REACHED_TAILS.md | `837535f363d8140516ed993698f0e48d183dc029fe66cffc1277aff79e328716` |

Scratch directory:
`data/generated/trained_data_response/p2_20260911_02/source_bootstrap/`.
