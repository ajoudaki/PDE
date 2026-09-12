# Route H: harmonic symmetries and the full fitted-reference tangent

Frozen independent candidate, 2026-09-12. Author: scoped route H agent.

**Status: partial mathematics; E₀ remains open.** The anchor constraint forces the
full frozen tangent to mix ordinary Fourier frequencies. The proved reference
symmetries separate only two infinite-dimensional sectors, and do not fix the
sign of the nonlinear advantage. There is an exact finite-time comparison with
an actual-path bound of order $T^2$, but no positive lower bound. A separate
finite-time counterexample proves that positive semidefiniteness, the reference
symmetries, anchor preservation and nonproportional kernel movement alone are
insufficient. That counterexample is an auxiliary kernel flow, not the neural
flow and not a counterexample to E₀.

No training experiment, Git operation, subagent, other study, other route or
trained-prediction-selected target was used. This candidate was prepared before
route comparison. The supervisor owns the shared README and Git coordination.

## 1. Exact admitted object and source interface

Use the contract's two-hidden-layer bias-free tanh network, stored Gaussian
variances $(1,1/n,1/n^2)$, mobilities $(n,1,n)$, output division by $n$,
unhalved squared loss and physical GF. Input is $x=\sqrt2u$, $u\in S^1$.
All finite networks keep their actual initial random readout and train from
original initialization on the fixed anchor/added-law mixture. Nothing here
restarts an actual finite network at the endpoint.

Write $\theta_0=\theta_\dagger$, $f_0=F_*$, and use the full raw gradient

\[
g_\theta(u)=\bigl(\phi'(w\cdot u)A^*[c\phi'(AH^1(u))]u,
 [c\phi'(AH^1(u))]\otimes H^1(u),H^2(u)\bigr).
\]

The action and adjoint are the same reused initialized action plus its trained
Hilbert–Schmidt increment. Put $d_\theta=\Pi_\theta g_\theta$, with both anchor
gradients in the projector. For fixed density $p$, define

\[
\mathcal T_\theta r=\int r(u)d_\theta(u)p(u)\,d\rho(u),\qquad
\mathsf K_\theta=\mathcal T_\theta^*\mathcal T_\theta.
\tag{H1}
\]

Thus $\mathsf K_\theta$ acts on the real odd subspace of $L^2(p\rho)$,
is positive and self-adjoint, and uses all raw parameter blocks. C.4.10.2 gives
the reached constrained path on $[0,T_c]$, its original-mixture selection,
and the actual finite-GF bridge in the stipulated iterated limit. Along it,

\[
r'= -2\mathsf K_{\theta(\tau)}r,\qquad
r=f_\theta-q,\qquad \frac d{d\tau}\|r\|_p^2=-4\|\mathcal T_\theta r\|^2.
\tag{H2}
\]

The frozen residual solves $r_{\rm fr}'=-2\mathsf K_0r_{\rm fr}$,
$r_{\rm fr}(0)=r_0=f_0-q$. Both clocks are exactly $\tau=\epsilon t$.
Centered bounded label noise leaves (H2)'s population force unchanged.

The new results below use C.4.10.2's bounds and strong reached-curve product
rules, C.4.10.3's injectivity, and the reference symmetry construction in
C.4.5.1. Their hypotheses hold for the class in §3: positive full-circle
density, bounded labels, finitely capped odd target, exactly fitted anchors.
No ambient twice-Fréchet-differentiable neural map is assumed.

## 2. Exact symmetry information and its obstruction

Let $S\alpha=\pi/2-\alpha$ denote the coordinate swap. At the reference,

\[
F_*(S\alpha)=-F_*(\alpha),\qquad F_*(\alpha+\pi)=-F_*(\alpha).
\tag{H3}
\]

The swap plus readout sign change is an isometry of the full raw metric. The
Gaussian first-row law is swap-invariant; including the transformed programs
on the same generated carrier gives the probability-space isometry of
C.4.5.1 R7. It preserves the action and actual adjoint. Differentiating the
scalar transformation $f(u)\mapsto-f(Su)$ shows that the endpoint gradients
at $u,Su$ are related by minus that raw isometry. The two anchor gradients
are interchanged up to sign. Their span, orthogonal projector and complement
are therefore transformed by the same isometry. Consequently

\[
k_0(Su,Sv)=k_0(u,v),\qquad k_0(-u,v)=-k_0(u,v).
\tag{H4}
\]

For swap-invariant $p$, the operator $Uf=f\circ S$ is an isometric
self-adjoint involution in the common prediction metric. Equation (H4) gives
$U\mathsf K_0=\mathsf K_0U$. Thus its eigenspaces
$\mathcal H_+=\{Uf=f\}$ and $\mathcal H_-=\{Uf=-f\}$ are orthogonal
and invariant. The orthogonality is elementary: for $a\in\mathcal H_+$,
$b\in\mathcal H_-$, invariance of the integral changes $\langle a,b\rangle$
to its negative. No claim is made that an arbitrary added task retains this
symmetry along its nonlinear path.

For $m=2k+1$, set $s_m=(-1)^k$ and

\[
\chi_m^\pm(\alpha)=\cos(m\alpha)\pm s_m\sin(m\alpha).
\tag{H5}
\]

The identities
$\cos(mS\alpha)=s_m\sin(m\alpha)$ and
$\sin(mS\alpha)=s_m\cos(m\alpha)$ give $U\chi_m^\pm=\pm\chi_m^\pm$.
All positive odd $m$ contribute to each sector. Multiplication by
$h=\sin^2(2\alpha)$ preserves these sectors. Symmetry therefore allows
arbitrary coupling between $h\chi_1^+$ and $h\chi_{11}^+$, for example.
It provides no different representation label with which to order their rates.

**Anchor obstruction to independent ordinary frequencies.** For every $p$
bounded above and below by positive constants and every positive odd integer
$m$, the plane

\[
V_m=\operatorname{span}\{\cos(m\alpha),\sin(m\alpha)\}
\]

is not invariant under $\mathsf K_0$.

Indeed $d_0(e_1)=d_0(e_2)=0$, so every continuous prediction
$\mathsf K_0 a$ vanishes at both anchors. If $V_m$ were invariant, its
image would be $A\cos(m\alpha)+B\sin(m\alpha)$. At $\alpha=0$ this
gives $A=0$, and at $\alpha=\pi/2$ it gives $B=0$, since
$\sin(m\pi/2)=\pm1$. Equality as $L^2(p\rho)$ functions gives equality
everywhere here: both functions are continuous and $p$ has full support.
Thus $\mathsf K_0$ would kill $V_m$, contradicting C.4.10.3's injectivity
of $\mathcal T_0$. The same argument shows that no nonzero ordinary sine or
cosine at an odd frequency is an eigenfunction of $\mathsf K_0$.

In particular the full frozen kernel is not a rotation-invariant convolution
kernel. Another direct proof is that rotational invariance would make its
diagonal constant, whereas it is zero at the anchors and nonzero elsewhere.
This rules out a Fourier-by-Fourier diagonal comparison with this baseline.
It does not rule out an advantage from nonlinear harmonic interactions.

For $p=1$, replacing a task $q$ by $q^S=-q\circ S$ transforms its whole
constrained path and its whole frozen path by $f\mapsto-f\circ S$.
The raw isometry and uniqueness establish this for the full finite episode.
Thus both risks, and their difference, agree for the paired tasks. In the
family below this simultaneously changes both $t$'s to their negatives,
leaves both $z$'s fixed, and sends $w$ to $-w\circ S$.
It is an evenness identity, not a positivity identity;
it does not permit changing the sign of just one $t$.

## 3. A fixed ordinary, quantitatively active family

This family is frozen to specify the sign obligation, not claimed to satisfy it.
Take $s=1$, $R=1/8$, cap $N=5$, and

\[
a=R/96=1/768,\quad c_0=3/8,\quad B_0=1+\sqrt{10},
\quad \eta_p=\min\{1/512,a/(64B_0)\}.
\]

Let

\[
v=t_1\chi_1^++t_{11}\chi_{11}^+
       +z_1\chi_1^-+z_{11}\chi_{11}^-+w,
\]
\[
t_1,t_{11}\in[a,2a],\quad z_1,z_{11}\in[-a/4,a/4],\qquad
\sum_{k=0}^{5}(2k+1)(|w_{c,k}|+|w_{s,k}|)\le a/64,
\tag{H6}
\]

and $q=q_0+hv$. The four displayed main coefficients vary independently.
Before $w$, the sine and cosine coefficients at frequencies 1 and 11 each
have magnitude at least $3a/4$. After $w$, each still has magnitude at
least $47a/64$. The weighted budget is at most

\[
2(t_1+11t_{11})+a/64\le48a+a/64<R.
\]

The perturbation radius is a fixed fraction $1/64$ of an active coefficient,
and controls both $\|w\|_\infty$ and $\|w'\|_\infty$. Targets are specified
entirely by elementary functions and coefficient ranges. All degrees are fixed;
the largest frequency in $q$ is 15. This is not a single favorable witness
enlarged after training.

Let $p$ range over all mean-one circle densities with
$\|p-1\|_\infty\le\eta_p$ and circular Lipschitz constant at most 1.
This gives full-circle support and includes arbitrary swap-breaking density
perturbations in that prescribed topology. The small radius is relative to the
active target scale, with an explicit factor $B_0$ to bound contamination by
the reference residual. Labels use the contract's conditionally centered noise
$|\xi|\le h/8$, $E[\xi^2\mid X]\le\sigma^2\le1/64$. The source bound
$|q_0|\le1-h/4$, together with $\|v\|_\infty\le R$, gives $|Y|\le1$.

Put $\psi_1=h\chi_1^+$, $\psi_{11}=h\chi_{11}^+$.
Their Fourier supports are respectively contained in ${1,3,5}$ and
${7,11,15}$; they are orthogonal in $L^2(\rho)$. Also

\[
\|\psi_m\|_\rho^2=\int h^2(1+s_m\sin(2m\alpha))\,d\rho=3/8.
\tag{H7}
\]

The sine integral vanishes by reflection, and
$h^2=(3-4\cos4\alpha+\cos8\alpha)/8$. The baseline $F_*-q_0$ and
the two $z$-terms are swap-antisymmetric, hence orthogonal to both
$\psi$'s under $\rho$. Projection onto the symmetric sector, followed
by the reverse triangle inequality, proves uniformly

\[
\mathcal E_\nu(F_*)\ge
e_0:=\frac12\bigl(\sqrt{3/4}-1/64\bigr)^2a^2>0.
\tag{H8}
\]

Since the full endpoint force is injective on odd functions, this excludes
stationarity as well as vanishing target components. The sizes are modest:
the chosen active coefficient scale is $1/768$, and the guaranteed initial
risk scale is proportional to its square. No order-one advantage is inferred.

### A fixed component normalization in the common metric

Let $\Psi=(\psi_1,\psi_{11})$, and let $G(p)_{ij}=\langle\psi_i,\psi_j\rangle_p$.
Use the positive symmetric inverse square root to define
$(e_1,e_{11})=\Psi G(p)^{-1/2}$. The basis depends only on the independently
chosen two frequency bands and the common test density. It is chosen before
either path. At $p=1$, $e_j=\psi_j/\sqrt{c_0}$. For perturbed $p$, it
is the symmetric orthonormalization of those same two bands.

Here are quantitative checks on this normalization. Cauchy–Schwarz gives
$\|G/c_0-I\|\le2\eta_p$, so $G>0$. Writing
$b_j=\langle r_0,e_j\rangle_p$, the difference between
$(\langle r_0,\psi_j\rangle_p)_j$ and $-c_0(t_1,t_{11})$ has norm at
most $\sqrt{2c_0}(a/64+\eta_pB_0)\le\sqrt{2c_0}a/32$.
Finite-dimensional diagonalization and the derivative of $x^{-1/2}$ on
$[1/2,3/2]$ give
$\|(G/c_0)^{-1/2}-I\|\le3\eta_p$.
Consequently

\[
\|(b_1,b_{11})+\sqrt{c_0}(t_1,t_{11})\|
\le6\sqrt{2c_0}\eta_p a+a/16<a/8.
\]

In particular each initial component energy is at least
$(\sqrt{c_0}-1/8)^2a^2>0$. There is no division by an inactive component.

An independently interpretable relative-learning observable is the recovered
fraction of initial error in each band,

\[
L_j(f)=1-\frac{\langle f-q,e_j\rangle_p^2}{b_j^2},
\qquad j\in\{1,11\}.
\tag{H9}
\]

The high-minus-low contrast $L_{11}-L_1$ tests whether the higher band catches
up relative to the lower band. It is fixed for that purpose, without looking at
which path performs better. All components outside the two-dimensional span
are retained in the actual evolution and the total risk.

For the actual path, $a_j(\tau)=\langle r(\tau),e_j\rangle_p$ obeys

\[
L_j'(\tau)=\frac{4a_j(\tau)\langle e_j,\mathsf K_{\theta(\tau)}r(\tau)\rangle_p}{b_j^2}.
\tag{H10}
\]

This contains the full residual, not its projection onto the two bands. Thus
off-band interactions are exact terms, not discarded errors. No sign for the
finite-time difference of (H9) has been established.

## 4. An actual-path comparison with a real finite-time remainder bound

Retain $L,k,A_s,T_g$ exactly as defined in C.4.10.2 NSC3–4 and NSC26.
Its controlled-curve proof gives
$\|g'(u)\|\le T_gm$, $\|G'\|\le\sqrt2T_gm$, where the constrained
curve has total absolute control density $m\le A_s$. For
$B=GM^{-1}$, $\|B\|\le\sqrt{2/k}$. Differentiating the orthogonal
projection gives

\[
\Pi'=-\Pi G'B^*-BG'^*\Pi,\qquad
\|\Pi'\|\le4T_gm/\sqrt{k}.
\]

The source's strong absolutely continuous product rules justify this almost
everywhere; they use the two controlled $L^4$ factors in the first-row
gradient and the bounded readout. Hence, with

\[
J_d=T_g(1+4L/\sqrt{k}),\qquad C_K=2LJ_dA_s,
\]

\[
\sup_u\|d_{\theta(\tau)}(u)-d_0(u)\|\le J_dA_s\tau,
\quad \|\mathsf K_{\theta(\tau)}-\mathsf K_0\|\le C_K\tau.
\tag{H11}
\]

For the operator bound, first bound the pointwise kernel derivative by
$2LJ_dm$, then integrate against the probability density and apply
Cauchy–Schwarz. This controls an actual reached curve. It neither assumes a
Taylor radius nor upgrades an ambient Hölder bound to a Lipschitz bound.

Put $D=r_{\rm fr}-r$. Bounded positive $\mathsf K_0$ has a contraction
semigroup $e^{-2t\mathsf K_0}$: the norm-convergent exponential series
solves its linear equation, and differentiation of the squared norm gives
nonpositive derivative. Subtracting the two residual equations and integrating
therefore gives exactly

\[
D(T)=2\int_0^T e^{-2(T-s)\mathsf K_0}
       (\mathsf K_{\theta(s)}-\mathsf K_0)r(s)\,ds.
\tag{H12}
\]

Both residual norms are at most $\|r_0\|_p\le B_0$. Equations (H11)–(H12)
give the explicit finite-time bounds

\[
\|D(T)\|_p\le B_0C_KT^2,\qquad
|\mathcal E_\nu(F_{\rm fr}(T))-\mathcal E_\nu(P_\nu(T))|
 \le2B_0^2C_KT^2,\quad 0\le T\le T_c.
\tag{H13}
\]

The exact signed quantity is

\[
\Delta(T)=2\langle r(T),D(T)\rangle_p+\|D(T)\|_p^2.
\tag{H14}
\]

Likewise the exact normalized band advantage is

\[
L_j(P_\nu(T))-L_j(F_{\rm fr}(T))
=\frac{2a_j(T)\langle D(T),e_j\rangle_p+\langle D(T),e_j\rangle_p^2}{b_j^2}.
\tag{H15}
\]

Equations (H12), (H14), and (H15) retain every interaction and finite-time
term. Their signs are unresolved. The positive energy identity for each
learner cannot compare two different kernels on two different residuals.

For scale comparison, $r_0\in E_5$, with C.4.10.3's finite conditioning
$\lambda_5>0$. Since $\|\mathsf K_0\|\le L_0^2$,
$\|r_{\rm fr}(s)-r_0\|\le2L_0^2s\|r_0\|$. It follows that

\[
\|\mathcal T_0r_{\rm fr}(s)\|
\ge(\sqrt{\lambda_5}-2L_0^3s)\|r_0\|.
\]

If $T\le\sqrt{\lambda_5}/(4L_0^3)$, integration of its energy identity yields

\[
\mathcal E(F_*)-\mathcal E(F_{\rm fr}(T))\ge\lambda_5e_0T,
\qquad
\frac{|\Delta(T)|}{\mathcal E(F_*)-\mathcal E(F_{\rm fr}(T))}
\le\frac{2B_0^2C_KT}{\lambda_5e_0}.
\tag{H16}
\]

Thus a very-short-time comparison is of higher order than total learning.
This does not bound the ratio away from zero at an acceptable finite stop.
The source constants and $\lambda_5$ have no evaluated useful conditioning
here; the reference source proof itself contains $e^{2880}$. Nothing in
(H13) or (H16) certifies the requested positive $a$.

## 5. Why symmetry and nonproportionality do not determine the sign

This subsection concerns auxiliary bounded-operator flows only. It is not an
alternative model offered as a solution of the neural contract.

Take $p=1$, $q=q_0+a(\psi_1+\psi_{11})$, and put
$\psi=\psi_1+\psi_{11}$. This is an ordinary fixed member of (H6). Let

\[
c=\langle\psi,\mathsf K_0\psi\rangle>0,\quad b=\mathsf K_0\psi,
\quad \mathsf Bf=b\langle b,f\rangle/c.
\]

Cauchy–Schwarz applied to $\mathcal T_0 f,\mathcal T_0\psi$ proves
$0\le\mathsf B\le\mathsf K_0$. This rank-one operator is nonzero, has
continuous odd kernel, commutes with the swap, and vanishes at both anchors.
It is not proportional to $\mathsf K_0$, which is injective on the
infinite-dimensional odd space. Both paths

\[
\mathsf K_s^\pm=\mathsf K_0\pm s\mathsf B,\qquad 0\le s\le1,
\tag{H17}
\]

are positive, anchor preserving, symmetry respecting, and nonproportional.
Let $r_\pm'=-2\mathsf K_s^\pm r_\pm$, $r_\pm(0)=r_0$. Their solutions
exist on this interval by uniform Picard convergence for a bounded continuous
linear coefficient; their residual norms contract by positivity.

Set $M=\|\mathsf K_0\|$, $N=\|\mathsf B\|\le M$, $E_0=\|r_0\|^2$,
and $b_r=\langle r_0,\mathsf B r_0\rangle$. The antisymmetric part of
$r_0$ is orthogonal to $\mathsf K_0\psi$, so
$\langle r_0,b\rangle=-ac$ and $b_r=a^2c>0$.

Apply (H12) with $\mathsf K_s^\pm-\mathsf K_0=\pm s\mathsf B$.
The elementary bounds

\[
\|e^{-2t\mathsf K_0}-I\|\le2Mt,\quad
\|r_\pm(s)-r_0\|\le4Ms\sqrt{E_0}
\]

give

\[
D_\pm(T)=\pm T^2\mathsf B r_0+R_\pm(T),\qquad
\|R_\pm(T)\|\le(10/3)MN\sqrt{E_0}T^3.
\]

To check the constant, the two errors inside (H12) integrate to
$4MN\sqrt{E_0}\int_0^T s(T-s)ds$ and
$8MN\sqrt{E_0}\int_0^T s^2ds$, respectively. Also
$\|D_\pm(T)\|\le N\sqrt{E_0}T^2$. Substitution into (H14), using
$N\le M$ and $T\le1$, proves

\[
\left|\{\|r_{\rm fr}(T)\|^2-\|r_\pm(T)\|^2\}
             \mp2b_rT^2\right|\le16MNE_0T^3.
\tag{H18}
\]

Therefore at any
$0<T\le\min\{1,b_r/(16MNE_0)\}$, the plus path beats the frozen
flow by at least $b_rT^2$, while the minus path loses by at least that
amount. This is a finite-time sign result with an explicit remainder, not a
formal jet. It rejects a symmetry/positivity/nonproportionality-only proof.
Whether the actual neural kernel moves in a favorable direction remains an
additional dynamical question.

A scalar path $\mathsf K_s=c(s)\mathsf K_0$ gives exactly
$r(s)=e^{-2\mathsf K_0\int_0^sc(v)dv}r_0$. Even such a scalar change can
alter finite-time relative recovered fractions when different directions have
different frozen rates. Thus a change in (H9) alone would not identify feature
reweighting. One scalar-invariant supplementary diagnostic is the two-band
matrix $M_{ij}(s)=\langle e_i,\mathsf K_se_j\rangle_p$, normalized by
its trace where that trace is positive. Positivity holds initially and on a
short interval by continuity. Its nonconstancy still would not establish benefit; (H14)
and (H15), or equivalent finite-time estimates, would remain necessary.

## 6. Matched sampling: a conditional transfer, not a missing sign proof

The following closes a downstream issue if a uniform population gap is proved.
It uses the same iid input/noisy-label observations for both empirical learners.
It introduces no independent sample advantage and no finite frozen realization.

Realize the infinite frozen predictor by raw displacement $z$:

\[
z'=-2\int(F_*(u)+\langle d_0(u),z\rangle-y)d_0(u)d\nu,
\qquad F_{\rm fr}=F_*+\langle d_0,z\rangle,\quad z(0)=0.
\]

This bounded affine Hilbert equation gives exactly the frozen prediction
equation. The empirical version uses the common observations. Its homogeneous
operator is positive, so its forced comparison propagator contracts. Evaluate
the random force only on the deterministic population frozen path. Independence,
centering and the energy bound give input and noise variances at most
$L_0^2B_0^2/m$, $L_0^2\sigma^2/m$. Cauchy–Schwarz in time followed by
Markov gives, with failure at most $\delta_I+\delta_\xi$,

\[
\sup_{s\le T}\|F_{{\rm fr},\widehat\nu_m}(s)-F_{{\rm fr},\nu}(s)\|_\infty
\le e_F(m):=\frac{2TL_0^2}{\sqrt m}
 (B_0/\sqrt{\delta_I}+\sigma/\sqrt{\delta_\xi}).
\tag{H19}
\]

The nonlinear source theorem gives on its own event
$e_N(m)=L\mathcal O_T(C_N/\sqrt m)$, with
$C_N=2TL(B_0/\sqrt{\delta_I}+\sigma/\sqrt{\delta_\xi})$.
This is C.4.10.4 NGL8–13, applied to the same observations. A union bound
needs no independence between the two empirical learners.

If a uniform population gap $a_0>0$ at a common $T\le T_c$ were known,
their empirical population-risk gap would be at least

\[
a_0-2(c_b+1)e_N(m)-2B_0e_F(m)-e_F(m)^2.
\tag{H20}
\]

For an explicit conditional threshold, take $\delta_I=\delta_\xi=\delta/4$
for each learner when $\sigma>0$; when $\sigma=0$, omit noise terms and
use input allowance $\delta/2$ for each. Define

\[
d_*=\min\{1/2,a_0/[8(c_b+1)L]\},\quad
\eta_*=e\exp[-(\sqrt{\log(e/d_*)}+\mathcal KT/2)^2],
\]
\[
e_*=\min\{1,a_0/[4(2B_0+1)]\},\quad
C_F=2TL_0^2(B_0/\sqrt{\delta_I}+\sigma/\sqrt{\delta_\xi}),
\]
\[
m\ge\max\{1,\lceil(C_N/\eta_*)^2\rceil,
                     \lceil(C_F/e_*)^2\rceil\}.
\tag{H21}
\]

Then (H20) is at least $a_0/2$ with probability at least $1-\delta$.
The branch condition for $\mathcal O_T$ holds because $d_*\le1/2$.
The known nonlinear bridge transfers its empirical learner width first at
fixed contamination and sample, then contamination second; increasing sample
size is separate and last. Any actual finite-network implementation of the
frozen comparator still requires its own approximation theorem. Equation
(H21) cannot be instantiated with a positive $a_0$ from this route.

## 7. Precise bottleneck and adversarial disposition

The unresolved implication is a uniform positive lower bound for (H14),
together with a beneficial fixed relative-band comparison such as (H15), on
the already specified family (H6), density neighborhood and common finite stop.
The needed input is a **signed actual-neural estimate** for the kernel-change
integral in (H12), with control of its correlation with the evolving residual.
An unsigned modulus, endpoint injectivity, kernel nonproportionality, or
second-hidden motion does not supply that estimate.

| Claim | Result and scope |
|---|---|
| Ordinary harmonic diagonalization of the full frozen baseline | Refuted by the two-anchor argument, for every positive odd frequency. |
| Exact sector decomposition at the reference | Proved for swap-invariant density; two sectors, each with infinitely many ordinary frequencies. |
| Several independently active ordinary target components | Proved for (H6), including target and density radii and a common-metric normalization. |
| Actual nonlinear–frozen finite-time comparison identity | Exact on the established reached episode; unsigned $O(T^2)$ bound proved. |
| Symmetry/PSD/nonproportional movement guarantees benefit | Refuted for auxiliary kernel flows by (H17)–(H18); no neural no-go follows. |
| Positive uniform actual-neural risk advantage | Open. |
| Beneficial relative learning of the fixed task bands | Open. |
| Matched-sample retention of an already proved margin | Conditional derivation (H19)–(H21). |
| Actual finite frozen realization | Not proved or assumed. |

The strongest surviving mundane explanation is scalar speed change; even a
relative component recovery change must be interpreted against it. The
strongest structural problem for this route is the unrestricted interaction
within the same swap sector, already present in the frozen baseline. The
family has not been shown to fail, and general E₀ has not been shown false.
Reopen this route only with a new signed estimate from the actual constrained
neural equations, or another genuinely dynamical invariant. Merely expanding
the Fourier cap or recomputing unsigned regularity does not address the gap.

## 8. Read coverage, checks and source versions

The scoped assignment replaced author startup. I read the complete neutral
contract, notation contract, both required skills, all three listed skill
references, and shared workflow. Scientific reads were only the permitted
established files. The supervisor subsequently authorized III.F as an added
dependency; I read that section in full. No cross-route material was read.

Actual line coverage in the frozen 17,016-line `docs/global_nonlinear.md`:

- 1840–1898: A.1–A.4, complete.
- 5475–5782: C.4.5.1 §§1–3, complete.
- 5999–6103: C.4.5.1 §5 rational Gaussian certificate, complete.
- 6104–6521: C.4.5.2 §§1–4, complete.
- 12994–13183: C.4.9 model, theorem and architecture, complete.
- 13184–13955: C.4.9 proof unit A including supplement, complete.
- 13956–14335: C.4.9 proof unit B through B.4, complete for those units.
- 15324–17016: C.4.10, complete.

Actual `docs/special_data_limits.md` coverage: 3785–4326, III.F in full.
The C.4.9 B.5/C/D remainder, unrelated scientific sections and other studies
were not read. For bounded-law continuation and finite capture the full
C.4.10 proof is the used source, rather than claiming a complete fresh audit of
all C.4.9. The primitive Gaussian-program and action dependencies, raw metric,
strong curve derivatives, source control, reference symmetries, signed-measure
separation and finite conditioning were checked against the read bodies.
This remains a scoped author check, not independent promotion review.

Checks performed: direct raw-isometry substitution; anchor evaluation for each
odd frequency; exact trigonometric support/norm calculation; Cauchy–Schwarz
for the density and component-conditioning bounds; reached-curve projector
product rule; variation of constants and explicit integral remainder estimates;
conditional variance/Markov/union-bound sampling calculation. No numerical
training, theorem prover, or new empirical reproduction was performed. The
source's rational Gaussian program was read, not reexecuted.

SHA-256 versions:

| Input | SHA-256 |
|---|---|
| `RESEARCH_CONTRACT.md` | `0bbd681da93a44574fbe30d9ee7fd5a984105d363c473c7756f31964c2896c0f` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/global_nonlinear.md` | `5c7f4cd85eebe73f497ff91cca4f3c525f158727c28b8a187a09add94e756483` |
| `docs/special_data_limits.md` | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |
| `RESEARCH_WORKFLOW.md` | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
| solve-math-rigorously skill | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| investigate-conjectures skill | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| research-contract reference | `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` |
| adversarial-audit reference | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |
| proof-search-orchestration reference | `6f288341eb90f9618ab9fa6fc8c37225f41230de6a40285761c17cc257edecdd` |

All quantities called proved above are exact deductions within their expressly
stated scope. The full E₀ theorem and its required positive/relative margins
are not proved, internally checked, or promoted by this document.
