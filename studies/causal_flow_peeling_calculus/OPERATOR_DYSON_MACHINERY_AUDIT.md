# Operator-Dyson and Marked-Resolvent Machinery Audit

## Verdict

The operator route supplies three exact and reusable pieces:

1. a depth-recursive Bethe--Salpeter identity for nonlinear
   forward/backward curvature;
2. a resolvent identity that really resums repeated cap insertions;
3. a finite-width Schwinger--Dyson equation whose remainder identifies
   adaptive diagonal gates.

It nevertheless fails the genuine-reduction gate. The adaptive remainder
contains the source-to-flow sensitivity

\[
Y^{ab}(t)=\partial_{\Gamma_{ab}}\Theta(t)=U(t,0)e_{ab}
\]

exactly. A dynamic marked local law therefore needs the same chronological
tangent-propagator estimate that the calculus was meant to replace.
Normalized spectral laws are also blind to the trace-class channels on
which learning has order-one action.

The route is classified **KILL as an easier completion**, not as a no-go for
all operator-valued formulations. Its exact identities remain useful rules.

## 1. Most favorable honest operator state

Put

\[
P_l=\operatorname{diag}\phi'(z_l),\qquad
S_l=\operatorname{diag}\phi''(z_l),
\]

and define

\[
|v\rangle\langle w|_n\,y
:=v\langle w,y\rangle_n=\frac1n vw^Ty.
\]

Then

\[
\dot G_l=|b_{l+1}\rangle\langle x_l|_n.                            \tag{1}
\]

An ordinary scalar spectral law is insufficient. The minimally plausible
state is a multi-object marked traffic law:

- each layer is an object;
- \(G_l\) and \(G_l^T\) are the two orientations of the same source;
- \(P_l,S_l\), and other gates lie in the corresponding diagonal algebra;
- closed paths are evaluated by \(\tau_n(W)=n^{-1}\operatorname{Tr}W\);
- open paths are evaluated by
  \(\omega_{v,w}(W)=\langle v,Ww\rangle_n\);
- signed cap operators and block linearizations are queried by resolvents.

A finite truncation can retain words of length at most \(m\), finitely many
diagonal moments, resolvents on a finite spectral grid with rational degree
at most \(q\), and Gram data for their cyclic marked vectors. At fixed
\((m,q)\) this is finite and its formal one-time evolution follows from
Leibniz and

\[
\dot R=-R\dot K R.                                                  \tag{2}
\]

Differentiation increases word and response degree, so this is only a formal
autonomous hierarchy until a uniform cyclic-tail estimate is proved.

The learning perturbation is trace-class at the normalized scale:

\[
\|\Delta G_l(t)\|_*
\le\int_0^t\|b_{l+1}(s)\|_{2,n}\|x_l(s)\|_{2,n}\,ds=O_T(1).        \tag{3}
\]

It is asymptotically invisible to leading normalized spectral moments:

\[
\tau_n(\dot G_l^T\dot G_l)
=\frac{\|b_{l+1}\|_2^2\|x_l\|_2^2}{n^3}=O(n^{-1}),                \tag{4}
\]

but acts at order one on the marked feature:

\[
\dot G_lx_l=b_{l+1}\langle x_l,x_l\rangle_n.                       \tag{5}
\]

Equations (4)--(5) explain why a bulk spectral law cannot determine feature
learning.

## 2. Exact Bethe--Salpeter recursion

Let \(K_l=D_{z_l}b_l\), holding all parameters fixed except the indicated
preactivation. At the top,

\[
K_D=\operatorname{diag}\bigl(A\phi''(z_D)\bigr).
\]

For every \(l<D\), direct differentiation gives

\[
\boxed{
K_l=
\operatorname{diag}\bigl(\phi''(z_l)r_l\bigr)
+P_lG_l^TK_{l+1}G_lP_l .
}                                                                  \tag{BS}
\]

Indeed,

\[
db_l=\operatorname{diag}(\phi''(z_l)r_l)\,dz_l+P_lG_l^Tdb_{l+1},
\]

while \(db_{l+1}=K_{l+1}dz_{l+1}\) and
\(dz_{l+1}=G_lP_ldz_l\).

At depth two,

\[
K_1=\operatorname{diag}(\phi''(z_1)r_1)
+P_1G_1^T\operatorname{diag}(A\phi''(z_2))G_1P_1.                  \tag{6}
\]

At depth three,

\[
K_2=\operatorname{diag}(\phi''(z_2)r_2)
+P_2G_2^T\operatorname{diag}(A\phi''(z_3))G_2P_2.                  \tag{7}
\]

The second term in (7) has entries

\[
(P_2)_{jj}\sum_kG_{2,kj}A_k\phi''(z_{3,k})
G_{2,kj'}(P_2)_{j'j'},
\]

which is exactly the leading depth-three cap. Formula (BS) adds one unchanged
rule per layer, so its algebraic part is depth-recursive.

## 3. The cap is leading and admits exact resolvent resummation

Let \(G_{ki}\) be iid \(N(0,1/n)\), let \(D\) be fixed diagonal, and set
\(C=G^TDG\). The three Wick pairings give

\[
\mathbb E\,\tau_n(C^2)
=(\tau_nD)^2+\tau_n(D^2)+\frac1n\tau_n(D^2).                       \tag{8}
\]

Thus even when \(\tau_nD\) vanishes, the cap has a nonzero limiting second
moment. It is not width-deficient.

For

\[
K=D_0+PG^TDGP,\qquad R_0=(D_0-\zeta I)^{-1},
\]

Woodbury gives

\[
\boxed{
(K-\zeta I)^{-1}
=R_0-R_0PG^TD
(I+GPR_0PG^TD)^{-1}GPR_0 .
}                                                                  \tag{9}
\]

The problem is not algebraic resummation; it is the limiting law of these
resolvents in adaptive marked directions.

## 4. Exact adaptive Schwinger--Dyson identity

Let \(P=\operatorname{diag}(p_i)\), \(Q=\operatorname{diag}(q_j)\),

\[
X=P\Gamma Q,\qquad
\mathbb H=\begin{pmatrix}0&X\\X^T&0\end{pmatrix},\qquad
R=(\mathbb H-\zeta I)^{-1}.
\]

Writing \(\bar j=n+j\), the resolvent equation gives

\[
1=-\zeta R_{ii}+\sum_jp_iq_j\Gamma_{ij}R_{\bar ji}.                \tag{10}
\]

Gaussian integration by parts uses
\(\mathbb E[\Gamma_{ij}F]=n^{-1}\mathbb E[\partial_{ij}F]\).
Separate the direct source derivative by defining

\[
\dot{\mathbb H}^{ij}
=\partial_{ij}\mathbb H
-p_iq_j(E_{i,\bar j}+E_{\bar j,i}).
\]

Since \(\partial R=-R(\partial\mathbb H)R\), one obtains

\[
\boxed{
\begin{aligned}
1={}&-\zeta\,\mathbb ER_{ii}\\
&-\frac1n\sum_j\mathbb E\!\left[
(p_iq_j)^2(R_{\bar ji}^2+R_{\bar j\bar j}R_{ii})
\right]+\mathcal E_i ,
\end{aligned}
}                                                                  \tag{SD}
\]

where

\[
\boxed{
\mathcal E_i=\frac1n\sum_j\mathbb E\!\left[
\partial_{ij}(p_iq_j)R_{\bar ji}
-p_iq_j(R\dot{\mathbb H}^{ij}R)_{\bar ji}
\right].
}                                                                  \tag{11}
\]

For fixed gates independent of \(\Gamma\), \(\mathcal E_i=0\). Ward bounds,
concentration, and factorization then lead to the diagonal-algebra MDE

\[
m_i=-\frac1{\zeta+p_i^2\widetilde a},\qquad
\widetilde m_j=-\frac1{\zeta+q_j^2a},
\]

\[
a=\frac1n\sum_i p_i^2m_i,\qquad
\widetilde a=\frac1n\sum_jq_j^2\widetilde m_j.                    \tag{12}
\]

Equation (11) states exactly what adaptivity adds. Repeated expansion of its
gate derivatives produces the response/cap hierarchy; calling the sum a
self-energy does not remove it.

## 5. Exact initialization conditioning

If \(x\) is independent of \(\Gamma\), \(z=\Gamma x\), and

\[
\Pi_x=I-\frac{xx^T}{\|x\|_2^2},
\]

then Gaussian regression gives

\[
\boxed{
\Gamma=\frac{zx^T}{\|x\|_2^2}+\widetilde\Gamma\Pi_x,
}                                                                  \tag{13}
\]

where \(\widetilde\Gamma\) has iid \(N(0,1/n)\) entries and is independent of
\((x,z)\). At depth two and \(t=0\), conditioning on
\(z_2=\Gamma_1x_1\) leaves an independent Gaussian bulk plus one marked
rank-one direction. At depth three, conditioning on \(z_3=G_2x_2\)
similarly splits the cap into a weighted-Wishart bulk and finitely many spike
and cross terms.

This computes static bulk laws, but ordinary freeness already fails for
marked observables. If \(z=\Gamma x\) and
\(S=\operatorname{diag}\phi''(z)\), then

\[
\langle x,\Gamma^TS\mathbf1\rangle_n
=\frac1n\sum_i z_i\phi''(z_i)
\longrightarrow \mathbb E[Z\phi''(Z)]<0.                          \tag{14}
\]

Replacing \(S\) by an independent diagonal would give zero. The marked
regression spike is leading.

## 6. Positive-time obstruction

At positive time, every vector presented to a reused source depends on that
source. For the complete parameter state,

\[
Y^{ij}(t)=\partial_{\Gamma_{ij}}\Theta(t)
\]

satisfies

\[
\boxed{
\dot Y^{ij}(t)=DF(\Theta(t))Y^{ij}(t),\qquad
Y^{ij}(0)=e_{\Gamma_{ij}}.
}                                                                  \tag{15}
\]

Consequently

\[
\partial_{\Gamma_{ij}}P_l(t)
=\operatorname{diag}\!\left(
\phi''(z_l(t))Dz_l(\Theta(t))[Y^{ij}(t)]
\right).                                                           \tag{16}
\]

The adaptive error (11) therefore contains the chronological tangent
propagator exactly.

- Finite-projection conditioning is exact at initialization, but a nonlinear
  positive-time state does not leave a Gaussian orthogonal complement.
- Gaussian cumulant expansion is already exact in (11); its correction is
  (15), and further integration by parts creates higher sensitivities.
- A fixed-step replacement can condition on finitely many directions, but
  the vanishing-mesh limit creates a continuum Gram kernel unless an
  independent response-tail theorem compresses it.
- A pointwise MDE does not control chronological products of noncommuting
  Hessians.

## 7. Sufficient master theorem

Let \(\mathsf S_m(t)\) be a finite marked-word/resolvent truncation,
\(\rho_{n,m}(t)\) its omitted source, and \(U_n(t,s)\) the finite-width
tangent propagator. A sufficient theorem would give computable autonomous
vector fields \(F_m\), reconstruction maps \(O_m\), and
\(\delta_m(T)\downarrow0\), with fixed-\(m\) convergence and

\[
\boxed{
\limsup_{n\to\infty}\mathbb E\sup_{t\le T}
\left\|\int_0^tU_n(t,s)\rho_{n,m}(s)\,ds\right\|_{\rm obs}
\le\delta_m(T),
}                                                                  \tag{17}
\]

uniformly over reachable restart states. Then the finite truncations would
converge to a compact-time autonomous limit.

The leaf audit is:

1. **Finite-time normalized moments:** triangular deterministic estimates
   and bounded activation derivatives give these at fixed depth.
2. **Exact one-time differential algebra:** (1), (2), and (BS) prove it.
3. **Static finite-projection innovation:** (13) proves it.
4. **Fixed-gate MDE off the real axis:** standard
   Ward/concentration/stability machinery applies after truncation.
5. **Dynamic innovation:** requires source-sensitivity control through
   (15)--(16); this is a core theorem.
6. **Adaptive marked isotropic local law:** must hold for adaptive cyclic
   vectors and signed cap pencils. Trace laws do not imply it.
7. **Chronological cyclic-tail estimate (17):** this is the original
   reachable tangent-stability problem in explicit form.
8. **Finite-dimensional convergence and restartability:** standard once
   1--7 hold uniformly over restart states.

Leaves 5--7 are not technical cleanup, and leaf 7 is not a reduction.

## 8. Schatten--Hölder misses the marked channel

For self-adjoint \(H_k\) and \(hK=T\), noncommutative Hölder gives

\[
\left\|\prod_{k=1}^K e^{hH_k}\right\|_{S_2,\tau}
\le\prod_{k=1}^K(\tau e^{2TH_k})^{1/(2K)}.                         \tag{18}
\]

Take \(H_k=\lambda vv^T\) for one Euclidean unit vector \(v\). Then

\[
\tau e^{2TH_k}
=1+\frac{e^{2T\lambda}-1}{n}\longrightarrow1,
\]

whereas for \(x=\sqrt n\,v\),

\[
\left\|\prod_{k=1}^Ke^{hH_k}x\right\|_{2,n}=e^{T\lambda}.          \tag{19}
\]

Thus a valid bulk inequality misses low-rank marked amplification. Repair
requires decorated exponentials in adaptive vectors and control of their
rotation under later Hessians, again the chronological estimate.

## 9. Claim-level conclusion

- **Proved:** (BS), cap scaling (8), Woodbury resummation (9), adaptive
  Schwinger--Dyson identity (SD), static regression (13), and the
  Schatten--Hölder limitation (19).
- **Conditionally valid:** finite marked-resolvent truncations, assuming
  dynamic marked local laws and (17).
- **Falsified:** sufficiency of ordinary scalar/operator-valued spectral
  laws, marked freeness of adaptive diagonal gates, and sufficiency of
  normalized spectral exponential control.
- **Open:** a dynamic reachable marked local law strictly easier than
  tangent stability.

The operator calculus organizes and resums the alternating caps, but its
probability and time-completion theorem is the original bottleneck. It is
therefore retained as a component library and rejected as a standalone
completion strategy.
