Independent adversarial mathematical audit B

Verdict: PASS for the actual stated finite RawGF theorem. Theorem 1, Lemma 2, and Theorem 3, including the uniform bounds in Section 7, follow with the numerical constants printed in the source. I found no required mathematical correction or counterexample under their stated hypotheses. This verdict concerns exactly the finite-dimensional dynamics (5).

The sole mathematical input was /tmp/l2-two-sample-proof-0ywjpp/COMPACT_FIRST_LINEAR_TAIL_TOP_CLOCK.md, read entirely: 564 lines, 23,903 bytes, Sections 1–8 and equations (1)–(49). No referenced source, project context, dependency, other review, skill instruction, subagent, experiment, or external import was used.

Source SHA-256 before reading:
cb0a9abb96ede054190b54cf883f9bd51081b39c3d7b36689eaa335268301e8b

Source SHA-256 after the audit:
cb0a9abb96ede054190b54cf883f9bd51081b39c3d7b36689eaa335268301e8b

The hashes agree. The source was not edited.

1. Model, frozen rows, and exact metric energy: (1)–(11).

The activation assumptions give \(\phi_1'=p\), \(|\phi_1|\le A\), Lipschitz constant \(P\), and the values \(+A,-A\) on the two saturated tails. Equation (2) gives \(\phi_2(0)=0\), \(1\le\phi_2'\le M=1+\varepsilon\), hence both \(|\phi_2(z)|\le M|z|\) and global Lipschitz constant \(M\).

For a row saturated at both inputs, fixing that row makes both \(p(z^1_{ja})\) identically zero. Solving the remaining smooth ODE with this fixed row therefore solves the full ODE; local uniqueness proves invariance. This includes coordinates equal to \(\pm R\), where smooth compact support forces \(p=0\). The frozen same-sign and opposite-sign feature rows are respectively \(\pm A(1,1)\) and \(\pm A(1,-1)\). Their summed Gram has eigenvalues
\[
 2A^2N_s/n,\qquad 2A^2N_o/n.
\]
Thus (7), including its factor 2, is exact. The other, moving rows add positive semidefinite outer products.

The output derivatives with respect to \(W^1,W^2,W^3\) are respectively
\[
 \delta^1_ax_a^T/n,\qquad
 \delta^2_a(h^1_a)^T/n,\qquad h^2_a/n.
\]
For the unhalved loss \(L=\sum_a r_a^2\), (5) is negative gradient flow with inverse metric factors \(n/d,1,n\). Consequently the metric factors in the squared-speed identity are \(d/n,1,1/n\). Substitution gives precisely
\[
 \dot r=-2Kr,\qquad
 -\dot L=4r^TKr
 =\frac d n\|\dot W^1\|_F^2+\|\dot W^2\|_F^2+
       \frac1n\|\dot W^3\|_2^2.
\]
The three kernel terms are the Grams of
\(\delta^1_ax_a^T/\sqrt{nd}\),
\(\delta^2_a(h^1_a)^T/n\), and \(h^2_a/\sqrt n\).
This checks every factor \(2,4,n,d\) in (8)–(10), including possible negative off-diagonal entries of the input Gram.

Integrating each nonnegative squared speed costs at most \(L(0)\); Cauchy–Schwarz gives all three bounds (11). Between any two existence times \(u<v\), the corresponding normalized displacement is at most \(\sqrt{(v-u)L(0)}\). At any finite maximal endpoint this makes all parameters Cauchy and gives a finite limiting state. Smooth local existence there extends the solution. Global finite-time existence therefore does not assume a frozen reservoir, a loss margin, or an already finite infinite-horizon clock.

2. Coercivity and centered balance with moving features: (12)–(20).

Writing \(d_{ia}=\phi_2'(z^2_{ia})\), direct expansion gives
\[
 (K_2)_{ab}=(G_1)_{ab}\frac1n
                  \sum_i(W_i^3)^2d_{ia}d_{ib}.
\]
Thus (12) is exactly a sum of congruences:
\[
 K_2=\frac1n\sum_i(W_i^3)^2D_iG_1D_i
 \succeq\frac\gamma n\sum_i(W_i^3)^2D_i^2
 \succeq\gamma b^2I.
\]
The lower bound uses \(D_i^2\succeq I\), not a generally invalid entrywise matrix comparison. It proves \(\dot L\le-4\gamma b^2L\) and, wherever \(s>0\), \(\dot s\le-2\gamma b^2s\). At \(s=0\) all parameter velocities vanish, so constant continuation is valid.

Differentiating the homogeneity defect gives
\[
 D'(z)=-2\varepsilon z^2/(1+z^2)^2.
\]
Its limits are \(\mp\varepsilon\pi/2\) at \(\pm\infty\), proving the exact supremum \(D_*=\varepsilon\pi/2\) in (14).

The bound \(\sum_a|r_a|\le\sqrt2s\) and \(\|h^1_a\|\le A\sqrt n\) yield
\[
 \|\dot B\|_F\le 2\sqrt2MA\,sb=C_Bsb.
\]
Differentiating only the parameter norms gives
\[
 (a^2-b^2)'=-\frac4n\sum_a r_a
 \left\langle W^3,
 D(z^2_a)-\phi_2'(z^2_a)\odot A_0h^1_a\right\rangle.
\]
This is (17): \(Bh^1_a=z^2_a-A_0h^1_a\) is an instantaneous substitution, not a differentiation of \(Bh^1_a\). There is therefore no omitted term involving \(\dot h^1_a\). For every time, including when unsaturated first rows move,
\[
 \|D(z^2_a)\|\le D_*\sqrt n,\qquad
 \|\phi_2'(z^2_a)\odot A_0h^1_a\|
       \le Ma_0A\sqrt n.
\]
Together these prove \(C_D=4\sqrt2(D_*+Ma_0A)\). Integrating from \(a(0)=0\) gives the sign and initial term exactly:
\[
 |a^2-b^2+b_0^2|\le C_DX.
\]
Hence every inequality in (16), (18), and (19) follows, including
\(a\le b+\sqrt{C_DX}\) and \(b^2\le a^2+b_0^2+C_DX\).

Finally,
\[
 \|H^2\|_F\le M\|W^2\|_{\rm op}A\sqrt{2n},
 \qquad
 \|f\|\le\sqrt2MA\,b(a_0+a).
\]
This verifies \(C_f=\sqrt2MA\) and the entire prediction estimate (20). Centering has correctly retained the initial operator norm \(a_0\); an initial Frobenius norm has not entered these constants.

3. Infinite-horizon closure and loss decay: (21)–(29).

An actual margin gives \(s_0<\sqrt2\) and
\(\|f(t)\|\ge\sqrt2-s(t)\ge\eta=\sqrt2-s_0>0\) for \(t\ge t_0\).
If \(b\le1\), the preceding prediction estimate implies
\[
 \eta\le C_f b(a_0+1+\sqrt{C_D})(1+\sqrt X).
\]
If \(b\ge1\), \(b\ge c/(1+\sqrt X)\) follows from \(c\le1\). Thus (22)–(23) hold with exactly the stated constant \(c\). In particular, a zero readout after the margin is impossible.

The integral in (24) can be checked by substituting \(u=v^2\):
\[
 F(x)=2(\sqrt x-\log(1+\sqrt x)),\qquad
 F'(x)=\frac1{1+\sqrt x},
\]
where the derivative at zero is the continuous right derivative \(1\).
Since \(X'=sb\ge0\),
\[
 \dot s\le-2\gamma bX'
          \le-2\gamma c\,\frac{X'}{1+\sqrt X}.
\]
Integration proves (25). Norms are absolutely continuous on compact time intervals; if the residual reaches zero, it and \(X\) remain constant. This argument needs neither division by \(s\) at zero nor an inverse clock.

The maximum of \(\log(1+u)-u/2\) on \(u\ge0\) is \(\log2-1/2\), attained at \(u=1\). The weaker bound used in the source, \(\log(1+u)\le u/2+\log2\), is valid. It implies
\[
 \sqrt{X(t)}
 \le F(X_0)+\frac{s_0}{2\gamma c}+2\log2
 \quad(t\ge t_0).
\]
The right side is positive, so squaring is legitimate and verifies \(\overline X\) in (26). Monotonicity of \(X\) extends the bound to \(t<t_0\).
Using \(a\le C_BX\) and \(b^2\le a^2+b_0^2+C_DX\) gives exactly
\[
 \overline a=C_B\overline X,\quad
 \overline b^2=C_B^2\overline X^2+b_0^2+C_D\overline X,\quad
 U=a_0+\overline a,\quad
 b(t)\ge\beta=\frac c{1+\sqrt{\overline X}}\ (t\ge t_0).
\]
The rate in (28) is consequently \(4\gamma\beta^2\) for \(L\), and \(2\gamma\beta^2\) for \(s\). Integrating the latter yields exactly
\[
 \int_0^\infty s\le t_0\sqrt{L(0)}
                  +\frac{s_0}{2\gamma\beta^2}.
\]
Before invoking any infinite-horizon conclusion, (11) already gives
\[
 b(t)\le b_0+\sqrt{tL(0)},\qquad
 X_0\le\sqrt{L(0)}\,b_0t_0+\frac23L(0)t_0^{3/2}.
\]
This checks the factor \(2/3\) and removes a possible circularity in defining the all-time constants. The edge cases \(t_0=0\) and \(L(t_0)=0\), including \(\delta=2\), cause no failure.

4. Total variation and limits: (30)–(32).

The equations, input norms, and \(\|\delta^1_a\|\le PMU\sqrt n\,b\) give
\[
 \frac{\|\dot W^3\|}{\sqrt n}\le C_BU s,\qquad
 \sqrt{\frac d n}\|\dot W^1\|_F
      \le2\sqrt2PMU\,sb,\qquad
 \frac{\|q_{:,a}\|}{\sqrt n}\le2MU|r_a|b\le2MU\,sb.
\]
The \(W^1\) normalization follows explicitly from
\(\sqrt{d/n}(2/d)\|x_a\|=2/\sqrt n\).
Integration gives respectively \(C_BUS_\infty\),
\(2\sqrt2PMU\overline X\), and \(2MU\overline X\);
the second-layer variation is at most \(C_B\overline X\).
All factors in (30)–(32) are therefore valid. At each fixed finite \(n,d\), these normalized bounds imply ordinary finite total variation for every parameter vector. Completeness yields finite parameter limits, and continuity of the network together with \(L\to0\) yields limiting predictions exactly \(y\). Infinite-time convergence is not being deduced from squared-speed integrability alone.

5. The actual short-time margin: (33)–(36).

The energy displacement bound implies
\[
 \frac{\|H^1(t)-H^1(0)\|_F}{\sqrt n}
 \le\frac{P\sqrt{2d}\|W^1(t)-W^1(0)\|_F}{\sqrt n}
 \le\sqrt2P\sqrt{tL(0)}.
\]
Decomposing the preactivation difference as \(BH^1(0)+W^2(t)(H^1(t)-H^1(0))\) gives precisely
\[
 \frac{\|H^2(t)-H^2(0)\|_F}{\sqrt n}
 \le M\sqrt{2tL(0)}
          [A+P(a_0+\sqrt{tL(0)})].
\]
Thus first-feature movement is included in (35).
For \(t\le\tau\), its square is at most
\[
 2M^2t\overline L[A+P(a_0+1)]^2\le\kappa/4,
\]
using both terms in the minimum (33). The denominator 8 there is correct. Perturbing the smallest singular value of \(H^2/\sqrt n\) by at most \(\sqrt\kappa/2\) leaves it at least \(\sqrt\kappa/2\), so \(K_3(t)\succeq\kappa I/4\). Dissipation gives \(L(t)\le L(0)e^{-\kappa t}\).

If \(L(0)\le2e^{\kappa\tau/2}\), then
\[
 L(\tau)\le2e^{-\kappa\tau/2}=2-\delta_*,
 \qquad \delta_*=2(1-e^{-\kappa\tau/2})\in(0,2).
\]
Every factor and exponent in Lemma 2 is correct. This controls an entire deterministic interval; it does not replace interval control by an initial-derivative assertion or require a readout-coordinate maximum.

6. Gaussian event, actual readout, and width threshold: (37)–(46).

The independent first rows in (37) give Gaussian input pairs of variances 1 and covariance \(\rho\), independently of \(d\). For \(|\rho|<1\), the density is positive on every open corner, so both \(m_s,m_o\) in (38) are strictly positive. For either count with success probability \(m\),
\[
 \Pr(N/n<m/2)\le\frac{nm(1-m)}{(nm/2)^2}
              =\frac{4(1-m)}{nm}.
\]
The union bound proves (39) and the event gives
\(\gamma_n\ge A^2\min(m_s,m_o)=\gamma\). Independence between the two counts is unnecessary.

Conditioned on the first-layer realization, the second preactivation rows are independent \(N(0,G)\), with \(G=H^TH/n\). On the reservoir event, \(G\succeq\gamma I\) and \(G_{aa}\le A^2\). Write \(Z=U+\sqrt\gamma\,\xi\), where \(U\) has covariance \(G-\gamma I\) and the coordinates of \(\xi\) are independent standard normals independent of \(U\). A singular covariance for \(U\) is harmless. Since \(|\phi_2(t)-\phi_2(t')|\ge|t-t'|\), the independent-copy variance identity gives
\(\operatorname{Var}(\phi_2(T))\ge\operatorname{Var}(T)\).
Conditional on \(U\), this implies
\[
 \operatorname{Var}(v^T\phi_2(Z)\mid U,H)
       \ge\gamma\|v\|^2.
\]
Taking expectations and retaining the nonnegative conditional-mean square proves (40). In particular, negative correlation creates no gap; an entrywise monotonicity assertion about covariances has not been used.

For a Gaussian of variance \(\sigma^2\), the fourth derivative at zero of its moment generating function \(e^{\sigma^2t^2/2}\) gives \(3\sigma^4\). Therefore
\[
 \mathbb E[V_a^2V_b^2\mid H]\le3M^4A^4.
\]
Summing the variances of the four entries of the empirical \(2\times2\) second-moment matrix gives \(12M^4A^4/n\). Off-diagonal entries are correctly counted twice, and need not be independent. A Frobenius error at most \(\gamma/2\) preserves a smallest eigenvalue of at least \(\gamma/2=\kappa\). Markov at squared threshold \(\gamma^2/4\) gives exactly \(48M^4A^4/(n\gamma^2)\) in (41).

The norm estimates (42)–(43) also have the stated constants. A maximal \(1/4\)-separated subset of the unit sphere has at most \(9^n\) elements by packing balls of radius \(1/8\) in a ball of radius \(9/8\), and is a \(1/4\)-net. Approximating each of the two unit vectors in a maximizing bilinear form costs at most \(\|A_0\|_{\rm op}/4\), hence
\[
 \|A_0\|_{\rm op}\le2\max_{\text{two nets}}|u^TA_0v|.
\]
Each fixed bilinear form has variance \(1/n\), and the exponential-moment bound at level 4 is \(2e^{-8n}\). Multiplying by \(9^{2n}\) gives \(2e^{-(8-2\log9)n}\); \(8-2\log9>0\).
For the actual readout \(W_i^3(0)=\xi_i/n\),
\[
 b_0^2=n^{-3}\sum_i\xi_i^2,\qquad
 \Pr(b_0>2/n)
 \le e^{-n}\bigl(\mathbb E e^{\xi^2/4}\bigr)^n
 =e^{-(1-\frac12\log2)n}.
\]
Here \(\mathbb E e^{\xi^2/4}=\sqrt2\), and the exponent coefficient is positive. There is no zero-readout substitution or erroneous readout scaling.

With \(a_0=8\), \(q_0=2MAa_0\), and \(b_0\le2/n\), the deterministic prediction estimate gives
\[
 \|f(0)\|\le\sqrt2q_0/n,\qquad
 L(0)\le2(1+q_0/n)^2.
\]
The second and third entries of the maximum in (44) respectively ensure
\[
 1+q_0/n\le\sqrt2,\qquad
 1+q_0/n\le e^{\kappa\tau/4}.
\]
These give exactly \(L(0)\le4\) and \(L(0)\le2e^{\kappa\tau/2}\). The ceiling, minimum width 2, and all exponents in (44)–(45) are valid. The parameters \(\gamma,\kappa,\tau,q_0,N_*\) are fixed independently of \(n,d\).

For precision, let \(E_K=\{K_3(0)\succeq\kappa I\}\). The probability calculation uses
\[
 \Pr(E_F\cap E_K^c)
 =\mathbb E\!\left[1_{E_F}\Pr(E_K^c\mid W^1(0))\right]
 \le\frac{48M^4A^4}{n\gamma^2}.
\]
Combining this with \(\Pr(E_F^c)\) and the two norm failure bounds proves exactly \(p_n\) in (46). It does not assume independence between \(K_3(0)\) and the operator norm of \(A_0\). At fixed stated activation and correlation parameters, \(p_n\to0\); clipping \(1-p_n\) below at zero is valid. Lemma 2 supplies the margin for this very trajectory, and the same event supplies Theorem 1's frozen Gram hypothesis.

7. Uniform constants and precise endpoint scope: (47)–(49), Section 8.

On the successful event, \(s(\tau)\le s_*=\sqrt2e^{-\kappa\tau/4}\), \(L(0)\le4\), and \(b_0\le2/n\le1\). Thus \(\eta\ge\eta_*>0\) and \(c\ge c_*\). Equation (29) gives
\[
 X(\tau)\le2\tau+\frac83\tau^{3/2}=X_{\rm pre}.
\]
Since \(F\) is increasing, the closure proof consequently gives exactly
\[
 X_*
 =\left(F(X_{\rm pre})+\frac{s_*}{2\gamma c_*}
                       +2\log2\right)^2.
\]
The remaining uniform replacements follow without any realization-dependent quantity:
\[
 U_*=8+C_BX_*,\quad
 b_*^2=C_B^2X_*^2+1+C_DX_*,\quad
 \beta_*=\frac{c_*}{1+\sqrt{X_*}},\quad
 S_*=2\tau+\frac{s_*}{2\gamma\beta_*^2}.
\]
In particular \(b\ge\beta_*\) after \(\tau\), and the loss bound is
\(L(t)\le s_*^2e^{-4\gamma\beta_*^2(t-\tau)}\).
This checks the \(8/3\), readout-square term 1, and all rate constants in (47)–(48). Replacing the constants in (31)–(32) is justified by the same inequalities. Finally,
\[
 \|z^2_a(t)\|/\sqrt n
 \le\|W^2(t)\|_{\rm op}\|h^1_a(t)\|/\sqrt n
 \le AU_*,
\]
which verifies (49). These are normalized moment and operator bounds; fixed-width parameter convergence does not assert uniform bounds on unnormalized coordinate maxima.

The separate zero-readout diagnostic is correct: \(f(0)=0\), \(r(0)=-y\), and \(K_1(0)=K_2(0)=0\), so
\(\dot L(0)=-4y^TK_3(0)y<0\) if \(K_3(0)\succ0\).
Continuity then yields a strictly smaller loss at a positive time. The Gaussian proof above does not use this diagnostic.

Both endpoint exclusions are substantive and correctly stated. At \(\rho=1\), the equal-norm inputs coincide, so every predictor has \(f_1=f_2=u\) and \(L=2+2u^2\ge2\); the opposite-sign reservoir is absent. At \(\rho=-1\), the inputs are antiparallel, and oddness gives \(h^1_2=-h^1_1\); the first Gram has rank at most one and the same-sign reservoir is absent. This invalidates the positive two-dimensional Gram hypothesis at that endpoint, without establishing optimization failure there. No uniformity near either endpoint or success for every finite Gaussian draw is claimed.

The curvature statement is also accurate: differentiating (2) gives
\(\phi_2''(z)=-2\varepsilon z/(1+z^2)^2\), which is bounded, but (48) yields only \(|W_i^3|\le\sqrt n\,b_*\). The stated estimates therefore do not establish a width-uniform coordinatewise bound on the curvature product. This limitation does not enter any step of the finite theorem.

Required corrections: none found. In particular, no replacement is needed for any printed numerical constant in (1)–(49).

Optional tightening only: the exact logarithm maximum already computed above gives \(F(x)\ge\sqrt x+1-2\log2\). Thus \(2\log2\) in the definitions of \(\overline X\) and \(X_*\) can be replaced by the positive smaller constant \(2\log2-1\). The source deliberately uses a looser valid bound; changing it is unnecessary.

The principal attempted failure mechanisms—wrong gradient metric, lost first-feature transport, collapse of \(b\), a stalled or unbounded clock, squared-speed versus total-variation confusion, negative-correlation Gaussian coercivity, overlapping probability events, small nonzero readout, and hidden width dependence—are all resolved by the derivations above. The finite RawGF assertions pass this source-isolated audit as stated.
