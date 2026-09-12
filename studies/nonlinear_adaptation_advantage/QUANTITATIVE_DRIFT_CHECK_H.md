# Internal quantitative-drift check H

Reviewer: scoped harmonic-route agent, 2026-09-12.

**Scoped verdict: PASS. No corrective mathematical finding.** Q1–Q14 follow
under the stated full-history source cap and established reached-curve bounds.
The candidate supplies a time-Lipschitz modulus for the reached kernel
derivative in terms of source/reference constants. It does not supply the
uniform favorable curvature sign, beneficial component sign, numerical
conditioning enclosure, or an unconditional E₀ advantage.

This is an internal check, not independent promotion review. The reviewer
previously froze a separate audit of the prompt-supplied source-moment lemma
before reading this complete candidate. No geometry current check or energy
current reduction was read. The candidate and established inputs were
preserved; no experiment or new sign search was performed.

## 1. Frozen inputs and actual reading

QUANTITATIVE_CURVATURE_DRIFT.md was read completely, lines 1–293, in an
untruncated output. Its assigned SHA-256 was verified:

5bfd6b4c1683d172e3c7a543e8b9e7faa17b2b14f0299ea4242a3776cbcee7d5

The source lemma had independently been audited and frozen in
SOURCE_MOMENT_AUDIT_H.md at:

b34420220022c7c30cd8a4b75d3c3a9c40702987df2328e8467ddb4c92c4cdbd

The fully read frozen geometry report, which supplies the scalar Hessian and
finite remainder identities checked here, is at:

e452735f683a6f8c3e4e895949dbd8aa912f470bbdeb475bf676bce4a10b9c04

Previously read permitted established inputs remain:

| Input | SHA-256 |
|---|---|
| docs/global_nonlinear.md | 5c7f4cd85eebe73f497ff91cca4f3c525f158727c28b8a187a09add94e756483 |
| docs/special_data_limits.md | 5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489 |
| docs/NOTATION.md | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |
| RESEARCH_CONTRACT.md | 0bbd681da93a44574fbe30d9ee7fd5a984105d363c473c7756f31964c2896c0f |
| RESEARCH_WORKFLOW.md | 8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12 |

Their actual scientific coverage is unchanged from INTERNAL_CROSSCHECK_H.md:
complete notation; global_nonlinear A.1–A.4, C.4.5.1 §§1–3 and §5,
C.4.5.2 §§1–4, C.4.9 model/source unit A and supplement/unit B through B.4,
and C.4.10 completely; special_data_limits III.F completely.
The source audit separately reread CT12–CT17, CT26–CT31, and the
formal-source and singular-query arguments. The required skills and process
references were already read. No other source/history was retrieved.

## 2. Q1–Q4: source moment and its scope

The candidate incorporates the needed clarification that the response cap
holds on every historical and current backward row, not only an endpoint row.
The source calculation therefore has the CT29 pulse estimate throughout its
memory. Its current queries are appended before the new forward probe, with
no intervening state updates and no merging of singular formal names.

The independently checked direct, two-gate and memory bounds are respectively
$M$, $4MHE_2q_2$, and $MDHE_1$. The moment substitution
$E_p=2^{1/p}\exp(3DH+2pH^4)$ follows from CT28. The new input has
$\|F_u(b)\|_2\le Mq_2$ and all old/current reverse inputs are pointwise
bounded by $H$. Hence the forward Gaussian fourth moment and the response
sum give Q4; the historical and current rank bounds then give Q2.

The choice $q_2=q_4$ is legitimate: NSC17 supplies the uniform fourth moment
from the same source tails, and L⁴ dominates L² on the probability spaces.
The historical queries also have those source bounds because every prefix
belongs to the same full controlled history.

Passage uses strong L² convergence and Fatou, not convergence of individual
derivative histories or an L⁴ action norm. The extension to L² coefficient
functions is valid by finite/continuous approximation and Cauchy–Schwarz
on absolute coefficient mass. If approximating coefficient norms have a
vanishing overshoot, passing the corresponding mass constants to their
limit gives the same final estimate. No additional limiting hypothesis is
needed. The conclusion remains restricted to generated gradient-combination
directions.

## 3. Q5–Q6: force and directional-field bounds

For $\|v\|_p\le1$, put $U_t(v)=\int v g_t p\,d\rho$ and
$B_t=G_tM_t^{-1}$. Then

\[
\|U_t(v)\|\le L,\qquad
\|\beta_t(v)\|_1
\le\sqrt2\|B_t\|\,\|U_t(v)\|
\le2L/\sqrt k.
\]

Thus the projected force has coefficient mass at most $m_d$. This proves
the claimed readout supremum and row fourth-moment bounds. The raw norm is
at most $L$ because the projector contracts; its time difference is at most
$Jh$ from the integrated NSC28/projector derivative estimate.

The upper-directional L² estimate follows directly:

\[
\|x_KH^1+A\phi'(w\cdot u)(x_w\cdot u)\|_2
\le(1+a_b)L=Z2f.
\]

The L⁴ version is Q2 with mass $m_d$. Each state velocity constant in Q5
matches NSC25–NSC28. In particular $\|c_t-c_s\|_\infty\le V_c h$
follows by integrating the pointwise bounded velocity, without claiming
supremum-norm convergence from raw convergence alone.

For the first directional lower feature, subtract the direction and gate:

\[
\|F_t(x_t)-F_s(x_s)\|_2
\le Jh+
2\|w_t-w_s\|_4\|x_{s,w}\|_4
\le(J+2Vw4\,W4f)h.
\]

For the upper directional field, subtraction of
$x_KH^1+AF$ costs in order
$J$, $L\,Vw2$, $VK\,L$, and $a_b\,VF$ times $h$.
This verifies the stated $VV$. No L⁴ time difference of $x_w$ is used;
its raw L² difference and its separate uniform L⁴ bound are sufficient.

## 4. Q7–Q9: every scalar-Hessian product

Q7 is the correct polarization of G12. The last term uses
$A^*\delta=Q$; the middle two terms come from differentiating the middle
action and lower activation once each. The initialized action is retained
with its actual adjoint.

For unit force arguments the four groups in Q7 have absolute-value bounds

\[
2L\,Z2f,\qquad 2H\,Z2f^2,\qquad
2c_bL^2,\qquad 2q_2W4f^2,
\]

which sum to $C_H$.

Here is the full time-difference check. All listed costs multiply $h$.

| Hessian group | Changing factor and valid norm pairing | Total contribution to $L_H$ |
|---|---|---|
| Two readout/feature terms | Readout difference in L² against $V$ in L²; gate difference via $\Delta Z$ in L², old direction readout in L∞ and $V$ in L²; $V$ difference in L² against readout in L² | $2[J\,Z2f+2m_d\,Vz\,Z2f+L\,VV]$ |
| Upper curvature | $\Delta c$ in L∞ and two L² directional fields; changed gate via $\Delta Z$ in L² against the product of two L⁴ directional fields; each changing directional field in L² against the other in L² | $2Vc\,Z2f^2+4H\,Vz\,Z4f^2+4H\,VV\,Z2f$ |
| Two middle mixed terms | $\Delta\delta$ in L² against an HS-action/L² product; direction action difference in HS; lower directional feature difference in L² | $2[Vdelta\,L^2+c_bJL+c_bL\,VF]$ |
| Row curvature | $\Delta Q$ in L² against two L⁴ row directions; gate difference using four L⁴ factors; each direction difference in L² against $Q$ and the other direction in L⁴ | $2VQ\,W4f^2+4Vw4\,q_4W4f^2+4q_4J\,W4f$ |

For the upper changed gate specifically,

\[
4H\|\Delta Z^2\|_2\|V(x_s)V(y_s)\|_2
\le4H\,Vz\,Z4f^2h.
\]

This is exactly where the newly proved generated-input fourth moment is
needed. The row changed gate uses Hölder exponents $(4,4,4,4)$ on
$\Delta w,Q,x_w,y_w$. A changing row direction uses exponents $(2,4,4)$.
These products are scalar expectations, so their exponent sums equal one.
No backward derivative is required in L⁴.

The uniform bounds $|\phi''|\le2$, $|\phi'''|\le4$ are conservative and
valid for tanh. The table accounts for every factor in Q7 and reproduces
Q8 without an omitted cross term: exact one-factor-at-a-time subtraction
uses current and old factors whose same uniform bounds apply. Homogeneity
then proves Q9 for all L² coefficient functions, including zero arguments.

## 5. Q10–Q12: changing projector coefficients and residual

The coefficient formula can be written
$\beta_t(v)=B_t^*U_t(v)$. NSC28 gives
$\|B_t-B_s\|\le A_sT_Bh$, while
$\|U_t(v)-U_s(v)\|\le A_sT_g h\|v\|_p$.
Together with $\|B_s\|\le\sqrt{2/k}$ and the two-dimensional
L²-to-L¹ factor $\sqrt2$, this gives exactly

\[
L_\beta=\sqrt2A_s[T_BL+\sqrt{2/k}T_g].
\]

For fixed $v$, the non-atomic part of $\mu_t(v)$ is fixed; only its two
anchor coefficients vary. Splitting the scalar Hessian integral into a
change of Hessian/directions and a change of measure yields
$C_C=m_dC_H$ and $L_C=m_dL_H+L_\beta C_H$.
The three arguments are independently linear, so these are genuine
trilinear bounds, not merely diagonal cubic estimates.

To verify Q11, differentiate $D_tv=\Pi_tU_t(v)$ along
$\theta'_t=-2D_tr_t$. The derivative of its tangent projection has a
normal term in the range of $G_t$, which pairs to zero with $D_tw$.
Its remaining tangent term is
$\Pi_tH_{\mu_t(v)}\theta'_t$. Therefore

\[
\langle v,K'_tw\rangle
=-2C_t(v;r_t,w)-2C_t(w;r_t,v).
\]

For $v=w=r_t$ at a fixed time this also reproduces the earlier constrained
curvature factor $-4$, providing a sign/factor cross-check.
This argument requires the established strong first directional derivative,
not a time derivative of the Hessian or $K''$.

The time-varying residual contributes an essential extra term:
$\|r_t-r_s\|_p\le2L^2Rh$, where the candidate locally denotes the common
initial-risk bound by $R=\sqrt{10}+1$.
For unit fixed $v,w$, each difference
$C_t(v;r_t,w)-C_s(v;r_s,w)$ is at most
$R(L_C+2C_CL^2)h$. There are two such terms in Q11 and each has coefficient
2. Hence

\[
|\langle v,(K'_t-K'_s)w\rangle|
\le4R(L_C+2C_CL^2)h.
\]

Taking the supremum over all unit $v,w$ is exactly the bounded operator norm
on the fixed common prediction Hilbert space. This proves Q12, including
its factor 4 and the residual-drift contribution. The L² force extension
and product bounds justify testing every unit vector, not merely bounded
or finitely supported coefficients. All operator norms here are for a
fixed task density; the constants are uniform over the declared classes.

## 6. Q13–Q14 and the conditional stopping criterion

Setting $s=0$ in Q12 gives $\Omega(t)\le\Lambda_1t$. The modulus now
depends on the stated source/reference constants rather than an unevaluated
supremum of reached trajectories. Its source constants may themselves be
unevaluated and extremely poorly conditioned, as the candidate explicitly
discloses.

The identification $\Gamma=2LJ$ agrees with the earlier kernel-speed
constant. Substitution into G22 yields Q14:

\[
|\Delta E(t)+8\mathcal C_p(r_0)t^2|
\le R^2t^2[(2\Lambda_1+8L^2\Gamma)t+\Gamma^2t^2].
\]

If a separate uniform certificate gives $\mathcal C_p(r_0)\le-c_*<0$,
and $T\le1$, the error is at most

\[
R^2T^3(2\Lambda_1+8L^2\Gamma+\Gamma^2).
\]

The proposed time restriction makes this at most $4c_*T^2$, while the
leading term is at least $8c_*T^2$. The resulting margin is therefore
$4c_*T^2$, exactly as claimed. The condition $T\le T_c$ preserves the
reached source neighborhood. No asserted positive Taylor radius is used.

The same substitution is valid in G24, subject to its separate scalar-clock
condition $|\alpha|T\le1$ and its fixed positive component normalizers.
It makes that remainder explicit but cannot give the individual or relative
component signs. The candidate does not claim those signs or a value of
$c_*$.

## 7. Outcome

| Component | Scoped verdict |
|---|---|
| Q1–Q4 generated-input source estimate | PASS with the explicitly stated full-history cap |
| Q5–Q6 force, gate and directional-field variation | PASS |
| Q7–Q9 scalar Hessian and Hölder factors | PASS |
| Q10 changing anchor coefficients | PASS |
| Q11 tangent/normal identity | PASS |
| Q12 operator norm and changing residual | PASS |
| Q13 modulus and Q14 finite-time remainder | PASS |
| Conditional positive margin given a uniform negative cubic | PASS |
| Actual uniform negative cubic or beneficial component sign | OPEN |
| Numerical source conditioning or E₀ completion | Not established |

No repair was requested. The check consisted of complete candidate reading,
source-hypothesis matching, and the algebraic/Hölder/constant reconstructions
above. No numerical package, symbolic package, external scientific theorem,
training computation or finite-network moment experiment was used.
