# Scaled stability route for the compression error prefactor

2026-10-04. Independent scoped derivation, frozen before exchanging
conclusions. **Partial result; the requested polynomial prefactor remains
open in this route.** No numerical experiment or Git operation was performed.

The complete scientific inputs were `STORAGE_QUADRATIC_IMPROVEMENT.md`,
`GENERAL_WEIGHTED_COMPARISON.md`, `DATASET_LABEL_DEPENDENCE.md`,
`INPUT_DEPTH_REFINEMENT.md`, and `SAMPLE_COUNT_REFINEMENT.md`, all in this
study. Required research/process and mathematical-presentation instructions
were also read. Linked scientific sources outside this input list were not
retrieved. The source and probability theorems stated in these inputs remain
inputs, rather than newly checked proofs here.

The target is the actual same-time, whole-sphere, all-time dense-versus-
compressed error, retaining the corrected-readout autonomous optimizer,
the label condition (Y\le c\lambda), and total retained size

\[
C\lambda^{-2}\log^{3d+2}(en)+Cm(d+1),\qquad
\lambda=\min(1,\gamma/m).
\]

Here (m) is the number of training samples, (\gamma) is the unnormalized
limiting top-feature Gram gap, and (Y=\|y\|_2/\sqrt m). Constants below
are structural: fixed depth, input dimension, and activation bounds may
enter, but (m,\gamma,Y,n) do not enter unless displayed.

## 1. A strictly better raw source-error estimate

Let (\epsilon>0) be the coordinate source tolerance on the existing
source horizon (T=C\lambda^{-1}\log(en)). Assume

\[
0<Y\le c\lambda,\qquad
\epsilon\le\min(1,Y/\sqrt\lambda).
\tag{1}
\]

The argument below gives the improved deterministic estimate

\[
\sup_{t\le T,v\in S^{d-1}}|f_C(t,v)-f_n(t,v)|
\le C\lambda^{-1/2}\epsilon
 \exp\left\{C\frac{Y}{\lambda^{3/2}}
       +C\frac{Y^2}{\lambda^2}\sqrt{\log(en)}\right\}.
\tag{2}
\]

In particular, the raw amplification of the unchanged tolerance

\[
\epsilon=n^{-1}
\tag{3}
\]

is displayed explicitly. There is no replacement of (\epsilon) by an
exponentially more accurate data-dependent tolerance. Relative to the
previous exponent

\[
C Y\lambda^{-5/2}
 +C Y^2\lambda^{-7/2}\sqrt{\log(en)},
\]

both terms improve. The first term in (2) remains exponential in the
conditioning and therefore does not solve the requested polynomial
dependence on (m\) and the gap.

## 2. Error variables and small physical scales

Use all definitions, norms, and the comparison state (A_R,B_R,w_R) of
Sections 4–5 of `STORAGE_QUADRATIC_IMPROVEMENT.md`. Thus (A_R=A_{n,I_1}),

\[
B_R^{(\ell)}=B_0^{(\ell)}+
 \frac2m\sum_a\int_0^t c_{n,a}(s)
 \delta_{n,a}^{(\ell)}(s)_{I_\ell}
 h_{n,a}^{(\ell-1)}(s)_{I_{\ell-1}}^\top H_{\ell-1}\,ds,
\qquad w_R=w_{n,I_L}.
\]

These are proof objects only. The actual compressed state and dynamics
are unchanged. Define separate nonnegative errors

\[
\begin{aligned}
h(t)&=\|A_C-A_R\|_{H_1,F}
 +\sum_{\ell=2}^L\|B_C^{(\ell)}-B_R^{(\ell)}\|_{\mathrm{HS}},\\
r(t)&=\|w_C-w_R\|_{H_L},\\
u(t)&=\|c_C-c_n\|_m.
\end{aligned}
\tag{4}
\]

The symbol (h(t)) in (4) is a scalar hidden-parameter error; layer
features retain their indexed notation (h_a^{(\ell)}). All three
errors start at zero. Put

\[
\alpha=Y/\sqrt\lambda,\qquad s=Y/\lambda,
\qquad \rho(t)=\|c_n(t)\|_m.
\tag{5}
\]

The inherited energy and source estimates give

\[
\rho(t)\le Ye^{-c_0\lambda t},\quad
\int_0^\infty\rho\le Cs,\quad
\|w_R\|_{H_L}+\|\widehat w_C\|_{H_L}
 +\max_{a,\ell}\bigl(\|\delta_{n,a,I_\ell}^{(\ell)}\|_{H_\ell}
 +\|\delta_{C,a}^{(\ell)}\|_{H_\ell}\bigr)\le C\alpha.
\tag{6}
\]

For the selected reference vectors, (6) uses exact source isometry,
coordinate error (\epsilon), and (1). All mixers are bounded in their
induced operator norms. The actual reference coordinate carrier maximum,
without adding an artificial lower bound of one, satisfies

\[
M_0:=\max_{a,\ell,i,t\le T}|k_{n,a,i}^{(\ell)}(t)|
 \le Cs\sqrt{\log(en)}.
\tag{7}
\]

The top carrier also obeys (7), directly by integrating its bounded
coordinate update. The inherited lower-layer carrier estimate supplies
the remaining cases.

## 3. Orthogonality improves the readout subtraction

At the compressed top layer write

\[
F=F_C,\quad Q=F^\top H_LF,\quad
P=FQ^{-1}F^\top H_L.
\]

Then (P) is an orthogonal projector for the (H_L) inner product.
The correction formula gives the exact identity

\[
\widehat w_C-w_R
 =(I-P)(w_C-w_R)
 +FQ^{-1}\bigl(y-c_C-F^\top H_Lw_R\bigr).
\tag{8}
\]

The original proof bounded the first term by feeding the entire raw
readout error through (Q^{-1}). Equation (8) instead uses

\[
\|(I-P)(w_C-w_R)\|_{H_L}\le r.
\]

Forward subtraction involves only hidden parameters, so

\[
\sup_v\|h_C^{(\ell)}(v)-h_{n,I_\ell}^{(\ell)}(v)\|_{H_\ell}
 \le C(h+\epsilon).
\tag{9}
\]

Using the true dense residual, the observation/source pairing defect,
and (\|w_R\|\le C\alpha), the sample norm of the vector in parentheses
in (8) is at most

\[
u+C\alpha h+C\epsilon.
\]

The source observation defect is actually bounded by (Cs\epsilon),
but the structural upper bound (C\epsilon) is enough here. Since

\[
\|FQ^{-1}b\|_{H_L}\le C\lambda^{-1/2}\|b\|_m,
\]

the effective-readout error (e=\|\widehat w_C-w_R\|_{H_L}) satisfies

\[
e\le C\left(r+\lambda^{-1/2}u+s h
                    +\lambda^{-1/2}\epsilon\right).
\tag{10}
\]

Crucially, (r) has coefficient one and the hidden error has coefficient
(s), rather than (\lambda^{-1/2}).

## 4. Keep the small response factors in every Gram term

Descending through the backward recursion, a changed gate multiplies
the true selected carrier and therefore costs (CM_0(h+\epsilon)).
A changed mixer multiplies a reference response of norm (C\alpha).
The upper response error propagates only through bounded mixers and
bounded gates. Combining this recursion with (10) proves

\[
\max_{a,\ell}\|\delta_{C,a}^{(\ell)}-
                   \delta_{n,a,I_\ell}^{(\ell)}\|_{H_\ell}
\le C\left[r+\lambda^{-1/2}u+(s+M_0)h
                         +(\lambda^{-1/2}+M_0)\epsilon\right].
\tag{11}
\]

The carrier contribution to the source term is retained in this formula.
It is not assumed that (M_0\epsilon\le C\epsilon\).

In a hidden tangent-Gram term, every changed backward vector is paired
with an unchanged response of norm (C\alpha); a changed feature is
paired with two responses and therefore has coefficient (C\alpha^2).
The top-feature Gram contributes (C(h+\epsilon)). Exact source
isometry bounds the original-versus-selected pairing defects by
(C\epsilon) for features and (C\alpha\epsilon) for responses.
Consequently

\[
\left\|\frac{K_C-K_n}{m}\right\|_{\mathrm{op}}
\le C\left[(1+\alpha(s+M_0))h+\alpha r+s u
                         +(1+\alpha M_0)\epsilon\right].
\tag{12}
\]

For example, the normalized sample operator norm of an entrywise error
matrix is bounded by its maximum entrywise magnitude; hence this step
introduces no factor (m). Products of two small response norms use
(6), rather than replacing both by a constant.

Subtracting the exact residual equations and using the compressed Gram
margin yields

\[
D^+u\le-c_1\lambda u
 +C\rho\left[(1+\alpha(s+M_0))h+\alpha r+s u
                         +(1+\alpha M_0)\epsilon\right].
\]

Because (\rho s\le Ys=s^2\lambda), a structural reduction of the
already structural constant (c) in (Y\le c\lambda) absorbs the
(u) term into the damping. Thus, with

\[
J(t)=\int_0^t\rho(\tau)
 \left[(1+\alpha(s+M_0))h(\tau)+\alpha r(\tau)
                         +(1+\alpha M_0)\epsilon\right]d\tau,
\]

we have

\[
u(t)\le CJ(t),\qquad
\int_0^t u\le C\lambda^{-1}J(t).
\tag{13}
\]

At zero residual error these statements follow by regularizing the norm,
as in the inherited comparison proof.

## 5. A scaled parameter error and the improved exponent

The hidden velocity difference contains a residual difference times a
compressed response, and a true residual times feature/response
differences. Equations (6), (9), and (11) give

\[
\begin{aligned}
h(t)\le{}&C\alpha\int_0^t u
 +C\int_0^t\rho\left[r+\lambda^{-1/2}u+(s+M_0)h
                          +(\lambda^{-1/2}+M_0)\epsilon\right],\\
r(t)\le{}&C\int_0^t u+C\int_0^t\rho(h+\epsilon).
\end{aligned}
\tag{14}
\]

The feature factor in a hidden update adds (C\alpha(h+\epsilon)),
which is absorbed by the displayed terms because (\alpha\le s).
These inequalities compare with the exact velocities defining (A_R),
(B_R), and (w_R), so they require no time derivative of a source
approximation or of an observation defect.

Set

\[
E(t)=h(t)+\sqrt\lambda\,r(t)+u(t).
\tag{15}
\]

The term (\int\rho u/\sqrt\lambda) in (14) is at most
(\alpha\int u), since (\rho\le Y). Hence the coefficient of
(\int u) in (h+\sqrt\lambda r) is at most (C\sqrt\lambda),
using (s\le c). Insert (13), and use

\[
h\le E,\quad r\le E/\sqrt\lambda,\quad
\alpha/\sqrt\lambda=s.
\]

Every coefficient is bounded by (C(\lambda^{-1/2}+M_0)). For example,
the seemingly problematic carrier contribution from (13) is

\[
\lambda^{-1/2}\alpha M_0=sM_0\le CM_0.
\]

The source terms obey the same bound. Adding the pointwise estimate for
(u) from (13) therefore proves

\[
E(t)\le C(\lambda^{-1/2}+M_0)
                     \int_0^t\rho(\tau)(E(\tau)+\epsilon)d\tau.
\tag{16}
\]

If (G(t)) is the right-hand integral majorant plus (\epsilon), then
(G(0)=\epsilon), (E+\epsilon\le G), and
(G'\le C(\lambda^{-1/2}+M_0)\rho G). Integrating this scalar
differential inequality gives

\[
\sup_{t\le T}(E(t)+\epsilon)
\le\epsilon\exp\{C(\lambda^{-1/2}+M_0)s\}.
\tag{17}
\]

The output difference is at most (C(e+\alpha(h+\epsilon)+\epsilon)).
Equations (10), (15), and (17), followed by (7), prove (2).

Both networks already have their independent global energy/Gram bounds;
the comparison uses those bounds rather than requiring its error to
preserve the compressed Gram. The selected proof mixer (B_R) is also
bounded: its learned operator displacement is at most (C\alpha s).
Thus this derivation does not introduce an exponential-data first-exit
width threshold.

## 6. Width, tails, and what is still exponential

At tolerance (3), the coefficient

\[
b=C(Y/\lambda)^2
\]

of (\sqrt{\log(en)}) in (2) is structurally bounded. Writing
(x=\sqrt{\log(en)}), the elementary inequality

\[
bx-\tfrac12x^2\le\tfrac12b^2
\]

shows directly, for every (n\ge1), that

\[
n^{-1}e^{b\sqrt{\log(en)}}\le C n^{-1/2}.
\tag{18}
\]

No condition making (\log n) exceed a positive power of (m/\gamma)
is used to absorb this factor. The unchanged finite-time comparison is
therefore bounded by

\[
C\lambda^{-1/2}\exp\{CY/\lambda^{3/2}\}\,n^{-1/2}.
\tag{19}
\]

For completeness the coarse differentiated-readout bounds in Section 6
of the runtime source imply, explicitly under (Y\le c\lambda),

\[
\sup_v|\partial_t f_C(t,v)|\le C\lambda^{-1}\rho_C(t),
\qquad
\sup_v|f_C(\infty,v)-f_C(t,v)|
 \le C Y\lambda^{-2}e^{-c\lambda t}.
\tag{20}
\]

Indeed (\|\dot V\|\le C\alpha\rho_C),
(\|\dot T_V\|+\|\dot P_V\|\le C\lambda^{-2}\alpha\rho_C),
(\|w_C\|\le C\alpha), and (\|b\|\le2Y). The potentially
largest product is (C\lambda^{-2}\alpha^2\rho_C
=CY^2\lambda^{-3}\rho_C\le C\lambda^{-1}\rho_C).
The remaining terms are smaller. The supplied dense tail is no larger
than this conservative scale. A structural horizon constant makes the
tail at (T) at most (CY\lambda^{-2}n^{-1}). Consequently this route
gives the completely explicit all-time prefactor

\[
\sup_{t\in[0,\infty],v}|f_C(t,v)-f_n(t,v)|
\le C\left[
\lambda^{-1/2}e^{CY/\lambda^{3/2}}+Y\lambda^{-2}
\right]n^{-1/2}.
\tag{21}
\]

The remaining width qualifications are the inherited source probability
threshold, the usual logarithmic gap condition used in the storage
formula, and (n\ge\sqrt\lambda/Y) from (1). This note neither
quantifies the inherited stochastic threshold nor replaces the
exponential in (21) by an extra width requirement.

When (\lambda=\gamma/m) and (Y=c\lambda), the first prefactor is

\[
C\sqrt{m/\gamma}\exp\{Cc\sqrt{m/\gamma}\}.
\]

This is a real improvement but is still outside the requested polynomial
dependence. Storage, runtime, query domain, reference realization, and
label scale are unchanged. The case (Y=0) is the exact zero predictor
and does not require any of the divisions by (Y) implicit in (1).

## 7. Exact remaining obstruction in this route

The residual damping in (13) yields one inverse gap. A raw readout error
is then bounded by the integral of the residual error, whereas a hidden
update responds directly to a readout error. After (15), this feedback
has coefficient (\lambda^{-1/2}\int\rho=Y/\lambda^{3/2}).
Small response norms and orthogonal readout reconstruction alone do not
remove it from (16).

This does **not** prove that exponential amplification is necessary for
the actual dynamics. In the vector readout equations, a residual error
has a sign and direction relative to the current feature span. Passing
to the three nonnegative norms in (4) discards that information. A
successful continuation would need a dissipative estimate for the
effective readout (or an equivalent coupled residual/readout energy),
retaining this cancellation while handling the moving feature span and
the non-diagonal activation metric. No such complete estimate is proved
here. In particular, independent fitting and finite path length do not
by themselves supply it.

Status recommendation: retain (2) and (21) as a candidate partial
quantitative improvement and submit them for a separate check; keep the
polynomial-prefactor target open. No independent check of this new
derivation had been received at the freeze time.
