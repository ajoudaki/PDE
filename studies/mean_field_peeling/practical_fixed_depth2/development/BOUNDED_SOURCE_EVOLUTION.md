# Bounded activation: exact source evolution and the remaining tail term

2026-09-08. This note concerns a **distinct fixed activation**,

\[
\phi(z)=1+\tanh z.
\tag{B1}
\]

It does not establish the contract for the principal affine-growth mixture. It uses only the canonical setup in `CONTRACT.md` and the fixed Gaussian operators and multiplier estimates in `GAUSSIAN_OPERATOR_ROUTE.md`. No experiment or new cap-existence argument is used.

**Conclusion.** Bounded activation makes the readout and learned kernel pointwise bounded on compact physical time intervals, justifies differentiation of the full reverse field, and yields a bounded linear evolution equation for that field. The actual initialization gives a bounded returned part and a Gaussian primitive part in its first nonzero time derivative. These facts do not yet give a compact-time source-tail theorem. A Gaussian-compression term in a comparison can be removed by integration by parts, including its potentially concentrating Hilbert--Schmidt part. The remaining strong-uniqueness term is explicitly

\[
[\phi'(z_i)-\phi'(\widetilde z_i)]\,\widetilde\beta_i,
\qquad \beta_i=F^*[C\phi'(v_i)].
\tag{B2}
\]

A uniform subexponential moment bound for these *physically generated* returned coefficients would close an Osgood strong-uniqueness estimate. Neither the bounded linear reverse-field evolution nor its actual initial derivative proves that bound.

## 1. Exact setting and compact-time bounds

Use the probability spaces and genuine operators

\[
A=A_0+U=F+R^*+U,\qquad A^*=F^*+R+U^*.
\]

The functions \(Fh\) and \(Rb\) are centered Gaussian with variances \(\|h\|_2^2\) and \(\|b\|_2^2\). They need not be independent of adapted multipliers. Initially \(U=C=0\), and \(z_i(0)\) are the required Gaussian input fields. All three blocks follow the original simultaneous raw gradient flow.

For clarity use constants

\[
|\phi|\le B,\quad |\phi'|\le L,\quad
|\phi''|\le M,\quad |\phi'''|\le J.
\]

For (B1), \((B,L,M,J)=(2,1,2,2)\) are valid bounds. The third derivative is used only in the integration-by-parts audit in Section 4; the basic bounded-field and first-source statements require only the first two derivative bounds.

Write

\[
\lambda(t)=\sum_i|r_i(t)|,\qquad
\Lambda(t)=\int_0^t\lambda(s)\,ds.
\]

Physical loss dissipation gives \(\|r(t)\|_2\le\|y\|_2\), so \(\Lambda(T)\le\sqrt3\|y\|_2T\). Directly from the equations, pointwise almost everywhere,

\[
|C(t)|\le B\Lambda(t),\qquad |b_i(t)|\le LB\Lambda(t).
\tag{B3}
\]

The learned operator has the actual integral kernel

\[
u_t(\omega_2,\omega_1)
=-\int_0^t\sum_i r_i(s)b_i(s,\omega_2)h_i(s,\omega_1)\,ds,
\]

and hence

\[
\|u_t\|_\infty\le\frac12 LB^2\Lambda(t)^2.
\tag{B4}
\]

In particular both \(U:H_1\to L^\infty(\Omega_2)\) and \(U^*:H_2\to L^\infty(\Omega_1)\) have norms at most \(\|u_t\|_\infty\). These are physical-path bounds. They apply to a strong competitor with this initialization as well: the strong integral equations for \(C,U\) give the displayed bounded representatives.

Since \(\|A_0\|\le2\), these bounds control \(q_i=A^*b_i\) in \(L^2\), and all raw velocities and the velocities of \(h,v\) in their respective \(L^2\) spaces, by constants depending only on \(T,B,L,M,y\). In what follows \(K_T\) denotes a finite such constant and may increase from line to line.

The bounded \(C\) is significant: the chain rule now really gives an \(L^2\) derivative

\[
\dot b_i=\dot C\phi'(v_i)+C\phi''(v_i)\dot v_i.
\tag{B5}
\]

This derivative was not justified by an \(L^2\) readout bound alone in the affine-growth variant.

## 2. The bounded linear equation is exact, but is not a tail estimate

Define

\[
m_{ij}=\phi'(z_i)\phi'(z_j),\qquad g_i=C\phi''(v_i),
\]

\[
s_i=\dot C\phi'(v_i)+g_i\dot U h_i.
\]

Then

\[
\dot h_i=-\sum_j\Gamma_{ij}r_jM_{m_{ij}}q_j,
\qquad
\dot q_i=\dot U^*b_i+A^*s_i+A^*M_{g_i}A\dot h_i.
\tag{B6}
\]

Equivalently,

\[
\dot q_i=\dot U^*b_i+A^*s_i
-\sum_j\Gamma_{ij}r_jA^*M_{g_i}AM_{m_{ij}}q_j,
\qquad q_i(0)=0.
\tag{B7}
\]

Every displayed operator is bounded on the relevant \(L^2\) space, uniformly on \([0,T]\). Also \(s_i\) is pointwise bounded. More explicitly, with \(H_{li}=\langle h_l,h_i\rangle\),

\[
s_i=-\sum_l r_l\left[
\phi(v_l)\phi'(v_i)
+C^2\phi''(v_i)\phi'(v_l)H_{li}\right].
\tag{B8}
\]

Thus (B7), along any specified physical trajectory, has a bounded evolution operator and a convergent ordinary \(L^2\) Dyson expansion. Its coefficients are still determined simultaneously by the unknown physical path. A bounded \(L^2\) propagator need not preserve square-tail uniform integrability, and its forcing contains \(F^*s_i\). In particular one cannot replace the desired physical source estimate by a claim that \(F^*\), or \(A_0^*\), maps arbitrary bounded inputs into an \(L^2\) family with uniformly integrable squared tails.

## 3. What the actual initialization proves

Put \(h_i^0=\phi(z_i(0))\). The initial Gaussian root is independent of the reverse source group, so

\[
R^*h_i^0=0,\qquad V_i=v_i(0)=Fh_i^0.
\]

Since \(C=U=q=0\) at time zero,

\[
\dot z_i(0)=\dot h_i(0)=\dot U(0)=\dot v_i(0)=0,
\qquad \dot C(0)=\sum_l y_l\phi(V_l).
\]

Consequently

\[
\dot q_i(0)=R a_i+F^*a_i,
\qquad
a_i=\left[\sum_l y_l\phi(V_l)\right]\phi'(V_i).
\tag{B9}
\]

The second term has an explicit bounded representative. Gaussian integration by parts in the finite vector \(V\), valid also for singular covariance, gives

\[
\begin{split}
F^*a_i={}&\sum_k y_k
E[\phi'(V_k)\phi'(V_i)]h_k^0\\
&+E\!\left[\left(\sum_l y_l\phi(V_l)\right)\phi''(V_i)\right]h_i^0.
\end{split}
\tag{B10}
\]

For completeness, represent \(V\) as a linear image of independent standard Gaussians and apply one-dimensional Gaussian integration by parts. Testing the resulting identity against any \(u\in H_1\) uses \(E[(Fu)V_k]=\langle u,h_k^0\rangle\), which proves (B10) in \(H_1\).

It follows that

\[
\|F^*a_i\|_\infty
\le B\|y\|_1(L^2+BM),
\qquad
\|a_i\|_2\le BL\|y\|_1.
\tag{B11}
\]

Thus the first nonzero physical reverse derivative is a centered Gaussian plus a bounded function; no independence between those two summands is asserted or needed. In particular it has a dimension-free subGaussian moment bound. This establishes a true initial source seed, not its propagation to positive time.

Even a common initial seed and any fixed number of matching time derivatives cannot replace the physical propagation argument. To see the precise weakness of that substitute, choose unit vectors \(e_n\) supported on events of probabilities tending to zero, and put \(Z_n=Fe_n\). For any fixed integer \(k\ge2\), the bounded top paths

\[
b_{i,n}(t)=t a_i+t^k\tanh Z_n
\]

have common derivatives through order \(k-1\) at zero and uniform bounds on every fixed-order time derivative on \([0,T]\). Nevertheless

\[
F^*b_{i,n}(t)=tF^*a_i+t^k\kappa e_n,
\qquad \kappa=E[Z\tanh Z]>0.
\tag{B12}
\]

Their squared tails fail uniform integrability for each \(t>0\). These paths are **not** claimed to satisfy the physical equations. This only rules out deducing tail propagation from bounded coefficients, time smoothness, and a finite initialization jet. It does not refute the physical conjecture.

## 4. A nontrivial cancellation in the operator-evolution comparison

The returned part \(\beta_i=F^*b_i\) obeys

\[
\dot\beta_i=F^*s_i+T_{g_i}\dot h_i
+F^*M_{g_i}(R^*+U)\dot h_i,
\qquad T_g=F^*M_gF=(Eg)I+K_g.
\tag{B13}
\]

The bounded third derivative in (B1) gives

\[
\dot g_i=\dot C\phi''(v_i)+C\phi'''(v_i)\dot v_i\in L^2,
\qquad \|\dot g_i\|_2\le K_T.
\tag{B14}
\]

The Gaussian compression estimate therefore makes \(T_{g_i(t)}\) absolutely continuous in operator norm, with

\[
\|\dot T_{g_i}\|\le(1+\sqrt2)\|\dot g_i\|_2.
\tag{B15}
\]

Here \(\dot T_g\) is the bounded Gaussian compression **form** furnished by the \(L^2\) estimate. It is not an assertion that multiplication by the possibly unbounded \(\dot g\) defines the usual \(L^2\) composition \(F^*M_{\dot g}F\).

For two strong paths, write \(\Delta h=h-\widetilde h\) and similarly for other quantities. Exactly,

\[
\begin{split}
\int_0^t(T_g\dot h-T_{\widetilde g}\dot{\widetilde h})\,ds
={}&T_g(t)\Delta h(t)-T_g(0)\Delta h(0)\\
&-\int_0^t\dot T_g\Delta h\,ds
+\int_0^t(T_g-T_{\widetilde g})\dot{\widetilde h}\,ds.
\end{split}
\tag{B16}
\]

Hence this entire term, including its Hilbert--Schmidt part, is bounded by

\[
K_T\left(\|\Delta h(t)\|_2+\|\Delta h(0)\|_2
+\int_0^t[\|\Delta h\|_2+\|\Delta g\|_2]\,ds\right).
\tag{B17}
\]

This avoids estimating the problematic product \((m-\widetilde m)\widetilde q\) inside the compressed term.

In the last term of (B13), the same product is controllable after the reverse projection or the bounded learned kernel. The estimates are

\[
\|R^*M_d\widetilde q\|_2
\le\omega_K(\|d\|_2)\|\widetilde q\|_2,
\qquad
\|UM_d\widetilde q\|_2
\le\|u\|_\infty\|d\|_2\|\widetilde q\|_2,
\tag{B18}
\]

for bounded \(d\), with \(\omega_K(s)=4s\sqrt{\log(eK/s)}\) on its stated domain. Changes of the outgoing multiplier are also controlled:

\[
\|F^*M_{g-\widetilde g}(R^*+U)\dot{\widetilde h}\|_2
\le\omega_K(\|g-\widetilde g\|_2)
\|(R^*+U)\dot{\widetilde h}\|_2.
\tag{B19}
\]

Thus no unprojected source-tail hypothesis is needed to compare the integrated equation (B13). This is an audit of a legitimate cancellation, not a new strong-uniqueness theorem: in the bounded-activation case the simpler identity \(\beta=F^*[C\phi'(v)]\) already makes \(\beta\) ordinarily \(L^2\)-Lipschitz in bounded primal states. The unprojected first-layer equation still remains.

## 5. The exact remaining strong-comparison term

The actual reverse field splits as

\[
q_i=Rb_i+\beta_i+U^*b_i.
\tag{B20}
\]

The first term is Gaussian with uniformly bounded variance and the last term is uniformly bounded. The possible concentrating component is \(\beta_i\).

Let

\[
D=\|w-\widetilde w\|_2+\|U-\widetilde U\|_{\rm HS}
+\|C-\widetilde C\|_2.
\]

The bounds in Section 1 and bounded first and second derivatives imply

\[
\|\Delta h_i\|_2+\|\Delta v_i\|_2+\|\Delta b_i\|_2
+\|\Delta q_i\|_2+|\Delta r_i|\le K_TD.
\tag{B21}
\]

The readout and learned-operator velocity differences also have ordinary \(K_TD\) bounds. In the first-layer velocity difference, use

\[
\phi'(z_i)q_i-\phi'(\widetilde z_i)\widetilde q_i
=\phi'(z_i)\Delta q_i
+[\phi'(z_i)-\phi'(\widetilde z_i)]\widetilde q_i.
\]

Applying (B20) to the last product, the Gaussian multiplier lemma controls its \(R\widetilde b_i\) part, and boundedness controls its \(\widetilde U^*\widetilde b_i\) part. The only term without a closed modulus is exactly (B2). Thus, for identical initial states,

\[
D(t)\le K_T\int_0^t\left[D(s)+\omega_{K_T}(K_TD(s))
+\sum_i\|[\phi'(z_i)-\phi'(\widetilde z_i)]\widetilde\beta_i\|_2\right]ds,
\tag{B22}
\]

with the harmless large-argument extension of the modulus understood. Projection of (B2) would change the quantity required by the unprojected raw flow.

For a family of physically reached returned coefficients define

\[
\eta_T(Q)=\sup_{\text{paths},\,t\le T,\,i}
\|\beta_i(t)1_{|\beta_i(t)|>Q}\|_2.
\tag{B23}
\]

The exact truncation estimate is

\[
\|[\phi'(z_i)-\phi'(\widetilde z_i)]\widetilde\beta_i\|_2
\le MQ\|z_i-\widetilde z_i\|_2+2L\eta_T(Q).
\tag{B24}
\]

An \(L^2\) bound alone gives no decay of \(\eta_T(Q)\). Even uniform integrability, if separately proved, need not make the optimized modulus in (B24) Osgood; its rate matters for this particular uniqueness argument.

## 6. A sufficient physical moment estimate, with the uniqueness implication proved

Here is a concrete remaining source statement weaker than a subGaussian bound:

\[
\sup_{t\le T,i}\|\beta_i(t)\|_{L^p}\le K_Tp
\quad\text{for every }p\ge2.
\tag{B25}
\]

For approximation convergence the supremum must additionally be uniform over the actual approximation family. For the following uniqueness statement it is enough that one of two strong paths satisfies (B25).

**Conditional uniqueness proposition.** Two bounded-primal strong solutions of the original population raw flow, with activation (B1), the canonical fixed \(A_0\), and identical initialized data, coincide on \([0,T]\) if the returned coefficients of one solution satisfy (B25).

**Proof.** Let \(d=\phi'(z_i)-\phi'(\widetilde z_i)\), \(s=\|d\|_2\), and \(\|d\|_\infty\le2L\). For every \(p\ge2\), Hölder's inequality and interpolation give

\[
\|d\widetilde\beta_i\|_2
\le\|\widetilde\beta_i\|_{2p}\|d\|_{2p/(p-1)}
\le2K_Tp(2L)^{1/p}s^{1-1/p}.
\]

Taking \(p=\max\{2,\log(2L/s)\}\) when \(0<s\le2L\) yields

\[
\|d\widetilde\beta_i\|_2
\le K_T' s\log(eK_T'/s).
\tag{B26}
\]

Since \(s\le M\|\Delta z_i\|_2\le MD\), (B22) is bounded by the corresponding logarithmic modulus. To spell out the zero-initial-data step, for small \(\varepsilon>0\) let

\[
a_\varepsilon(t)=\varepsilon+K\int_0^t\rho(D(s))\,ds,
\qquad \rho(x)=x\log(eK/x)
\]

on a small interval where this increasing modulus applies. Then \(D\le a_\varepsilon\) and \(a_\varepsilon'\le K\rho(a_\varepsilon)\). Integrating gives

\[
\int_\varepsilon^{a_\varepsilon(t)}\frac{du}{\rho(u)}\le Kt.
\]

The integral from zero to any positive value is infinite, because the substitution \(v=\log(eK/u)\) produces \(\int^\infty dv/v\). Letting \(\varepsilon\downarrow0\) forces \(D(t)=0\). Continuing the same argument along the compact interval proves equality throughout. All competitors inherit (B3)--(B4), so the estimates did not assume an additional pointwise bound for the second competitor. ∎

This proposition is a conditional bridge. It does not prove (B25), finite-width convergence, cap removal, or the full GF/GD and kernel-law contract.

## 7. Claim ledger and exact outstanding task

| Statement | Status |
|---|---|
| Compact-time pointwise bounds for the physical readout and learned kernel | Proved directly from the bounded activation and original raw flow |
| Strong differentiation of \(b,q\) and bounded \(L^2\) operator equation (B7) | Proved for an existing strong physical path |
| Gaussian-plus-bounded first nonzero reverse derivative at the actual initialization | Proved by (B9)--(B11) |
| Integrated cancellation of the entire Gaussian compression term | Proved by (B13)--(B19) |
| Strong uniqueness assuming the physical returned-source moment estimate (B25) for one path | Proved conditionally |
| Preservation of physical returned-source tails or (B25) on every compact interval | Open |
| Convergent causal Gaussian-polynomial approximation of the nonlinear physical coefficients | Open; the bounded linear Dyson expansion alone does not establish it |
| Main affine-growth activation or full finite-algorithm bridge | Not resolved by this note |

The next necessary advance in this route must exploit simultaneous physical coefficient generation to control \(F^*[C\phi'(v)]\) in (B23) or directly bound (B2). Arbitrarily prescribed bounded gates and common initial time jets cannot supply that information. The compression cancellation identifies a genuine removable term, but the final unprojected multiplier on the returned source remains an explicit unresolved term.
