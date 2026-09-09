## Part N. Nonzero initial motion and variation of the projected kernel

This part proves the remaining initial-motion assertions of Theorem M.1. Throughout, \(A=A_0\) and \(B=B_0\) denote the initialized actions when no time argument is shown. Their norms are at most 10, and their stars are their actual adjoints. All products and inner products are taken in the appropriate layer. We use the internal fixed-program theorem F.1, the operator-moment and trace-probe estimates (F.4a)–(F.4c), the bounded multiplier and weighted Taylor lemmas F.5–F.7, and the derivative-valid initialization observation lemma V.I. These statements include the singular input-Gram cases.

The proof first identifies explicit hidden directions, proves positivity of all parameter blocks and every bottom sample using fresh reverse Gaussian sources, and then establishes quantitative affine lower bounds for every upper sample. A direct perturbation estimate preserves the upper bounds for the amplitude in (M.21). The physical equations determine the time factors, and a scalar feature-energy differential determines the kernel expansion.

### N.1. Initial directions and their scalar feature-energy interpretation

Write
\[
 p_i=y_i/3,\qquad m=\sum_{i=1}^3p_i,\qquad
 m\in\{-1,-1/3,1/3,1\},\qquad \sum_i|p_i|=1.
 \tag{N.1}
\]
All \(p_i\) are nonzero, and \(|m|\ge1/3\). Let \(Z_i^\ell,h_i^\ell\) be the initialized forward fields for
\(\phi(z)=a(1+z)+e\arctan z\), and put \(d_i^\ell=\phi'(Z_i^\ell)\).
The activation parameters in this part satisfy \(a\ge1\) and \(0<e\le1\), with the additional quantitative upper bound specified in Section N.5. Define
\[
 H=\sum_i p_i h_i^3,\qquad
 \beta_i^3=H d_i^3,\qquad q_i^2=B^*\beta_i^3,\qquad
 \beta_i^2=d_i^2q_i^2,\qquad q_i^1=A^*\beta_i^2,\qquad
 \beta_i^1=d_i^1q_i^1.
 \tag{N.2}
\]
All these variables lie in the indicated \(L^2\) spaces, because the gates are bounded and the actions are bounded. Lemma V.I identifies their actual finite-array limits and all the response coefficients used below; this is not an application of a bounded-derivative theorem directly to the unbounded products in (N.2).

The three hidden raw directions are
\[
 V^1=d^{-1}\sum_i p_i\beta_i^1x_i,\qquad
 V^2=\sum_i p_i\beta_i^2\otimes h_i^1,\qquad
 V^3=\sum_i p_i\beta_i^3\otimes h_i^2.
 \tag{N.3}
\]
Here \(V^1\in L^2(\Omega_1;\mathbb R^d)\), \(V^2\) and \(V^3\) are Hilbert–Schmidt operators, and
\[
 \|V\|_{\rm hidden}^2
       =d\|V^1\|_2^2+\|V^2\|_{\rm HS}^2+\|V^3\|_{\rm HS}^2.
 \tag{N.4}
\]
For every sample define the preactivation directions
\[
 U_j^1=V^1\cdot x_j=\sum_i\Gamma_{ji}p_i\beta_i^1,
\]
\[
 U_j^2=V^2h_j^1+A(d_j^1U_j^1),\qquad
 U_j^3=V^3h_j^2+B(d_j^2U_j^2).
 \tag{N.5}
\]

The scalar functional needed later is defined on the hidden raw parameter space by
\[
 {\cal E}(\theta_h)=\tfrac12\left\|\sum_i p_i h_i^3(\theta_h)\right\|_3^2,
 \qquad \theta_h=(w,A,B).
 \tag{N.6}
\]
It is continuously Fréchet differentiable in the hidden raw norm, and at initialization its raw gradient is \(V\). We give the argument to specify the exact differentiability assertion.

On a raw neighborhood, all forward differences are \(O(\eta)\) in \(L^2\) for an increment \(\Delta\theta_h\) of raw norm \(\eta\): apply the Lipschitz activation bounds and
\[
 \Delta(Ah)=\Delta A\,h+A\,\Delta h+\Delta A\,\Delta h,
 \qquad \|\Delta A\|_{\rm op}\le\|\Delta A\|_{\rm HS}.
\]
Thus \(\Delta H=O(\eta)\), and
\[
 {\cal E}(\theta_h+\Delta\theta_h)-{\cal E}(\theta_h)
       =\langle H,\Delta H\rangle+\tfrac12\|\Delta H\|^2.
 \tag{N.7}
\]
The second term is \(O(\eta^2)\). For any fixed \(v,z\in L^2\), the weighted Taylor estimate (F.41) says
\[
 E\!\left[v\{\phi(z+q)-\phi(z)-\phi'(z)q\}\right]
                                             =o(\|q\|_2).
 \tag{N.8}
\]
Explicitly the remainder is bounded both by
\(\|\phi''\|_\infty|q|^2/2\) and \(2\|\phi'\|_\infty|q|\).
Split its weighted expectation at \(|v|=M\); the bound is
\(\|\phi''\|_\infty M\|q\|_2^2/2+
2\|\phi'\|_\infty\|v\mathbf1_{|v|>M}\|_2\|q\|_2\).
First send \(\|q\|_2\) to zero and then \(M\) to infinity.

Apply (N.8) in each term \(p_i\langle H,\Delta h_i^3\rangle\), with fixed top weight \(H\). Expanding \(\Delta z_i^3\) and using adjunction gives, up to \(o(\eta)\),
\[
 \sum_i p_i\{\langle\beta_i^3,\Delta B h_i^2\rangle
                         +\langle q_i^2,\Delta h_i^2\rangle\}.
\]
Terms containing \(\Delta B\,\Delta h_i^2\) are \(O(\eta^2)\).
Apply (N.8) with the fixed weights \(q_i^2\), expand \(\Delta z_i^2\), and move \(A\) through the resulting inner product. A last application with fixed weights \(q_i^1\) gives
\[
 d{\cal E}[\Delta\theta_h]
 =\sum_i p_i\{\langle\beta_i^1,x_i\cdot\Delta w\rangle
             +\langle\beta_i^2,\Delta A h_i^1\rangle
             +\langle\beta_i^3,\Delta B h_i^2\rangle\}
 =\langle V,\Delta\theta_h\rangle_{\rm hidden}.
 \tag{N.9}
\]
This proves the Fréchet derivative. Its continuity follows from forward \(L^2\) continuity, the bounded multiplier lemma F.5 applied successively to the gates and incoming fields, and the rank-one Hilbert–Schmidt difference inequality. This is a scalar differentiability result; no Fréchet derivative of the nonlinear map from all of \(L^2\) to \(L^2\) is assumed.

### N.2. Positive backward Grams, hidden blocks, and every bottom sample

Let
\[
 Q_\ell=(\langle h_i^\ell,h_j^\ell\rangle)_{ij},\qquad
 S_\ell=(\langle\beta_i^\ell,\beta_j^\ell\rangle)_{ij}.
 \tag{N.10}
\]
The initial Gaussian projection and augmented-Gram inequality (G.1), (G.4) imply \(Q_1\succeq a^2(\Gamma+\mathbf1\mathbf1^T)\succ0\), and \(Q_2\succeq a^2Q_1\succ0\). The initialized \(Z^3\) is therefore a nondegenerate centered three-dimensional Gaussian, with covariance \(Q_2\), and has a strictly positive density on \(\mathbb R^3\).

For \(v\in\mathbb R^3\), \(v^TS_3v=0\) would imply
\[
 \left[\sum_i p_i\phi(z_i)\right]
       \left[\sum_i v_i\phi'(z_i)\right]=0
                                      \quad\hbox{for every }z\in\mathbb R^3.
 \tag{N.11}
\]
Indeed the identity first holds almost surely, and full support and continuity extend it to every point. The first factor has no open zero set: its derivative in coordinate \(i\) is \(p_i\phi'(z_i)\), which is never zero because \(p_i\ne0\) and \(\phi'\ge a\). Its nonzero set is therefore dense. The second factor vanishes on that dense set and hence everywhere. Differentiate it in coordinate \(i\) to obtain \(v_i\phi''(z_i)=0\) for every \(z_i\). Since \(\phi''(z)=-2ez/(1+z^2)^2\) is not identically zero when \(e>0\), every \(v_i=0\). Thus
\[
                                  S_3\succ0.
 \tag{N.12}
\]

For use in the next step, the exact derivative-valid transpose formulas of Lemma V.I are
\[
 q_i^2=\zeta_i^2+\sum_jD^3_{ij}h_j^2,\qquad
 D^3_{ij}=E[p_jd_j^3d_i^3+\mathbf1_{i=j}H\phi''(Z_i^3)],
 \qquad E[\zeta^2(\zeta^2)^T]=S_3,
 \tag{N.13}
\]
\[
 q_i^1=\zeta_i^1+\sum_jD^2_{ij}h_j^1,\qquad
 D^2_{ij}=E[\mathbf1_{i=j}\phi''(Z_i^2)q_i^2+d_i^2D^3_{ij}d_j^2],
 \qquad E[\zeta^1(\zeta^1)^T]=S_2.
 \tag{N.14}
\]
The families \(\zeta^2,\zeta^1\) are centered Gaussian and independent of the respective forward-source families and first-layer roots. Their return terms are retained. The expected derivative formulas are legitimate precisely because Lemma V.I first truncates the incoming fields, passes their expected derivatives by dominated convergence, and then removes the truncations in their actual matrix answers.

Conditioning on all the layer-two forward sources in (N.13) gives
\(\operatorname{Cov}(\beta^2\mid Z^2)
       =\operatorname{diag}(d_i^2)S_3\operatorname{diag}(d_i^2)\).
Hence, for every \(v\in\mathbb R^3\),
\[
 v^TS_2v\ge E\operatorname{Var}\!\left(\sum_i v_i\beta_i^2\mid Z^2\right)
 \ge a^2\lambda_{\min}(S_3)\|v\|_2^2.
 \tag{N.15}
\]
In particular \(S_2\succ0\). Likewise
\[
 \operatorname{Cov}(\beta^1\mid Z^1)
 =\operatorname{diag}(d_i^1)S_2\operatorname{diag}(d_i^1)
 \succeq a^2\lambda_{\min}(S_2)I_3.
 \tag{N.16}
\]
These lower bounds use fresh reverse Gaussian covariance, not a claim that the full incoming fields are independent of the forward features.

Apply (N.16) to each Euclidean component of \(V^1\), and sum:
\[
 d\|V^1\|_2^2
 \ge\frac{a^2\lambda_{\min}(S_2)}d\sum_i p_i^2\|x_i\|_{\mathbb R^d}^2
 =a^2\lambda_{\min}(S_2)\sum_i p_i^2>0.
 \tag{N.17}
\]
For the two matrix blocks the rank-one inner-product formula yields
\[
 \|V^\ell\|_{\rm HS}^2
   =\sum_{i,j}p_ip_j(S_\ell)_{ij}(Q_{\ell-1})_{ij}
   =\operatorname{tr}\!\left(\operatorname{diag}(p)S_\ell
                         \operatorname{diag}(p)Q_{\ell-1}\right),
 \quad\ell=2,3.
 \tag{N.18}
\]
For positive definite \(S,Q\), the last trace is at least
\(\lambda_{\min}(S)\lambda_{\min}(Q)\sum_i p_i^2>0\).
To see this, the matrix \(\operatorname{diag}(p)S\operatorname{diag}(p)
-\lambda_{\min}(S)\operatorname{diag}(p)^2\) is positive semidefinite; its trace pairing with \(Q\) is nonnegative, by diagonalizing \(Q\). Apply the same reasoning to \(\operatorname{diag}(p)^2\) and \(Q\succeq\lambda_{\min}(Q)I\). Thus all three hidden parameter directions are nonzero.

For any fixed sample \(j\), (N.5) and (N.16) give
\[
 \|U_j^1\|_2^2
 \ge E\operatorname{Var}(U_j^1\mid Z^1)
 \ge a^2\lambda_{\min}(S_2)\sum_i\Gamma_{ji}^2p_i^2
 \ge a^2\lambda_{\min}(S_2)p_j^2>0.
 \tag{N.19}
\]
The last step uses \(\Gamma_{jj}=1\). Since \(d_j^1\ge a\), the corresponding feature direction \(d_j^1U_j^1\) is nonzero as well. This covers singular \(\Gamma\) without its inverse and without requiring nonzero affine bottom motion.

### N.3. Exact affine formulas for the two upper layers

We now set \(e=0\) only for a comparison calculation, on the same initialized actions and roots. Define
\[
 z_p=\sum_i p_iZ_i^1,\qquad \gamma_j=(\Gamma p)_j,\qquad
 k=m\mathbf1_1+z_p,
\]
\[
 v=a^2m\mathbf1_2+a^3Ak,\qquad
 H=am\mathbf1_3+Bv,\qquad Q=B^*H.
 \tag{N.20}
\]
The subscripts on the constant vectors specify their layer. These identities follow by summing the affine forward equations:
\(\sum_i p_ih_i^1=ak\),
\(\sum_i p_ih_i^2=am\mathbf1_2+a^2Ak\), and
\(\sum_i p_ih_i^3=am\mathbf1_3+Bv\).

Affine backward gates give, independently of the sample index,
\[
 \beta_i^3=aH,\qquad \beta_i^2=a^2Q,\qquad
 \beta_i^1=a^3A^*Q,\qquad U_j^1=a^3\gamma_jA^*Q.
 \tag{N.21}
\]
Also \(V^2=a^3Q\otimes k\). The first affine feature Gram is
\(Q_1=a^2(\Gamma+\mathbf1\mathbf1^T)\), so
\(\langle k,h_j^1\rangle=a(m+\gamma_j)\). Substituting in (N.5) gives
\[
 U_j^2=a^4L_jQ,\qquad
               L_j=(\gamma_j+m)I+\gamma_jAA^*.
 \tag{N.22}
\]
At the next layer,
\(Q_2=a^4\Gamma+(a^2+a^4)\mathbf1\mathbf1^T\) and
\(V^3=H\otimes v\). Therefore
\(\langle v,h_j^2\rangle
=a^5[\gamma_j+(1+a^{-2})m]\). The second formula in (N.5) gives
\[
 U_j^3=a^5T_jH,
\]
\[
 T_j=[\gamma_j+(1+a^{-2})m]I
       +(\gamma_j+m)BB^*+\gamma_jBAA^*B^*.
 \tag{N.23}
\]
These formulas hold for every sample individually; no permutation symmetry of the inputs or labels has been used.


### N.4. Finite Gaussian calculations and strictly positive affine lower bounds

We specify carefully how finite Gaussian identities yield deterministic population inequalities. Let \(A_n,B_n\) be the independent initialized square Gaussian matrices and use the corresponding first-layer roots to define \(k_n,v_n,H_n,Q_n\) by (N.20). For a fixed sample, put
\[
 L_{j,n}=(\gamma_j+m)I+\gamma_jA_nA_n^T,
\]
\[
 T_{j,n}=[\gamma_j+(1+a^{-2})m]I
       +(\gamma_j+m)B_nB_n^T+\gamma_jB_nA_nA_n^TB_n^T.
 \tag{N.24}
\]
The numbers \(\gamma_j,m\) are deterministic. The vectors
\(a^4L_{j,n}Q_n\) and \(a^5T_{j,n}H_n\) are fixed finite programs and converge to (N.22)–(N.23), including their squared norms. They can be viewed as proxies for the finite feature directions after empirical Gram contractions are replaced by their limiting deterministic values. The finite-array inner products need not equal their population values exactly; Theorem F.1 justifies this replacement.

For every fixed polynomial matrix expression \(P_n\) in the initialized actions and their transposes, (F.4b) bounds every fixed moment of \(\|P_n\|_{\rm op}\) uniformly in \(n\). The vectors just described have normalized norms bounded by fixed polynomials in \(\|A_n\|_{\rm op},\|B_n\|_{\rm op},\|z_{p,n}\|_n\) and constants. All fixed moments of the last normalized Gaussian norm are uniformly bounded by Jensen. Hölder consequently proves uniform moments of all fixed orders for these vector norms and their squared norms. Their deterministic convergence in probability from F.1 therefore implies convergence of expectations: truncate at a fixed level, pass the bounded part, and bound the tail using a higher moment.

A normalized trace of \(P_n\) also has a deterministic limit. Append an independent standard Gaussian vector \(g_n\); the contraction \(\langle g_n,P_ng_n\rangle_n\) is a fixed finite program, and (F.4c) makes its difference from \(n^{-1}\operatorname{tr}P_n\) tend to zero in \(L^2\). Its trace thus has a deterministic limit in probability, and the preceding operator moment bounds give uniform integrability and convergence of its expectation. Write \(\tau(P)\) for this limiting normalized trace; this symbol does not assert existence of a trace of the infinite-dimensional initialized action. These arguments apply simultaneously to every finite list of traces and contractions below.

For completeness the Gaussian fourth-moment identities used in the calculations follow from differentiating the Gaussian moment-generating function: for centered jointly Gaussian scalars,
\[
 E[X_1X_2X_3X_4]
 =E[X_1X_2]E[X_3X_4]+E[X_1X_3]E[X_2X_4]
                         +E[X_1X_4]E[X_2X_3].
 \tag{N.25}
\]
One can verify this directly by differentiating
\(E e^{t^TX}=\exp(t^T\operatorname{Cov}(X)t/2)\) four times at zero. The same function is even, so centered cubic moments vanish.

Condition on \(A_n,z_{p,n}\), making \(v_n\) fixed and leaving \(B_n\) independent. In coordinates
\[
 (Q_n)_r=am\sum_i(B_n)_{ir}
           +\sum_{i,s}(B_n)_{ir}(B_n)_{is}(v_n)_s.
\]
The first sum is centered Gaussian of covariance \(a^2m^2 I\); the expectation of the second is \(v_n\). Its covariance, by the two non-mean pairings in (N.25), is
\(\|v_n\|_n^2I+v_nv_n^T/n\). The covariance between the first and second sums is zero by the cubic moment identity. Thus exactly at every width
\[
 E_BQ_n=v_n,\qquad
 \operatorname{Cov}_B(Q_n)
 =(a^2m^2+\|v_n\|_n^2)I+v_nv_n^T/n.
 \tag{N.26}
\]
For any fixed matrix \(L\) measurable with respect to \(A_n,z_{p,n}\), taking the trace of \(L\operatorname{Cov}_B(Q_n)L^T\) gives
\[
 E_B\|LQ_n\|_n^2
 =(1+1/n)\|Lv_n\|_n^2
       +(a^2m^2+\|v_n\|_n^2)\frac1n\operatorname{tr}(LL^T).
 \tag{N.27}
\]
In particular this bounds the expectation below by its second summand.

Here are all normalized traces required for (N.22). For \(X_n=A_nA_n^T\), entrywise use of (N.25) gives
\[
 E(X_n)_{ij}=\delta_{ij},\qquad
 E[(X_n)_{ij}(X_n)_{kl}]
 =\delta_{ij}\delta_{kl}
       +n^{-1}(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}).
 \tag{N.28}
\]
Indeed expand the two entries as sums over the two column indices; the mean pairing contributes the first term, and each of the two cross pairings forces the same column and contributes the displayed factor \(1/n\). Summing \(i=j\) gives \(E\tau_n(X_n)=1\). Summing \(k=j,l=i\) gives
\[
 E\tau_n(X_n^2)
 =\frac1n\sum_{i,j}\{\delta_{ij}+n^{-1}(\delta_{ij}+1)\}
 =2+1/n.
\]
The trace-probe and uniform-integrability argument therefore proves
\[
                    \tau(AA^*)=1,\qquad \tau((AA^*)^2)=2.
 \tag{N.29}
\]
It follows by expanding \(L_j^2\) that
\[
 \tau(L_j^2)
 =(\gamma_j+m)^2+2\gamma_j(\gamma_j+m)+2\gamma_j^2
                         =(m+2\gamma_j)^2+\gamma_j^2.
 \tag{N.30}
\]
The other factor in (N.27) also has a deterministic limit. Since \(A_n\) is independent of \(k_n\), \(E_AA_nk_n=0\) and \(E_A\|A_nk_n\|_n^2=\|k_n\|_n^2\). The first-layer roots are centered, with
\(E\|z_{p,n}\|_n^2=p^T\Gamma p\). Hence for every \(n\)
\[
 E\|v_n\|_n^2=a^4m^2+a^6(m^2+p^T\Gamma p).
\]
The deterministic finite-program limit and uniform integrability identify
\[
                   \|v\|_2^2=a^4m^2+a^6(m^2+p^T\Gamma p).
 \tag{N.31}
\]
The product of the nonnegative factors in (N.27) converges in probability to the product of their deterministic limits, and its higher moments are bounded as above. Thus its expectation converges too. Taking the unconditional expectation in (N.27) with \(L=L_{j,n}\), and then passing to the limits just justified, proves
\[
 \|U_j^2\|_2^2
 \ge a^8[a^2m^2+a^4m^2+a^6(m^2+p^T\Gamma p)]
                               [(m+2\gamma_j)^2+\gamma_j^2].
 \tag{N.32}
\]
Since \(p^T\Gamma p\ge0\) and
\[
 (m+2c)^2+c^2=5(c+2m/5)^2+m^2/5,
\]
we obtain the positive lower bound
\[
                 \|U_j^2\|_2^2
                 \ge\frac{a^8m^4}{5}(a^2+a^4+a^6)>0.
 \tag{N.33}
\]

For (N.23), \(T_{j,n}\) is even under \(B_n\mapsto-B_n\), whereas \(B_nv_n\) is odd. Condition on \(A_n,z_{p,n}\); symmetry of \(B_n\) makes the cross term in
\(\|T_{j,n}(am\mathbf1+B_nv_n)\|_n^2\) have expectation zero. Therefore
\[
 E\|a^5T_{j,n}H_n\|_n^2
 \ge a^{12}m^2 E\|T_{j,n}\mathbf1\|_n^2.
\]
Left orthogonal invariance of \(B_n\), at fixed \(A_n\), makes the conditional expectation of \(T_{j,n}^2\) a scalar multiple of the identity. This can also be checked using only row sign changes to kill off-diagonal entries and row permutations to equalize diagonal entries. Since \(\|\mathbf1\|_n=1\),
\(E_B\|T_{j,n}\mathbf1\|_n^2=E_B\tau_n(T_{j,n}^2)\).
The deterministic limits and uniform integrability thus give
\[
                         \|U_j^3\|_2^2\ge a^{12}m^2\tau(T_j^2).
 \tag{N.34}
\]

We compute that trace in full. Put \(S_n=B_nB_n^T\), \(R_n=B_nA_nA_n^TB_n^T\), and \(M_n=B_n^TB_n\). Equations (N.28)–(N.29), now for \(B_n\), give
\(\tau(S)=1,\tau(S^2)=2\). Conditioning on \(B_n\), \(E_AA_nA_n^T=I\) gives
\[
 E_A\tau_n(R_n)=\tau_n(S_n),\qquad
 E_A\tau_n(S_nR_n)=\tau_n(S_n^2).
\]
Therefore the limiting traces satisfy \(\tau(R)=1,\tau(SR)=2\).
For the final one, expand
\(\operatorname{tr}(X_nM_nX_nM_n)
 =\sum_{i,j,k,l}(X_n)_{ij}(M_n)_{jk}(X_n)_{kl}(M_n)_{li}\).
Each term of (N.28) contributes, respectively,
\(\operatorname{tr}M_n^2\), \(n^{-1}\operatorname{tr}M_n^2\), and
\(n^{-1}(\operatorname{tr}M_n)^2\). Dividing by \(n\) proves the exact formula
\[
 E_A\tau_n(R_n^2)
 =(1+1/n)\tau_n(M_n^2)+\tau_n(M_n)^2.
 \tag{N.35}
\]
The cyclic trace identities give \(\tau_n(M_n^2)=\tau_n(S_n^2)\) and
\(\tau_n(M_n)=\tau_n(S_n)\). Their deterministic limits are 2 and 1, and their squared moments pass by the already proved uniform integrability. Hence
\[
              \tau(S)=\tau(R)=1,\qquad
              \tau(S^2)=\tau(SR)=2,\qquad \tau(R^2)=3.
 \tag{N.36}
\]
Every convergence assertion here follows from F.1 and the trace-probe argument (F.4c), with moment control (F.4b); the finite fourth-moment expectation calculations alone would not prove concentration.

Set \(t_a=a^{-2}\). For
\(u=\gamma_j+(1+t_a)m,\ v=\gamma_j+m,\ w=\gamma_j\),
(N.36) gives
\[
 \tau(T_j^2)=(u+v+w)^2+(v+w)^2+w^2
       =[3\gamma_j+(2+t_a)m]^2+(2\gamma_j+m)^2+\gamma_j^2.
\]
Completing the square in \(\gamma_j\) gives
\[
 \tau(T_j^2)
 =14\left(\gamma_j+\frac{8+3t_a}{14}m\right)^2
                         +\frac{6+8t_a+5t_a^2}{14}m^2.
 \tag{N.37}
\]
Combining this with (N.34) yields
\[
              \|U_j^3\|_2^2
              \ge\frac{a^{12}m^4}{14}(6+8a^{-2}+5a^{-4})>0.
 \tag{N.38}
\]
In particular, using \(a\ge1\) and \(|m|\ge1/3\), the two affine lower bounds imply
\[
             \|U_{j,0}^2\|_2\ge\frac{a^7}{9\sqrt5},\qquad
             \|U_{j,0}^3\|_2\ge\frac{a^6}{9}\sqrt{\frac37}.
 \tag{N.39}
\]
The subscript 0 denotes the affine comparison, and these bounds hold for every upper sample uniformly over admissible input Grams and binary labels.


### N.5. Explicit nonlinear perturbation and a geometry-independent cutoff

Compare nonlinear and affine initial calculations on the same initialized actions and first-layer roots. Use subscript \(e\) for the nonlinear fields, subscript 0 for the affine fields, and \(\Delta\) for their difference. For every layer and sample,
\[
 \|d^\ell_{j,e}\|_\infty\le2a,\qquad
                 \|d^\ell_{j,e}-a\|_\infty\le e.
 \tag{N.40}
\]
The second bound compares with the constant affine gate, so it requires no derivative of a change of preactivation.

The following estimates use \(e\le1\), \(\|A\|,\|B\|\le10\), \(\|Z_j^1\|_2=1\), \(\pi/2<2\), and \(\sum_i|p_i|=1\). All bounds are per sample; the bound on \(h^3\) also bounds \(H\).
\[
\begin{array}{c|c|c}
 \text{field}&\text{nonlinear norm bound}&\text{difference bound}\\ \hline
 h^1&4a&2e\\
 h^2&43a^2&22ae\\
 h^3,\ H&433a^3&222a^2e\\
 \beta^3&866a^4&655a^3e\\
 \beta^2&17320a^5&15210a^4e\\
 \beta^1,\ U_j^1&346400a^6&325300a^5e
\end{array}
 \tag{N.41}
\]
Here is the full scalar derivation. Forward propagation gives
\[
 \|h_e^1\|\le2a+2\le4a,\quad
 \|h_e^2\|\le a+10a(4a)+2\le43a^2,\quad
 \|h_e^3\|\le a+10a(43a^2)+2\le433a^3.
\]
The same initial actions appear in both programs, so
\[
 \|\Delta h^1\|\le2e,\quad
 \|\Delta h^2\|\le10a(2e)+2e\le22ae,\quad
 \|\Delta h^3\|\le10a(22ae)+2e\le222a^2e.
 \tag{N.42}
\]
The affine forward bounds are \(2a,21a^2,211a^3\). Summing with \(|p_i|\) gives the corresponding bounds for \(H_e,H_0,\Delta H\).

The backward difference decompositions are exactly
\[
 \beta_e^3=d_e^3H_e,\qquad
 \Delta\beta^3=a\Delta H+(d_e^3-a)H_e,
\]
\[
 \beta_e^2=d_e^2B^*\beta_e^3,\qquad
 \Delta\beta^2=aB^*\Delta\beta^3+(d_e^2-a)B^*\beta_e^3,
\]
\[
 \beta_e^1=d_e^1A^*\beta_e^2,\qquad
 \Delta\beta^1=aA^*\Delta\beta^2+(d_e^1-a)A^*\beta_e^2.
 \tag{N.43}
\]
Their nonlinear norm coefficients are \(2\cdot433=866\),
\(20\cdot866=17320\), and \(20\cdot17320=346400\), with the powers of \(a\) in (N.41). The difference coefficients are
\[
 222+433=655,\qquad
 10\cdot655+10\cdot866=15210,\qquad
 10\cdot15210+10\cdot17320=325300.
 \tag{N.44}
\]
The respective powers are \(a^3e,a^4e,a^5e\). Since
\(U_j^1=\sum_i\Gamma_{ji}p_i\beta_i^1\), the inequalities
\(|\Gamma_{ji}|\le1\), \(\sum_i|p_i|=1\) give the same norm and difference bounds for each \(U_j^1\).

For the matrix directions, expand
\[
 \Delta(\beta\otimes h)
                 =\Delta\beta\otimes h_e+\beta_0\otimes\Delta h
 \tag{N.45}
\]
and sum with the absolute coefficients \(|p_i|\). The affine backward bounds are \(\|\beta_0^3\|\le211a^4\), \(\|\beta_0^2\|\le2110a^5\). Thus
\[
 \|V_e^2\|_{\rm HS}\le(17320)(4)a^6=69280a^6,\qquad
 \|V_e^3\|_{\rm HS}\le(866)(43)a^6=37238a^6,
\]
\[
 \|V_0^2\|_{\rm HS}\le(2110)(2)a^6=4220a^6,\qquad
 \|V_0^3\|_{\rm HS}\le(211)(21)a^6=4431a^6,
\]
\[
 \|\Delta V^2\|_{\rm HS}
 \le[(15210)(4)+(2110)(2)]a^5e=65060a^5e,
\]
\[
 \|\Delta V^3\|_{\rm HS}
 \le[(655)(43)+(211)(22)]a^5e=32807a^5e.
 \tag{N.46}
\]
This also gives a direct finite norm comparison for the parameter directions, though their positivity was already proved for every \(e>0\) in Section N.2.

For the preactivation directions the exact difference formulas from (N.5) are
\[
 \Delta U_j^2=(\Delta V^2)h_{j,e}^1+V_0^2\Delta h_j^1
                 +A[a\Delta U_j^1+(d_{j,e}^1-a)U_{j,e}^1],
\]
\[
 \Delta U_j^3=(\Delta V^3)h_{j,e}^2+V_0^3\Delta h_j^2
                 +B[a\Delta U_j^2+(d_{j,e}^2-a)U_{j,e}^2].
 \tag{N.47}
\]
The nonlinear middle norm satisfies
\[
 \|U_{j,e}^2\|
 \le[(69280)(4)+10\cdot2\cdot346400]a^7
                                      =7205120a^7.
 \tag{N.48}
\]
Using (N.41), (N.46) in the first line of (N.47) gives
\[
 \|\Delta U_j^2\|
 \le[(65060)(4)+(4220)(2)+10(325300+346400)]a^6e
 =6985680a^6e<7\cdot10^6a^6e.
 \tag{N.49}
\]
The second line, with (N.48)–(N.49), gives
\[
 \|\Delta U_j^3\|
 \le[(32807)(43)+(4431)(22)+10(6985680+7205120)]a^7e
 =143416183a^7e<1.5\cdot10^8a^7e.
 \tag{N.50}
\]
Consequently a common simple bound is
\[
                 \|\Delta U_j^\ell\|\le C(a)e,\quad\ell=2,3,
                 \qquad C(a)=2\cdot10^8a^7.
 \tag{N.51}
\]

Choose
\[
                              0<e\le(10^{10}a)^{-1}.
 \tag{N.52}
\]
Then \(C(a)e\le a^6/50\). The affine lower bounds (N.39) are preserved by more than one half, since \(a\ge1\) and
\[
 \frac{a^6}{50}<\frac{a^7}{18\sqrt5},\qquad
 \frac{a^6}{50}<\frac{a^6}{18}\sqrt{\frac37}.
 \tag{N.53}
\]
For the first scalar inequality, \(18\sqrt5<45<50\); for the second, \(18\sqrt{7/3}<36<50\). The triangle inequality therefore proves \(U_j^2\ne0,U_j^3\ne0\) for every sample at the chosen positive nonlinearity. Their feature directions are nonzero as well because \(\phi'\ge a\). The activation rule (M.21) is smaller than the cutoff (N.52). Together with Section N.2 this proves nonzero preactivation and feature directions in every layer and sample.

### N.6. Physical initial accelerations

Consider the strong uncut physical solution constructed in Parts G and V. At time zero \(C_0=0\), so every residual-free backward field \(b_i^\ell(0)\) and every hidden raw velocity vanish. The initialized predictions are zero and \(r_i(0)=-y_i=-3p_i\). The readout equation gives
\[
                  C'(0)=\sum_i y_i h_i^3=3H,\qquad
                  C(t)/t\longrightarrow3H\quad\text{in }H_3.
 \tag{N.54}
\]
The hidden fields are continuous in their \(L^2\) norms. By Lemma F.5, bounded multiplication by the continuously varying gate gives
\[
 b_i^3(t)/t
     =\phi'(z_i^3(t))\,C(t)/t\longrightarrow3\beta_i^3.
\]
Operator-norm convergence \(B(t)^*\to B^*\), boundedness of these actions, and another application of F.5 then give \(b_i^2(t)/t\to3\beta_i^2\). The identical explicit sequence with \(A(t)^*\) and the first-layer gate gives
\[
                 b_i^\ell(t)/t\longrightarrow3\beta_i^\ell
                 \quad\text{in }H_\ell,\qquad\ell=1,2,3.
 \tag{N.55}
\]
For example split
\(B(t)^*[b_i^3(t)/t]-3B^*\beta_i^3\)
into \(B(t)^*[b_i^3(t)/t-3\beta_i^3]
+3(B(t)^*-B^*)\beta_i^3\); both terms tend to zero. This states every needed incoming-field step without assuming pointwise uniform gates.

Divide the hidden equations (M.12) by \(t\). Use \(r_i(t)\to-3p_i\), (N.55), forward-field continuity, and the rank-one norm inequality. We obtain in the hidden raw Hilbert space
\[
                   \theta_h'(t)/t\longrightarrow9V.
 \tag{N.56}
\]
Thus the right second derivative exists at zero and equals \(9V\) in each block. Integrating the \(o(t)\) remainder in (N.56) yields
\[
                   \theta_h(t)-\theta_h(0)=\tfrac92t^2V+o(t^2).
 \tag{N.57}
\]
The integral estimate follows directly: if the velocity error is bounded by \(\eta s\) for \(0<s<t_\eta\), its integral to \(t<t_\eta\) is bounded by \(\eta t^2/2\).

The strong forward chain and product rules give
\[
 (z_j^1)'=(w')\cdot x_j,\qquad
 (z_j^2)'=A'h_j^1+A[\phi'(z_j^1)(z_j^1)'],
\]
\[
                    (z_j^3)'=B'h_j^2+B[\phi'(z_j^2)(z_j^2)'].
 \tag{N.58}
\]
Divide these identities successively by \(t\), use (N.56) and Lemma F.5, and compare with (N.5). This proves
\[
 \frac{(z_j^\ell)'(t)}t\longrightarrow9U_j^\ell,\qquad
 \frac{(h_j^\ell)'(t)}t
        =\phi'(z_j^\ell(t))\frac{(z_j^\ell)'(t)}t
                                    \longrightarrow9d_j^\ell U_j^\ell.
 \tag{N.59}
\]
All first velocities at zero are zero. Therefore the initial second derivatives are
\[
                      (z_j^\ell)''(0)=9U_j^\ell,\qquad
                      (h_j^\ell)''(0)=9\phi'(Z_j^\ell)U_j^\ell.
 \tag{N.60}
\]
They are nonzero in \(L^2\) by Sections N.2 and N.5. In the half-line time domain these are right derivatives at its initial endpoint. No assertion of a second Fréchet derivative of the ambient nonlinear activation map is involved.

### N.7. The projected total kernel changes

Put \(f_p=\sum_i p_if_i\), and let \(g_h(t)\) be the hidden part of its raw gradient. The scalar prediction differentiability and raw metric identities in Part F give exactly
\[
 \kappa(t)=p^T\Big(\sum_{\ell=1}^4K^\ell(t)\Big)p
           =\|g_h(t)\|_{\rm hidden}^2+\|H(\theta_h(t))\|_3^2.
 \tag{N.61}
\]
The hidden gradient has components
\[
 d^{-1}\sum_i p_i b_i^1(t)x_i,\qquad
 \sum_i p_i b_i^2(t)\otimes h_i^1(t),\qquad
 \sum_i p_i b_i^3(t)\otimes h_i^2(t).
\]
Equation (N.55) and forward continuity consequently imply
\[
                  g_h(t)/t\longrightarrow3V,\qquad
                  \|g_h(t)\|_{\rm hidden}^2
                          =9t^2\|V\|_{\rm hidden}^2+o(t^2).
 \tag{N.62}
\]
At initialization this hidden gradient is zero.

For the readout term in (N.61), use the scalar Fréchet differential (N.9) and the raw displacement (N.57):
\[
 {\cal E}(\theta_h(t))
 ={\cal E}(\theta_h(0))
    +\left\langle V,\tfrac92t^2V+o(t^2)\right\rangle_{\rm hidden}
    +o(t^2)
 ={\cal E}(\theta_h(0))+\tfrac92t^2\|V\|_{\rm hidden}^2+o(t^2).
\]
Since \(\|H\|_3^2=2{\cal E}\), this gives the second contribution
\[
 \|H(\theta_h(t))\|_3^2
       =\|H(\theta_h(0))\|_3^2+9t^2\|V\|_{\rm hidden}^2+o(t^2).
 \tag{N.63}
\]
Adding (N.62) and (N.63) proves
\[
                 \kappa(t)=\kappa(0)+18t^2\|V\|_{\rm hidden}^2+o(t^2),
                 \qquad\|V\|_{\rm hidden}>0.
 \tag{N.64}
\]
For all sufficiently small positive \(t\), the remainder is smaller in magnitude than \(9t^2\|V\|_{\rm hidden}^2\), so \(\kappa(t)>\kappa(0)\). This proves a change of the actual projected total kernel along physical training, and completes all initial-motion assertions.

