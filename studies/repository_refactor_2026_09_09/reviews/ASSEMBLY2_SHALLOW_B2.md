**CLEAN.** Theorem SD and its restricted dyadic consequence are correct under the stated assumptions. I found no required mathematical corrections. The transported-defect identity, all constant recursions, derivative envelopes, expectation interchanges, cubic coefficient, and sharpness argument check out. Section 8 supplies no proof dependency.

I performed this audit independently, without delegation, external sources, numerical experiments, or inspection of other candidate packets, checkouts, studies, task history, or prior verdicts. All input files remain unchanged.

The complete read and integrity ledger is:

| Input | Lines read | Bytes | SHA-256 before and after |
|---|---:|---:|---|
| [shallow.md](/tmp/pde_assembly2_shallow_r1/shallow.md) | 1–551, all | 17,318 | `4321fc6bf9fdddedccb752072f3326134d514edbdd576c328923432e4345efd9` |
| [NOTATION.md](/tmp/pde_assembly2_shallow_r1/NOTATION.md) | 1–98, all | 5,110 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| [INPUTS.json](/tmp/pde_assembly2_shallow_r1/INPUTS.json) | 1–12, all | 286 | `0da4173c89588799ec10b57eb170a31998b68a74402c54f5e812c18a926a46e1` |

For both mathematical files, the initial and final hashes, byte counts, and line counts match `INPUTS.json`. The manifest does not contain its own hash; its final hash was checked against its initial hash.

I also personally read every line of the five required instruction files:

| Instruction file | Complete lines read |
|---|---:|
| `/etc/codex/skills/solve-math-rigorously/SKILL.md` | 1–115 |
| `/etc/codex/skills/investigate-conjectures/SKILL.md` | 1–185 |
| `/etc/codex/skills/investigate-conjectures/references/research-contract.md` | 1–99 |
| `/etc/codex/skills/investigate-conjectures/references/evidence-ledger.md` | 1–157 |
| `/etc/codex/skills/investigate-conjectures/references/adversarial-audit.md` | 1–121 |

Their scope, evidence, and adversarial checks were applied to the supplied proof, without expanding the task into research.

The mathematical checks follow in proof order.

**NOTATION.md, lines 1–98.** The shallow specialization respects the notation contract. With \(L=m=d=1\) and \(x_1=1\), the first preactivation equals \(u_i\), and the stored-readout convention gives
\[
f_{n,1}=\frac1n\sum_i a_i\phi(u_i).
\]
Consequently,
\[
n\,\partial_{a_i}f_{n,1}=\phi(u_i),\qquad
n\,\partial_{u_i}f_{n,1}=a_i\phi'(u_i).
\]
Thus the two mobilities \(n\) produce precisely the feature-ascent updates in SD1.

The general backward-coordinate formulas in the notation file also have the correct normalization: differentiating the readout contributes \(1/n\), and multiplying by \(n\) gives the displayed terminal \(\delta\); the earlier-layer formula then follows by the chain rule. The normalized pairing and rank-one representative \(uv^T/n\) are consistent with population contraction by expectation.

The chapter explicitly replaces the small-readout convention with independent order-one standard Gaussian stored readouts. No inference between those initialization regimes is used. Its population variables occupy the single specified mark space, and its derivative operator norms are ordinary Euclidean operator norms.

The clock distinction is substantive and correct. For the one-sample squared loss \((f-1)^2\), physical gradient flow with these mobilities would satisfy
\[
\dot a_i=2(1-f)\phi(u_i),\qquad
\dot u_i=2(1-f)a_i\phi'(u_i).
\]
Hence \(ds/dt=2(1-f)\) gives the feature-flow equations where this clock is positive. Exact raw loss GD still has a changing residual multiplier and is not SD1 with a fixed feature step.

The primitive convention also checks: for \(\phi'(z)=1/(1+z^2)\), \(F'(z)=1/\phi'(z)\) when \(F(z)=z+z^3/3\); for the displayed scaled arctangent activation, the primitive gains the factor \(10\). The continuous chain rule gives \(dF(u)/ds=a\), whereas a raw Euler increment generates additional finite-step terms. None of these clock or primitive observations is used to import a continuous-flow theorem into the candidate.

**§11.1, lines 9–74: model and quantitative statement.** Initialization, activation class, update ordering, observable, and step domain are specified. Both coordinates update simultaneously from their old values. The theorem covers every integer \(k\ge1\), with
\[
|h|k\le c_\phi=\frac1{16M},
\]
including negative steps.

The normalization \(E\phi(G)^2=1\) is compatible with the activation hypotheses. All terms defining \(J_\phi\) are integrable: bounded activation derivatives and linear growth of \(\phi\) bound its integrand by a constant depending on \(M\) times \(1+|G|+G^2\).

The theorem’s metric is the absolute error of a scalar expected output. Its width assertion concerns expectations at fixed finite step count and step size. The subsequent convergence assertion concerns terminal expected outputs in the uniform norm on a specified feature-time interval. These scopes are explicit and are not silently replaced by state-space or physical-time convergence.

**§11.2, lines 76–160: definition of the constant.** The recursion is finite and triangular. The \(X\)'s precede the \(\mathcal G\)'s and \(\mathcal B\)'s; these precede the \(\mathcal Z\)'s and \(T\)'s; the \(\mathcal H\)'s then precede the successive \(V\)'s. Each \(V_q\) uses only lower-indexed \(V\)'s. There is no circular dependence.

The exponential identity in SD5 is exact:
\[
4c\Lambda
=4\frac1{16M}(12MR)=3R,
\qquad P=e^{3R}.
\]
The constant in SD12 is the explicitly specified Gaussian integral
\[
B_\phi^{\rm sh}
=\frac1{2\pi}\int_{\mathbb R^2}
\mathcal C_M(1+|a|+|u|)
e^{-(a^2+u^2)/2}\,da\,du.
\]
Its only activation input is \(M\); it contains no trained trajectory, output derivative, or unstated continuity modulus. The justification of every recursive coefficient and of finiteness is checked below.

**§11.3, lines 162–211: width identification and exact defect.** Write
\[
\psi(a,u)=a\phi(u),\qquad
g(a,u)=(\phi(u),a\phi'(u)),\qquad
R(a,u)=1+|a|+|u|.
\]
The growth estimate follows directly:
\[
\begin{aligned}
R(E_{\alpha h}z)
&\le R(z)+\alpha|h|
   \bigl(|\phi(u)|+|a|\,|\phi'(u)|\bigr)\\
&\le(1+\alpha M|h|)R(z).
\end{aligned}
\]
In particular,
\[
|\psi(E_h^Nz_0)|
\le M(1+M|h|)^{2N}R(z_0)^2.
\]
This is Gaussian-integrable for every fixed finite \(N,h\).

Each neuron is the same deterministic function of its own independent initial pair. Independence and identical distribution therefore persist exactly, and linearity of expectation gives
\[
E f_{n,1}^N(h)=E_1[A_N\phi(U_N)]
\]
for every width \(n\). No law of large numbers or width-limit interchange is needed.

For \(C_h=E_{2h}\) and \(B_h=E_h\circ E_h\),
\[
B_hz-C_hz=h\bigl(g(z+hg(z))-g(z)\bigr)
=h^2\int_0^1Dg(z+\tau hg(z))[g(z)]\,d\tau.
\]
This verifies SD15, including its sign and its validity for negative \(h\).

To check the noncommuting telescoping step, define
\[
H_q=\psi(B_h^qC_h^{k-q}z).
\]
With \(x_q=C_h^{k-1-q}z\) and \(v_q=\psi\circ B_h^q\),
\[
H_q-H_{q+1}=v_q(C_hx_q)-v_q(B_hx_q).
\]
Summing over \(q=0,\ldots,k-1\), and integrating along the segment from \(C_hx_q\) to \(B_hx_q\), gives exactly
\[
\psi(C_h^kz)-\psi(B_h^kz)
=-h^2\sum_{q=0}^{k-1}\int_0^1
Dv_q(C_hx_q+\tau h^2b_h(x_q))[b_h(x_q)]\,d\tau.
\]
Thus SD16 is an exact transported-defect identity. It does not require \(B_h\) and \(C_h\) to commute.

**§11.4, lines 213–388: state bounds and derivative envelopes.** The interpolation is exactly
\[
C_hx+\tau h^2b_h(x)=(1-\tau)C_hx+\tau B_hx.
\]
Since \(R\) is convex, endpoint growth bounds control this segment. The allowances of at most \(4k\) pre-interpolation Euler coefficients and \(2k\) subsequent fine steps are valid upper bounds. They give
\[
R(z)\le e^{6M|h|k}R(z_0)
\le e^{3/8}R(z_0)<2R(z_0).
\]
The segment is not incorrectly counted as an Euler step.

For the local derivative norms, when \(1\le q\le4\), the first coordinate of \(D^qg\) has one activation-derivative term. The second has one term containing \(a\phi^{(q+1)}\) and \(q\) terms containing \(\phi^{(q)}\). On unit Euclidean directions this gives the sufficient estimate
\[
\|D^qg(z)\|\le M(1+|a|+q)\le6MR(z).
\]
For \(q=0\), \(\|g(z)\|_2\le MR(z)\). Similarly, \(D\psi=g\), while for \(2\le j\le4\),
\[
\|D^j\psi(z)\|\le M(|a|+j)\le5MR(z).
\]
Thus all derivative bounds used in the proof are at most \(\Lambda=12MR(z_0)\) on the relevant points. The assumed \(C^{12}\) regularity supplies every derivative used.

For a pre-defect path, the homogeneous tangent factors obey
\[
\prod_j\|I+\alpha_jhDg(y_j)\|
\le \exp\!\left(\Lambda|h|\sum_j\alpha_j\right)
\le P.
\]
This estimate is valid for either sign of \(h\); it requires no contractivity assumption.

The differentiated updates in SD21 have the correct coefficients. In particular,
\[
\frac{d^q}{dh^q}\bigl(hg(y(h))\bigr)
=h\frac{d^q}{dh^q}g(y(h))
+q\frac{d^{q-1}}{dh^{q-1}}g(y(h)),
\]
which produces the displayed factors \(2\) and \(3\), and the third-order mixed chain-rule factor \(3\).

Using \(\sum\alpha_j\le4k\), \(|h|k\le c\), and the lower-order derivative bounds, the source sums divided by \(k^q\) are:

| Order \(q\) | Normalized pre-defect source bound |
|---|---|
| \(1\) | \(4\Lambda\) |
| \(2\) | \(8\Lambda X_1+4c\Lambda X_1^2\) |
| \(3\) | \(12\Lambda(X_1^2+X_2)+4c\Lambda(X_1^3+3X_1X_2)\) |

Multiplication by \(P\) gives exactly SD6. Initial derivatives vanish because \(z_0\) does not depend on \(h\). This verifies all three \(X_q\) bounds, uniformly over path prefixes.

For the compositions defining the local defect, the chain rule gives the four bounds
\[
\Lambda,\quad
\Lambda X_1k,\quad
\Lambda(X_2+X_1^2)k^2,\quad
\Lambda(X_3+3X_1X_2+X_1^3)k^3.
\]
These apply both to \(g(x_q)\) and to
\(Dg(x_q+\tau hg(x_q))\). In the latter case, three step derivatives require \(D^4g\), which is covered by SD19. The appended coefficient \(\tau\le1\) keeps the argument path within the pre-defect allowance.

Leibniz’s rule consequently gives SD7 and SD23. Explicitly, the four product envelopes are
\[
\begin{aligned}
\mathcal B_0&=\mathcal G_0^2,\\
\mathcal B_1&=2\mathcal G_0\mathcal G_1,\\
\mathcal B_2&=2\mathcal G_0\mathcal G_2+2\mathcal G_1^2,\\
\mathcal B_3&=2\mathcal G_0\mathcal G_3+6\mathcal G_1\mathcal G_2.
\end{aligned}
\]
Integration over the unit interval introduces no additional factor.

For the interpolation derivatives,
\[
\partial_h^q(h^2b_h)
=h^2\partial_h^qb_h
+2qh\,\partial_h^{q-1}b_h
+q(q-1)\partial_h^{q-2}b_h
\]
is exact, with nonexistent derivative orders omitted. Its norm is bounded by
\[
\left(c^2\mathcal B_q+2qc\mathcal B_{q-1}
+q(q-1)\mathcal B_{q-2}\right)k^{q-2}.
\]
Since \(k\ge1\), this is bounded by the same coefficient times \(k^q\). Adding the \(C_hx_q\) derivative bound proves SD8. The deliberately loose replacement of \(k^{q-2}\) by \(k^q\) is valid for all three orders, including \(q=1\).

For the remaining fine path, there are at most \(2k\) steps, and its initial derivative bounds are \(\mathcal Z_qk^q\). The normalized initial-plus-source bounds become:

| Order \(q\) | Bound before homogeneous amplification |
|---|---|
| \(1\) | \(\mathcal Z_1+2\Lambda\) |
| \(2\) | \(\mathcal Z_2+4\Lambda T_1+2c\Lambda T_1^2\) |
| \(3\) | \(\mathcal Z_3+6\Lambda(T_1^2+T_2)+2c\Lambda(T_1^3+3T_1T_2)\) |

Their multiplication by \(P\) verifies SD9. The actual homogeneous bound here is at most \(e^{2c\Lambda}\le P\), so reusing \(P\) is safe.

The same chain-rule expressions, now with \(T\) in place of \(X\), give exactly \(\mathcal H_0,\ldots,\mathcal H_3\) in SD10. They apply to both \(Dg\) and \(D\psi\) along the final path.

For direction transport, let \(\omega\) start at \(b_h(x_q)\). Differentiating
\[
\omega^+=\omega+hDg(z)\omega
\]
gives SD25 exactly. Separating the homogeneous term leaves two kinds of sources. After summing at most \(2k\) steps and dividing by \(k^q\), they are bounded by
\[
2c\sum_{v=1}^q\binom qv\mathcal H_vV_{q-v}
\]
and
\[
2q\sum_{v=0}^{q-1}\binom{q-1}v
\mathcal H_vV_{q-1-v},
\]
respectively. The initial contribution is \(\mathcal B_q\); homogeneous amplification contributes \(P\). This verifies the entire \(V_q\) recursion in SD11, starting from \(V_0=P\mathcal B_0\).

Finally, differentiating \(D\psi(z)[\omega]\) gives
\[
\left|\partial_h^j\bigl(D\psi(z)[\omega]\bigr)\right|
\le k^j\sum_{v=0}^j\binom jv\mathcal H_vV_{j-v},
\qquad 0\le j\le3.
\]
There are \(k\) transported defects. Therefore the third derivative is bounded by
\[
k^4\sum_{v=0}^3\binom3v\mathcal H_vV_{3-v}
=6\mathcal C_M(R)k^4.
\]
Both the factor \(6\) and the power \(k^4\) in SD27 are correct.

The finiteness and expectation-interchange argument is also sufficient. Every envelope is a finite polynomial in \(c,\Lambda,P\) with nonnegative coefficients. Substituting \(\Lambda=12MR\) and \(P=e^{3R}\) bounds it by a polynomial in \(R\) times \(e^{CR}\), with finite constants depending only on \(M\) and the displayed recursion.

For any finite \(p,\lambda\ge0\),
\[
(1+|x|)^p e^{\lambda|x|}e^{-x^2/2}
\]
is integrable, because its exponential factor is bounded by \(e^{-x^2/4}\) outside a finite interval. Also,
\[
1+|a|+|u|\le(1+|a|)(1+|u|).
\]
The two independent Gaussian integrations therefore control every required envelope.

In particular, \(B_\phi^{\rm sh}<\infty\). For each fixed \(k\), SD26 supplies integrable majorants for \(Q_k\) and all its first three derivatives, uniformly over the stated step interval. Integrating the fundamental theorem of calculus and passing expectations through the resulting integrals justifies the three differentiations. Equivalently, one may first restrict the marks to a bounded set and then let the Gaussian-integrable tail bound tend to zero. There is no unsupported expectation/derivative interchange and no width limit involved here.

**§11.5, lines 390–490: parity and cubic coefficient.** The symmetry holds pathwise:
\[
A_j(-h;-a_0,u_0)=-A_j(h;a_0,u_0),\qquad
U_j(-h;-a_0,u_0)=U_j(h;a_0,u_0).
\]
It follows by induction from the simultaneous updates. Since changing \(a_0\) to \(-a_0\) preserves its joint law with \(u_0\), each \(F_{N,1}\) is odd.

Thus \(D_k(h)=h^2\overline Q_k(h)\) is odd. The established \(C^3\) regularity makes \(\overline Q_k\) odd also at zero, giving
\[
\overline Q_k(0)=\overline Q_k''(0)=0.
\]
Taylor’s formula with integral remainder then gives exactly SD30. Using
\[
\sup|\overline Q_k'''|\le6B_\phi^{\rm sh}k^4
\]
yields
\[
|\overline Q_k(h)-h\overline Q_k'(0)|
\le B_\phi^{\rm sh}k^4|h|^3.
\]
Multiplication by \(h^2\) gives the claimed fifth-order remainder. Reversing integration orientation proves the same bound for negative \(h\).

For an independent check of the coefficient, evaluate all vector fields at the initial point and set
\[
b=Dg[g],\qquad c_1=Dg[b],\qquad c_2=D^2g[g,g].
\]
At \(h=0\), all iterates equal that point. Differentiating the recursion gives
\[
z_N'=Ng,\qquad z_N''=N(N-1)b.
\]
The third-derivative increment at step \(j\) is
\[
3j(j-1)c_1+3j^2c_2.
\]
Using
\[
\sum_{j=0}^{N-1}j(j-1)=2\binom N3,\qquad
\sum_{j=0}^{N-1}j^2=\frac{N(N-1)(2N-1)}6
\]
proves SD31, including both coefficients.

Because \(g=\nabla\psi\), its Jacobian is symmetric. Consequently,
\[
D\psi[Dg[b]]
=g^TDg\,b=(Dg\,g)^Tb=\|b\|_2^2,
\]
and the other two identities in SD32 follow from the same Hessian and third-derivative symmetries.

Writing
\[
\mathsf S=E_1D^3\psi[g,g,g],\qquad
\mathsf H=E_1\|Dg[g]\|_2^2,
\]
the third derivative of the composite observable has:

- an \(\mathsf S\)-coefficient
  \[
  N^3+\frac{N(N-1)(2N-1)}2
  =\frac{N(4N^2-3N+1)}2;
  \]
- an \(\mathsf H\)-coefficient
  \[
  N(N-1)(N-2)+3N^2(N-1)
  =2N(N-1)(2N-1).
  \]

These are exactly SD33. For each fixed \(N\), the previously proved path and composition bounds apply near zero, giving an integrable Gaussian envelope for these derivatives. Their averaging is justified.

To check the Gaussian algebra, put
\[
t=\phi(u_0),\quad p=\phi'(u_0),\quad q=\phi''(u_0).
\]
Direct differentiation gives
\[
Dg=
\begin{pmatrix}
0&p\\
p&a_0q
\end{pmatrix},
\qquad
Dg[g]=(a_0p^2,tp+a_0^2pq).
\]
Hence
\[
\|Dg[g]\|_2^2
=a_0^2p^4+t^2p^2+2a_0^2tp^2q+a_0^4p^2q^2,
\]
and
\[
D^3\psi[g,g,g]
=3a_0^2tp^2q+a_0^4p^3\phi'''(u_0).
\]
Independence and the Gaussian moments \(Ea_0^2=1\), \(Ea_0^4=3\) yield
\[
\begin{aligned}
\mathsf S&=3E[\phi\phi'^2\phi''+\phi'^3\phi'''],\\
\mathsf H&=E[\phi'^4+\phi^2\phi'^2
+2\phi\phi'^2\phi''+3\phi'^2\phi''^2].
\end{aligned}
\]
Thus \(\mathsf S+4\mathsf H\) has exactly the five coefficients \(3,11,4,4,12\) displayed in \(J_\phi\).

Finally, applying \(8(\cdot)|_{N=k}-(\cdot)|_{N=2k}\) to SD33 gives coefficients
\[
-3k(2k-1)\quad\text{and}\quad-12k(2k-1)
\]
for \(\mathsf S\) and \(\mathsf H\). Dividing by \(6\) gives
\[
\overline Q_k'(0)
=-\frac{k(2k-1)}2(\mathsf S+4\mathsf H)
=-\frac{k(2k-1)}2J_\phi.
\]
This verifies the sign and normalization in SD36 and completes the proof of SD4.

**§11.5, lines 492–516: special cases and sharpness.** For a constant admissible activation, normalization forces \(\phi\equiv\pm1\). Then
\[
A_N=a_0+Nh\phi,\qquad U_N=u_0,
\]
so \(F_{N,1}(h)=Nh\), \(J_\phi=0\), and the discrepancy vanishes.

For \(\phi(z)=z\), the activation assumptions hold with \(M=1\), and \(J_\phi=8\). Under the orthogonal coordinates
\[
\xi_\pm=(a\pm u)/\sqrt2,
\]
one Euler step multiplies \(\xi_\pm\) by \(1\pm h\). Their initial second moments equal one, and
\[
au=(\xi_+^2-\xi_-^2)/2.
\]
This proves SD37 directly.

The discrepancy’s cubic coefficient is
\[
8\binom{2k}{3}-\binom{4k}{3}
=-4k(2k-1),
\]
as required. Its fifth coefficient expands to
\[
32\binom{2k}{5}-\binom{4k}{5}
=-\frac{64}{3}k^4+56k^3-\frac{140}{3}k^2+12k,
\]
which factors as
\[
-\frac43k(k-1)(2k-1)(8k-9).
\]
This verifies SD38, including the vanishing fifth coefficient at \(k=1\).

If a bound \(Ck^p|h|^5\), with \(p<4\), held on a positive radius proportional to \(1/k\), then for each fixed \(k\), division by \(|h|^5\) and passage to \(h=0\) would bound the absolute fifth coefficient by \(Ck^p\). Its leading magnitude is \((64/3)k^4\), a contradiction as \(k\to\infty\).

This establishes precisely the claimed sharpness: the exponent cannot be lowered for the whole activation class, even permitting an activation-dependent constant. It does not claim sharpness of the numerical value of \(B_\phi^{\rm sh}\).

**§11.6, lines 518–551: dyadic terminal-output consequence.** With
\[
G_N(s)=F_{N,1}(s/N),\qquad h=s/(2k),
\]
the condition \(|s|\le S\le2c_\phi\) guarantees the hypothesis of SD4. The cubic contribution has magnitude
\[
|J_\phi|\frac{2k-1}{16k^2}|s|^3
\le\frac{|J_\phi|S^3}{8k},
\]
and the remainder is
\[
B_\phi^{\rm sh}k^4\left|\frac{s}{2k}\right|^5
\le\frac{B_\phi^{\rm sh}S^5}{32k}.
\]
Thus SD39 has the correct constants.

For nonnegative integers \(q>p\), telescoping along dyadic indices gives
\[
\sup_{|s|\le S}|G_{2^q}(s)-G_{2^p}(s)|
\le
\left(\frac{|J_\phi|S^3}{8}
+\frac{B_\phi^{\rm sh}S^5}{32}\right)
\sum_{j=p}^{q-1}2^{-j}.
\]
Completeness of \(\mathbb R\) gives a pointwise limit; the same bound proves uniform convergence. Since the infinite tail equals \(2^{1-p}\), the resulting error is exactly SD40:
\[
\sup_{|s|\le S}|G_\infty(s)-G_{2^p}(s)|
\le2^{-p}
\left(\frac{|J_\phi|S^3}{4}
+\frac{B_\phi^{\rm sh}S^5}{16}\right).
\]

Continuity is justified. On this interval the finite-recursion observable has the common bound
\[
|A_N\phi(U_N)|
\le M(1+MS/N)^{2N}R(z_0)^2
\le Me^{2MS}R(z_0)^2.
\]
Thus Gaussian integration preserves the continuity of each fixed \(G_N\), and uniform convergence preserves continuity of \(G_\infty\).

The conclusion is correctly restricted to the dyadic sequence of terminal expected outputs. No identification with a continuous-flow solution is needed for the stated result.

**Required corrections: none.**

The precise limitations of this clean verdict are:

- SD4 is uniform in the update count only under \(|h|k\le c_\phi\); it is not a fixed-step, unlimited-horizon estimate.
- Width identification is exact equality of expectations. The candidate does not prove sample-path, probabilistic, or hidden-state convergence for growing programs.
- SD40 proves a continuous dyadic limit on the stated short feature-time interval. It does not establish convergence along all discretizations, partition independence, a restart state, or an ODE identification.
- Physical loss GD, small-readout initialization, and reused inter-hidden-layer matrices are outside the proved model.
- The constant is finite and explicit, but no numerical evaluation or optimality claim for its value was checked or needed.
- This is an analytic proof audit, not a machine-checked formal verification. All mathematical conclusions above were checked from the supplied arguments using finite-dimensional calculus, finite algebraic sums, and Gaussian integration.