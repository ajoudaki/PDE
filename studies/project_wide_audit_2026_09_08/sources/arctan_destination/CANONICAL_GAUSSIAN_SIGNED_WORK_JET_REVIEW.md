# Independent complete audit of the canonical fifth-coefficient lemma

**Verdict: PASS at the exact input hashes below. No required corrections remain.** The complete zero-readout argument and the finalized tiny-readout transfer establish \(J_n^{\rm can}\to J_*>0\) in probability. The transfer uses its explicit pure-program closure and Tensor Programs III v3, Theorem 2.10. No Appendix E theorem is a premise of this verdict.

This audit covers the complete combined lemma, both proof dependencies, the three permitted primitive dependencies, and the actual versioned primary theorem. The six local mathematical inputs were read completely. The needed dependency statements were checked by derivation, not accepted from status labels or another review. No other reviews, ledgers, agent history, source agents, experiments, or merely referenced local files were consulted. Inputs were not edited. The original zero-readout review remains a separate, unchanged output; it is not substituted for the mathematical checks below.

## 1. Exact reviewed inputs and scope

The local mathematical inputs are in /tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/.

| Input | SHA256 |
| --- | --- |
| CANONICAL_GAUSSIAN_SIGNED_WORK_JET.md | 8b0c1bbc9e8133b0585bbdee17945ae12088e603c46d20c9056cfb178b7e01a8 |
| TINY_READOUT_SIGNED_JET_TRANSFER.md | 518d8d870ccec8a76a29812fcac43b514fcd4e3a6c24a25b2bc1202b070f75ad |
| GAUSSIAN_SIGNED_PRIMITIVE_WORK_JET.md | 4f982b4f23204186c484f014a9c064480f93709e1d7001942886b0ad9511c6f3 |
| ACTUAL_BACKPROP_PRIMITIVE_RESPONSE.md | 067e1bc7d38c7409dab9639f29f84543abd2d0b7a9b9d543f9a47a6747e54d1e |
| ACTUAL_PRIMITIVE_OFFDIAGONAL_PAIR.md | f7f1b24a4f53cacdf0f86258eafb9b4ae86473b894d70fc9346af0726697df04 |
| ACTUAL_LOG_GATE_COVARIANCE_COMMUTATOR.md | 5770d934df3840184d0b19bc3a15eae82290cc879201fe862786ba56d24c6c76 |
| Tensor Programs III: Neural Matrix Laws, arXiv:2009.10685v3, PDF bytes | 6b0d6504c12373e6837de0aff5ab77bb18675a225fcda10d59b56540ec74b5da |

Primary source: [Greg Yang, Tensor Programs III, v3](https://arxiv.org/pdf/2009.10685v3), Definition 2.1, Setup 2.2, Box 1 and Theorem 2.10 with its footnote 15, printed pp. 6–9. The downloaded, hashed PDF is /tmp/canonical-signed-work-primary-NK0DUZ/2009.10685v3.pdf.

All seven input hashes were rechecked after report creation and still match this table. The separate zero-readout review retained SHA256 d73c4fc9574a1fbc50e1ac1ea3484dd538e59d6ec4ff12041d312aa3ddc29f6d.

The transfer's provenance section mentions additional local context. None is needed here: its initial laws and finite equations are explicit, agree with the combined statement and the permitted primitive notes, and are sufficient for the argument below. In particular, no fixed-mesh, clipping, continuation, or bounded-readout event theorem is imported from those references.

## 2. Same actual dynamics, primitive, and normalization throughout

Use the candidate's canonical notation, with \(\phi=\arctan\), \(D^{(\ell)}=\operatorname{diag}\phi'(z^{(\ell)})\), \(h^{(\ell)}=\phi(z^{(\ell)})\), and \(w=W^{(4)}\). All vector norms and transposes below are ordinary, with factors \(1/n\) explicit. Put
\[
F(z)=z+z^3/3,\qquad x^{(1)}=F(z^{(1)}).
\]
Since \(F'=1/\phi'>0\), the transfer equations
\[
(x^{(1)})'=(W^{(2)})^T\delta^{(2)},\quad
(W^{(2)})'=\delta^{(2)}(h^{(1)})^T/n,\quad
(W^{(3)})'=\delta^{(3)}(h^{(2)})^T/n,\quad w'=h^{(3)}
\]
give \((z^{(1)})'=D^{(1)}(W^{(2)})^T\delta^{(2)}\) and
\[
(z^{(2)})'=(m_1I+K)\delta^{(2)},\qquad
m_1=\|h^{(1)}\|_2^2/n,\quad
K=W^{(2)}(D^{(1)})^2(W^{(2)})^T.                    \tag{C1}
\]
These are exactly the first-layer and matrix-training contributions in the primitive dependencies. The rescaling does not change the initialization: \(x^{(1)}_0=F(z^{(1)}_0)\) with standard Gaussian \(z^{(1)}_0\), and \(w_0=\rho G_4\); \(\rho=1/n\) gives the required variance \(n^{-2}\).

For a probe, set \(p=\operatorname{var}\delta^{(2)}\), \(u=\operatorname{var}q^{(2)}\), \(\zeta=\operatorname{var}z^{(2)}\), and \(a' =p\), \(a(0)=0\). Direct differentiation gives
\[
p=D^{(2)}u+\phi''(z^{(2)})\odot q^{(2)}\odot\zeta,\qquad
c'=u+\beta(z^{(2)})\odot(q^{(2)}\odot\zeta-(z^{(2)})'\odot c),
\quad c=(D^{(2)})^{-1}a.                             \tag{C2}
\]
Thus both notes and the wrapper use the same full signed contribution to the derivative of \((2n)^{-1}\sum_i\mathbb E_\xi\|c_i\|_2^2\), excluding precisely the ordinary source term.

The exact primitive representation is also justified from the lower tangent equations:
\[
(\widehat x^{(1)})'=A^T\delta^{(2)}+(W^{(2)})^Tp,\quad
A'=p(h^{(1)})^T/n+\delta^{(2)}(\widehat h^{(1)})^T/n,\quad
\widehat h^{(1)}=(D^{(1)})^2\widehat x^{(1)}.
\]
In the first dependency, its operator \(L_0\) has autonomous lower components and its direct forcing is purely upper. Its response maps obey \(TR=m_1I+K\). Integration by parts in variation of constants, using \(a'=p\), yields
\[
\zeta(t)=(m_1I+K)_t a(t)+\int_0^t N_0(t,s)a(s)\,ds. \tag{C3}
\]
There is no missing direct lower response. Inserting (C3) into (C2) cancels the instantaneous \(m_1\) self-pair, while retaining memory. Symmetry of \(K\) and of \(n\mathbb E_\xi cc^T\), and \(\beta_j=-2z^{(2)}_jD^{(2)}_j\), give the off-diagonal dependency's polarized pair; its diagonal vanishes exactly. This is an identity, not a sign argument.

The log-gate dependency's needed initial covariance is derived in section 3. Its metric identities impose no isotropy premise: if \(C_0=(m_1I+K)/m_1\), \(L=\operatorname{diag}\log\phi'(z^{(2)})\), and \(J_g=LC_0L'-L'C_0L\), then \(J_g^T=-J_g\), \(Q=J_gC_0\), and \(Q^TC_0=-C_0Q\). For \(\Gamma=n\mathbb E_\xi aa^T\), the ordinary trace identity is \(\operatorname{Tr}(J_gC_0\Gamma)=\operatorname{Tr}(J_g[C_0,\Gamma])/2\); it is not set to zero. Its positive corrected metric and remaining source terms do not enter this coefficient proof.

All these finite-state identities are smooth locally. The needed probe source scale is consistent as well: for \(\Delta=\xi e_i^T/\sqrt n\), the map into the norm \(\|\cdot\|_2/\sqrt n\) satisfies \(\|\xi\mapsto\Delta h^{(2)}\|=|h^{(2)}_i|/n\), whereas \(\mathbb E_\xi\|\Delta^T\delta^{(3)}\|_2^2=\|\delta^{(3)}\|_2^2/n\). No false \(1/n\) operator bound on this latter contact term is required. Width-uniform positive-time source estimates are not premises of either finite-jet calculation.

## 3. Complete zero-readout ingredient: jet, conditional moments, concentration

In this section fields without a time argument are initial fields. At \(w_0=0\), all hidden velocities vanish. Set \(D=D^{(2)}\), \(h=h^{(2)}\), \(m=\|h\|_2^2/n\), \(\psi=\phi\phi'\), and
\[
v=(W^{(3)})^T\psi(z^{(3)}),\qquad
R_i=e_i\psi(z^{(3)})^T+h_i(W^{(3)})^T\operatorname{diag}\psi'(z^{(3)}).
\]
Because \(w'=h^{(3)}\), direct chain rules give
\[
(q^{(2)})'(0)=v,\quad(\delta^{(2)})'(0)=Dv,\quad
(z^{(2)})''(0)=(m_1I+K)Dv,\quad
\operatorname{var}_i(q^{(2)})'(0)=R_i\xi/\sqrt n.
\]
Here \(\psi'=\phi'^2+\phi\phi''\) differentiates both factors in \(D^{(3)}h^{(3)}\), including the readout response. Top training has zero initial velocity and zero variation of that velocity, so adds no omitted term at this order. Therefore
\[
c_i(s)=\frac{s^2}{2\sqrt n}R_i\xi+O_n(s^3)\|\xi\|_2,\quad
\zeta_i(s)=\frac{s^2}{2\sqrt n}(m_1I+K)DR_i\xi+O_n(s^3)\|\xi\|_2.
\]
The \(m_1D\) and \(KD\) terms account for second-matrix and first-layer training. The memory in (C3) is at least order \(s^3\). Smooth dependence gives remainders in the response operator norm; products are bounded by a finite-state constant times \(\|\xi\|_2^2\), justifying their probe averages at fixed width.

The work consequently has \(\mathscr W_n^0(s)=P_n(0)s^5+O_n(s^6)\), with
\[
P_n(0)=\frac1{4n^2}\operatorname{Tr}[\mathcal M(v)C],\quad
\mathcal M(q)=\operatorname{diag}(\beta\odot q)KD
-\operatorname{diag}(\beta\odot KDq),\quad C=\sum_iR_iR_i^T. \tag{C4}
\]
The \(1/(4n^2)\) is the product of the two \(1/(2\sqrt n)\) response factors and the column average \(1/n\). For \(n=1\), \(\mathcal M(v)=0\).

Let \(d=\psi(z^{(3)})\), \(E=\operatorname{diag}\psi'(z^{(3)})\), and \(\ell=(W^{(3)})^TEd\). Multiplication, retaining both cross terms, gives
\[
C=\|d\|_2^2I+h\ell^T+\ell h^T+nm(W^{(3)})^TE^2W^{(3)}. \tag{C5}
\]
Conditional on the whole lower initialization and \(z=z^{(3)}\), Gaussian row projection yields
\[
W^{(3)}=zh^T/(nm)+XP/\sqrt n,\quad P=I-hh^T/(nm),
\]
with standard Gaussian \(X\). Given the lower initialization alone, the \(z_j\) are independent \(N(0,m)\), and \(m>0\) almost surely. Define
\[
\bar A=\|d\|_2^2/n+m\operatorname{Tr}(E^2)/n,\quad
\bar\gamma=z^Td/(nm),\quad
\bar\lambda=(d^TEd+d^TE^2z)/n.
\]
Then \(\mathbb E_XC=n\bar A I+\bar\kappa hh^T\), \(\mathbb E_Xv=\bar\gamma h\), and
\[
\mathbb E_X[(v_j-\bar\gamma h_j)C_{kl}]
=\bar\lambda(h_kP_{jl}+P_{jk}h_l).                  \tag{C6}
\]
To check this last identity, the centered query is \(PX^Td/\sqrt n\). Its covariances with the centered \(\ell\) and with the linear part of the quadratic matrix term in (C5) are \(P(d^TEd/n)\) and \(P(d^TE^2z/n)\), respectively. The remaining linear times quadratic centered residual is odd Gaussian.

The trace in (C4) has summands \(\beta_jK_{jk}D_k(v_jC_{kj}-v_kC_{jj})\). Rank-one mean terms cancel. Using \(h_kP_{jj}-h_jP_{jk}=h_k-h_j\mathbf1_{j=k}\) gives
\[
\mathbb E_XP_n(0)=\frac{\bar\lambda-n\bar A\bar\gamma}{4n^2}S_n,
\quad S_n=\sum_{j\ne k}\beta(z^{(2)}_j)K_{jk}\psi(z^{(2)}_k). \tag{C7}
\]

For \(Z_v\sim N(0,v)\), write \(\chi_{\rm G}(v)=\mathbb E[\psi'(Z_v)\psi(Z_v)^2]\), the zero note's scalar \(\chi\). Expanding the empirical product, not multiplying its expectations, yields
\[
n\mathbb E[\bar A\bar\gamma\mid\mathrm{lower}]
=(n-1)A(m)\gamma(m)+m^{-1}\mathbb E[Z_m\psi(Z_m)^3]
+\mathbb E[Z_m\psi'(Z_m)^2\psi(Z_m)].
\]
The mean of \(\bar\lambda\) is \(\chi_{\rm G}(m)\) plus the last term. Gaussian integration by parts for bounded smooth \(\psi^3\), with vanishing boundary term, gives
\[
m^{-1}\mathbb E[Z_m\psi(Z_m)^3]=3\chi_{\rm G}(m)>0.
\]
Thus the exact difference is \(-(n-1)A(m)\gamma(m)-2\chi_{\rm G}(m)\). This verifies the product bias and its sign despite the changing pointwise sign of \(\psi'\).

Conditional now on \(z^{(1)},z^{(2)}\), the analogous row projection for \(W^{(2)}\), with independent centered residual rows, gives for \(j\ne k\)
\[
\mathbb E[K_{jk}\mid z^{(1)},z^{(2)}]
=\frac{b_{1,n}}{nm_1^2}z^{(2)}_jz^{(2)}_k,\quad
b_{1,n}=\frac1n\sum_r(h^{(1)}_r)^2(D^{(1)}_r)^2.
\]
Consequently
\[
\mathbb E[P_n(0)\mid z^{(1)},z^{(2)}]
=-\frac{[(n-1)A(m)\gamma(m)+2\chi_{\rm G}(m)]b_{1,n}}{4n^3m_1^2}
\sum_{j\ne k}[z^{(2)}_j\beta(z^{(2)}_j)][z^{(2)}_k\psi(z^{(2)}_k)]. \tag{C8}
\]
All scalar prefactors apart from the displayed minus sign are strictly positive almost surely; each summand is strictly negative. Nondegenerate conditional Gaussian coordinates are nonzero almost surely. Integrability below therefore gives \(\mathbb EP_n(0)>0\) for every \(n\ge2\).

The passage from these conditional means to the actual random coefficient is valid. For \(\bar C=C/n\), a Frobenius-unit residual variation has \(\delta W^{(3)}=\delta XP/\sqrt n\), and differentiation of (C5) gives
\[
\|\delta v\|_2\le C,\quad
\|\bar C\|_{\rm op}\le C(1+\|W^{(3)}\|_{\rm op}^2),\quad
\|\delta\bar C\|_F\le C(1+\|W^{(3)}\|_{\rm op})/\sqrt n.
\]
Bounding rows of \(K\) gives \(\|\mathcal M(q)\|_F\le C\|K\|_{\rm op}\|q\|_2\); expanding the two diagonal traces gives
\[
|\operatorname{Tr}[\mathcal M(q)\bar C]|
\le2\sqrt n\,\|K\|_{\rm op}\|\bar C\|_{\rm op}\|q\|_2.
\]
Since \(\|v\|_2\le C\sqrt n\|W^{(3)}\|_{\rm op}\), these are full directional-derivative estimates and imply
\[
\|\nabla_XP_n(0)\|_F\le
C\|K\|_{\rm op}(1+\|W^{(3)}\|_{\rm op}^2)/\sqrt n.    \tag{C9}
\]
Gaussian Poincare applies conditionally: its semigroup proof uses
\(-\partial_t\mathbb E(P_t f)^2=2\mathbb E\|\nabla P_tf\|^2\) and
\(\nabla P_tf=e^{-t}P_t\nabla f\), followed by Jensen and integration.
The conditioned function is polynomial in \(X\), so the square-integrable-gradient and cutoff hypotheses hold.

For the original Gaussian matrices, a pair of \(1/4\)-nets gives
\(\mathbb P(\|W\|_{\rm op}>x)\le2\,9^{2n}e^{-nx^2/8}\);
integration above a fixed large threshold supplies uniform moments of every fixed order. Thus averaging conditional Poincare under the original independent matrix laws gives
\[
\mathbb E|P_n(0)-\mathbb E_X[P_n(0)\mid\mathrm{lower},z^{(3)}]|^2\le C/n.
\]
The conditioned mean matrix need not have uniformly bounded norm; only its original, integrated Gaussian law is used. No inverse moment of \(m\) is assumed.

Conditional scalar averaging, localized to a fixed positive variance interval containing the limit of \(m\), and \(|S_n|/n\le C\|K\|_{\rm op}\), now yield
\[
P_n(0)=-A(m)\gamma(m)S_n/(4n)+o_{\mathbb P}(1).
\]
For the lower step write \(S_n=b^TKf-\sum_jb_jf_jK_{jj}\), \(b=\beta(z^{(2)})\), \(f=\psi(z^{(2)})\). Conditional residual differentiation in \(W^{(2)}\) bounds each bilinear gradient of \(S_n/n\) by \(C\|W^{(2)}\|_{\rm op}/\sqrt n\), and the diagonal gradient by \(C\|W^{(2)}\|_F/(n\sqrt n)\). These follow by differentiating \(K=W^{(2)}(D^{(1)})^2(W^{(2)})^T\), with residual factor \(1/\sqrt n\), bounded \(b,f,D^{(1)}\), and \(\|b\|_2,\|f\|_2=O(\sqrt n)\). Poincare therefore centers \(S_n/n\) about the conditional mean from (C8) with squared error \(O(1/n)\).

The bounded first-layer law of large numbers gives \(m_1\to\mu_1>0\), \(b_{1,n}\to b_1>0\). Given that layer, \(z^{(2)}_j\) are independent \(N(0,m_1)\). Conditional averaging gives \(m\to\mu_2>0\) and the means of the bounded functions \(z\beta(z)\), \(z\psi(z)\). Removing the diagonal of their product of sums costs \(O(1/n)\). Thus, for \(Z\sim N(0,\mu_1)\),
\[
S_n/n\to\frac{b_1}{\mu_1^2}\mathbb E[Z\beta(Z)]\mathbb E[Z\psi(Z)].
\]
All scalar variance-dependent functions are continuous, with the required compact-interval derivative bounds by Gaussian dominated differentiation. Combining proves the exact \(J_*\) in the wrapper. It is strictly positive because \(A,\gamma,b_1,\mu_1,\mu_2>0\), \(\mathbb E[Z\beta(Z)]<0\), and \(\mathbb E[Z\psi(Z)]>0\).

Finally (C4)–(C5) and the trace bound above imply
\[
|P_n(0)|\le C\|W^{(2)}\|_{\rm op}^2\|W^{(3)}\|_{\rm op}
(1+\|W^{(3)}\|_{\rm op}^2).
\]
The established operator moments give uniform \(L^2\) boundedness and hence \(L^1\) uniform integrability. Therefore \(P_n(0)\to J_*\) also in \(L^1\). This completes the zero ingredient, including its conditional laws, concentration, finite-width sign, and integrability, without transferring any of those stronger claims to tiny readout by assumption.

## 4. Transfer: full probe and exact finite degree in readout amplitude

Take \(J\) with independent \(N(0,1/n)\) entries, independent of \(\mathcal F_n=\sigma(z^{(1)}_0,W^{(2)}_0,W^{(3)}_0,G_4)\). It is the sum of independent column probes \(K_i=\xi_i e_i^T/\sqrt n\). For any two response maps \(U,V\), linear in the probe, and a base-measurable \(M\), zero conditional cross-column means give
\[
\mathbb E_J[U[J]^TMV[J]\mid\mathcal F_n]
=\sum_i\mathbb E_{\xi_i}[U[K_i]^TMV[K_i]\mid\mathcal F_n].
\]
The original \(1/n\) column average is consequently exactly
\[
\mathcal W_n^\rho(s)=\mathbb E_J\!\left[
\frac{c[J]^T}{n}\{\beta(z^{(2)})\odot(q^{(2)}\odot\zeta[J]
-(z^{(2)})'\odot c[J])\}\,\middle|\,\mathcal F_n\right]. \tag{C10}
\]
There is no extra factor of \(n\) or \(\sqrt n\). Conditional differentiation in time is differentiation of a finite-dimensional Gaussian quadratic-form trace with smooth coefficients.

All trained factors in transfer (5) follow from the product rule. Besides the lower equations checked above, the full top response is
\[
\zeta^{(3)}=(J+B)h^{(2)}+W^{(3)}D^{(2)}\zeta,\quad
\widehat\delta^{(3)}=D^{(3)}v_4+w\odot\phi''(z^{(3)})\odot\zeta^{(3)},
\]
\[
\widehat q^{(2)}=(J+B)^T\delta^{(3)}+(W^{(3)})^T\widehat\delta^{(3)},\quad
B'=\{\widehat\delta^{(3)}(h^{(2)})^T+\delta^{(3)}(\widehat h^{(2)})^T\}/n,\quad
v_4'=D^{(3)}\zeta^{(3)}.
\]
Together with (C2), this is an exact first variation with zero learned-state initial variation. No top, lower, readout, or memory response is frozen.

Write \(\Theta=(x^{(1)},W^{(2)},W^{(3)})\). The primal equations have \(\Theta'=\mathscr B(\Theta)w\), \(w'=\mathscr V(\Theta)\), with \(\Theta_0\) independent of \(\rho\), \(w_0=\rho G_4\), and smooth \(\mathscr B,\mathscr V\). A smooth function of \(\Theta\) has its \(k\)-th time coefficient as a finite sum of derivatives at \(\Theta_0\) applied to positive-order coefficients whose indices sum to \(k\). Induction then gives
\[
\deg_\rho\Theta_k\le k,\quad \deg_\rho w_0\le1,\quad
\deg_\rho w_k\le k-1\ (k\ge1).
\]
Specifically, the order-\(k\) term containing \(w_0\) in \(\Theta'\) has degree at most \(k+1\); a term containing \(w_j\), \(j\ge1\), has degree at most \(k-1\). The readout recurrence completes the induction. Differentiating these identities with respect to \(W^{(3)}_0\) preserves the degree bounds.

Accordingly the time coefficients of \(z^{(2)},\zeta,\beta(z^{(2)})\) have degree at most their order; those of \(q^{(2)},\delta^{(2)},\widehat\delta^{(2)},(z^{(2)})'\) have degree at most order plus one. Since \(a_k=\widehat\delta^{(2)}_{k-1}/k\) and \(c=(1+(z^{(2)})^2)\odot a\), \(a_k,c_k\) have degree at most \(k\). In
\[
P_n(\rho)=\sum_{r+t+u+v=5}\mathbb E_J\!\left[
\frac{c_r^T(b_t\odot q^{(2)}_u\odot\zeta_v)}n
-\frac{c_r^T(b_t\odot\nu_u\odot c_v)}n
\,\middle|\,\mathcal F_n\right],                     \tag{C11}
\]
where \(b_t=[s^t]\beta(z^{(2)})\), \(\nu_u=[s^u](z^{(2)})'\), every term has degree at most \(r+t+u+1+v=6\). Probe averaging preserves this exact polynomial identity. Smoothness suffices; no convergent time series or approximation in \(\rho\) is being assumed.

## 5. Finite jet compilation and the actual Theorem 2.10 application

For fixed \(\rho\), the scalar coefficient rule is
\[
[s^k]f(v(s))=\sum_{t=0}^k\frac{f^{(t)}(v_0)}{t!}
\sum_{\substack{r_1+\cdots+r_t=k\\r_j\ge1}}
v_{r_1}\odot\cdots\odot v_{r_t},
\]
with the usual empty term at \(k=0\). Positive-order learned matrix coefficients obey
\[
(W^{(\ell)})_k=\frac1k\sum_{a+b=k-1}
(\delta^{(\ell)})_a(h^{(\ell-1)})_b^T/n,\qquad \ell=2,3.
\]
Their action on a vector reduces to a fixed finite sum of vectors times dot products divided by \(n\); transposed action exchanges the two factors. Differentiating this rule differentiates both outer-product factors and both factors of every contraction. At order zero, variation of \(W^{(3)}_0v\) is \(Jv+W^{(3)}_0\widehat v\), and similarly for the transpose. The \(W^{(2)}_0\) action has no \(J\) term. These recurrences construct the complete primal jet through order six and all responses in (C11) by a number of instructions independent of \(n\).

Every nonpolynomial coefficient function is evaluated at an initialized node. The initialized gates and derivatives of \(\phi,\phi',\beta\) are bounded smooth functions. For the first transformed layer,
\[
(\phi\circ F^{-1})^{(t)}(F(z))
=(\phi'(z)\partial_z)^t\phi(z).
\]
For \(t\ge1\) these are rational functions, with denominator a power of \(1+z^2\), decaying at infinity; successive differentiation and multiplication by \(\phi'\) preserve this property. Their derivatives needed for the first variation are likewise bounded. The \(t=0\) function is bounded \(\arctan z\), and \(F(z)\) itself is a polynomial. Thus the actual coordinate maps have fixed polynomial growth. No empirical inverse or nonpolynomial function of positive-order jet coefficients is required.

The key closure in transfer (20a)–(20c) is exact. Let a pure vector be built from the Gaussian roots and matrices \(W^{(2)}_0,W^{(3)}_0,J\), using only parameterless coordinate maps and matrix/transposed-matrix actions. Let \(\mathscr S\) be polynomials in finitely many pure-vector contractions \(p^Tq/n\). Represent each required vector as \(u=\sum_a\alpha_ap_a\), with \(\alpha_a\in\mathscr S\), \(p_a\) pure. Then
\[
u\odot v=\sum_{a,b}\alpha_a\gamma_b(p_a\odot q_b),\quad
Wu=\sum_a\alpha_aWp_a,\quad
u^Tv/n=\sum_{a,b}\alpha_a\gamma_b\,p_a^Tq_b/n.
\]
Addition and scalar multiplication close as well. Pulling \(\alpha_a\) outside a matrix action is a finite-width algebraic identity even if \(\alpha_a\) depends on that same matrix or on \(J\). There is no independence assumption in this step.

The initialized values and their gate derivatives are pure. The recurrences above, their first variations, the primitive, and all products in (C11) use only these closed operations. In differentiating a gate coefficient one adds \(f^{(t+1)}(v_0)\odot\widehat v_0\), which has the same form. In particular \(\widehat z^{(3)}_0=Jh^{(2)}_0\) is pure. Induction through the fixed order therefore appends only finitely many pure nodes and contractions. Crucially, no step applies a nonpolynomial \(f\) to an empirical-scalar-weighted sum. The expansion is not an approximation to a trajectory or a purported general removal of scalar feedback.

The needed primary result is the following specialization. A fixed program with parameterless coordinate maps and actions of independent Gaussian matrices and their actual transposes, initialized by iid jointly Gaussian vector slices as in Setup 2.2, has almost-sure convergence of each fixed polynomially bounded empirical test to its prescribed scalar-law expectation when its coordinate maps are polynomially bounded. Theorem 2.10 imposes no additional rank-convergence hypothesis; footnote 15 explicitly confirms this. It does not, in this application, supply convergence of unconditional expectations. [Tensor Programs III v3, Theorem 2.10, printed p. 9](https://arxiv.org/pdf/2009.10685v3#page=9).

Every hypothesis is met by the constructed pure program: its independent matrices have variance \(1/n\); the aligned initial root tuple \((z^{(1)}_{0,\alpha},G_{4,\alpha})\) is iid \(N(0,I_2)\), independent of them; all three populations have size \(n\); each actual coordinate product and contraction stays within its population; and \(\rho\) is a fixed deterministic parameter built into maps. The transformed root \(F(z^{(1)}_0)\) and the upper initial preactivations are generated nodes, not falsely declared Gaussian roots. Constant and zero nodes cause no missing rank premise. Repeated uses of a matrix and its transpose remain uses of the same matrix.

The theorem is applied only to pure-vector contractions, with test \((p,q)\mapsto pq\). It is not applied to the original scalar-feedback recurrences. For these smooth maps, the scalar-law covariance and derivative-correction expectations are finite by induction: gate derivatives are bounded, the remaining coordinate maps are polynomial, and Gaussian moments of every fixed order are finite. All finitely many required contractions converge jointly to finite constants after concatenating their pure constructions. Polynomial scalar prefactors therefore converge too. In particular, for an actual expanded vector \(V[J]=\sum_a\alpha_ap_a\),
\[
\|V[J]\|_2^2/n=\sum_{a,b}\alpha_a\alpha_b\,p_a^Tp_b/n=O_{\mathbb P}(1). \tag{C12}
\]
This remains valid when prefactors depend on \(J\). The bounded-degree statements concern a fixed finite calculation; no uniform degree bound over arbitrary programs is invoked.

## 6. Conditional trace tightness, interpolation, and the combined conclusion

Realized tightness alone would not justify averaging over probes. The transfer supplies a valid additional argument. If \(g\) is standard Gaussian independent of a sigma-field \(\mathcal F\), \(T\) is \(\mathcal F\)-measurable, and \(Q=\|Tg\|_2^2/n\), then, with \(M=T^TT/n\),
\[
\mu=\mathbb E[Q\mid\mathcal F]=\operatorname{Tr}M,\qquad
\mathbb E[Q^2\mid\mathcal F]=\mu^2+2\operatorname{Tr}(M^2)\le3\mu^2.
\]
These follow by diagonalizing the nonnegative matrix \(M\) and using Gaussian second and fourth moments. For \(\mu>0\),
\(\mathbb E[Q\mathbf1_{\{Q>\mu/2\}}\mid\mathcal F]\ge\mu/2\);
conditional Cauchy–Schwarz gives
\[
\mathbb P(Q>\mu/2\mid\mathcal F)\ge1/12,\qquad
\mathbb P(\mu>2R)\le12\mathbb P(Q>R).                 \tag{C13}
\]
Thus tight realized quadratic forms imply tight conditional traces, without uniform integrability or a bound on unconditional expectations.

Here \(g=\operatorname{vec}(\sqrt nJ)\) has \(n^2\) independent standard coordinates. Each of \(c_r\), \(b_t\odot q^{(2)}_u\odot\zeta_v\), and \(b_t\odot\nu_u\odot c_v\) is exactly linear in \(g\), conditional on \(\mathcal F_n\): the weights are primal jets, and the response equations are first variations. Their alternative pure-program expansion may obscure that linearity but does not change it. Equation (C12), followed by (C13), therefore makes all their conditional squared norms divided by \(n\) tight. Conditional Cauchy–Schwarz bounds every bilinear term of (C11) by the product of two such conditional norms. There are only finitely many terms, proving \(P_n(\rho)=O_{\mathbb P}(1)\) for each fixed \(\rho\).

Apply this at \(\rho=0,1,\ldots,6\) on the common initialization. A finite union bound makes their maximum tight; independence between these evaluations is unnecessary. Since \(\deg_\rho P_n\le6\), the coefficient vector satisfies
\[
(A_{n,0},\ldots,A_{n,6})^T
=V^{-1}(P_n(0),\ldots,P_n(6))^T,\quad V_{jm}=j^m.
\]
The constant column is one and \(\det V=\prod_{0\le i<j\le6}(j-i)\ne0\). This fixed inverse preserves tightness, so every coefficient is tight. Consequently
\[
n|P_n(n^{-1})-P_n(0)|
\le\sum_{m=1}^6|A_{n,m}|=O_{\mathbb P}(1).            \tag{C14}
\]
All probe averages have already been taken. The probability in (C14) concerns only the original hidden initialization and \(G_4\). No common positive-time existence interval for the seven auxiliary readout amplitudes, uniform Taylor bound, or expected-moment theorem has been used.

By the checked initialization and common work identity,
\[
J_n^{\rm can}=P_n(n^{-1})=P_n(0)+O_{\mathbb P}(n^{-1})
\ \longrightarrow\ J_*>0
\]
in probability, with exactly the wrapper's displayed constant. Hence \(\mathbb P(J_n^{\rm can}>J_*/2)\to1\). The wrapper's final Theorem 2.10 source description and dependency link accurately match this proof.

This proves only the canonical fifth coefficient. It does not prove \(L^1\) convergence or a finite-width expectation sign for the tiny-readout coefficient: tightness alone would not supply either. Lower time coefficients need not vanish at tiny readout, so positivity of the fifth coefficient does not contradict a nonpositive complete work function near zero. An exact local identity making the full signed work vanish on events of probability tending to one would force this coefficient to vanish, and is therefore excluded. No width-uniform positive-time sign, time-limit exchange, Taylor radius, response-amplitude growth bound, clipped-flow result, failure of a positive-constant Gronwall estimate, or full canonical population/continuation theorem follows. These are precisely the current lemma's limitations.
