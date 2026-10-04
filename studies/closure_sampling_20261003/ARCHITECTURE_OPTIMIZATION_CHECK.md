# Internal check of the separated runtime depth constants

2026-10-04. **PASS, conditional on the stated source interface.** This is
an independent scoped reconstruction of `DEPTH_CONSTANT_SEPARATION.md`,
not a promotion review or a new proof of the inherited stochastic source
theorem. I found no numerical or logical defect in replacing the mixer
tube by 9, in the exponent table, or in the resulting runtime label and
all-time error bounds. No experiment, Git operation, original-route edit,
other-study read, or maintained-book edit was performed.

The assigned new label-rescaling and dimension-optimization routes had
not been frozen for exchange and were not read for this check. Their
validity is not implied by this report.

## Inputs and scope

The following inputs were read completely. The canonical-notation skill,
its neural-response reference, and the rigorous-math skill were applied.

| Input | SHA-256 |
| --- | --- |
| `DEPTH_CONSTANT_SEPARATION.md` | `6e23f2eb95b1979e7be722f76bafb43ee239f83cc5175d58d17a0f9e73fcb17f` |
| `EXPLICIT_RUNTIME_CONSTANTS_ROUTE.md` | `775ed6756af7de018c961173b850ad69930a71e4273c669bfe71c93182987bcd` |
| `EXPLICIT_SOURCE_CONSTANTS_ROUTE.md` | `d4a1bf4bd247d1b93909d4ee001da74c4c6f4573021370800f9c152dae05ab6a` |
| `STORAGE_QUADRATIC_IMPROVEMENT.md` | `ec18f54a3e3977bf9c99ce5c26066f48688848f8b5a9c142b75424badeb025e2` |
| `ERROR_PREFACTOR_GEOMETRIC_ROUTE.md` | `2cf92bcfb35729374b607c348b69ab80ae8e741878155012980ed3ffa580879c` |
| `EXPLICIT_ARCHITECTURE_CONSTANTS.md` | `19a307c4c8d9325605b0a88099dce8668baf1f61e3bf7088bc5ba36deee3c64d` |

Let hidden depth be \(L\ge2\), label RMS be \(Y>0\), capped normalized
feature gap be \(0<\lambda\le1\), and \(s=Y/\lambda\). Let

\[
B=\max(1,B_\phi),\qquad
\beta=\max(10,B,4B/a,32B/a^2,16/a),
\]

where the activations are bounded by \(B_\phi\) on the common strip

\[
|\operatorname{Im}z|<a.
\]

The real activation norm

\[
B_{\rm rt}=\max(1,B_\phi,2B_\phi/a,8B_\phi/a^2)
\]

is at most \(\beta\). The exact inherited source interface includes the
initial Gram gap at least \(\lambda/2\), coordinate tolerance

\[
\epsilon=n^{-1}\le Y,
\]

exact source-space isometries and paired initialized actions, initialized
dense mixer cap 8, and a coefficient \(1\le K\le\beta^{5L}\) such that

\[
M\le1+4Ks\sqrt{\log(en)}.
\tag{1}
\]

The source theorem must supply these properties through

\[
T=32\lambda^{-1}\log(en)
\]

under its own label conditions. Equation (1) is a direct bound; it is
not normalized by the actual residual activity. This check retains the
normalization correction in Section 7.3 of the explicit source route.

## The tube change does not alter the source interface

For the initialized compressed mixer, equation (5) of the storage
construction is a dense initialized operator compressed between two
source-space isometries and their adjoints. Therefore

\[
\|B_C^{(\ell)}(0)\|\le\|W_n^{(\ell)}(0)\|\le8.
\]

Set \(g=h=2B_{\rm rt}\) and use mixer tube \(R=9\). The raw energy and
readout projection argument in the explicit runtime route gives

\[
\|\theta_{h,C}(t)-\theta_{h,C}(0)\|
 \le56Us^2\sqrt\lambda,
\qquad
\sup_{\ell,v}\|h_C^{(\ell)}(t,v)-h_C^{(\ell)}(0,v)\|
 \le56FUs^2\sqrt\lambda.
\tag{2}
\]

Here \(U,F\) are the route's finite recurrences with \(R=9\). Under

\[
224FUs^2\le1,
\]

the second displacement is at most \(\sqrt\lambda/4\), and the first
is at most \(1/4\), since \(F\ge1\) and \(\lambda\le1\). Hilbert--Schmidt
displacement bounds operator displacement, so every compressed mixer
remains below \(8+1/4<9\). The training least singular value remains
above

\[
\sqrt{\lambda/2}-\sqrt\lambda/4>\sqrt{\lambda/8}.
\]

The dense model obeys the same sufficient estimates with smaller metric
constants. This closes both real tubes independently of the comparison
error. The selected reference mixer does not need an operator cap 9:
the forward and reverse subtraction propagates errors with the actual
compressed mixer, and treats the selected reference action by its
separate source defect. Thus no unstated bound on that proof-only mixer
is introduced.

The appearances of \(K\) in source pairing, action, carrier and readout
transfer estimates remain unchanged. In particular the initialized
paired-action defect \(2K(K+1)\epsilon\) remains a valid conservative
bound. The smaller tube does not require decreasing that coefficient.

## Reconstruction of the exponent table

Write \(b_\ell=g^{L-\ell+1}9^{L-\ell}\) and

\[
b=\max_\ell b_\ell.
\]

This is the runtime route's backward constant, distinct from the
activation-only base \(\beta\). Since

\[
9g\le18\beta\le\beta^3,
\]

we have \(b\le\beta^{3L}\). The recurrence

\[
F_1=g,\qquad F_\ell=g(h+9F_{\ell-1})
\]

in fact gives \(F\le2b\): with \(A=9g\ge18\), its geometric sum is

\[
F_\ell=gA^{\ell-1}
 +gh\frac{A^{\ell-1}-1}{A-1}
 \le gA^{\ell-1}\left(1+\frac h{A-1}\right)
 <2b.
\]

Also \(U\le h\sqrt L\,b\). Consequently the displayed weaker bounds

\[
U\le\beta^{5L},\qquad F\le\beta^{6L}
\]

hold for all \(\beta\ge10,L\ge2\). Substitution into the exact runtime
definitions gives the following independently reconstructed estimates.
The middle column records a sufficient intermediate expression before
absorbing numerical coefficients and powers of \(L\).

| Quantity | Intermediate upper bound | Final upper bound |
| --- | --- | --- |
| \(D_\delta\) | \(6\beta^{5L}\) | \(\beta^{6L}\) |
| \(W\) | \(64\beta^{5L}\) | \(\beta^{7L}\) |
| \(J_0\) | \(20\sqrt L\,\beta^{5L+1}\) | \(\beta^{8L}\) |
| \(V_0\) | \(14\beta^{11L}\) | \(\beta^{12L}\) |
| \(P_h,P_\delta\) | \(17\beta^{10L},29\beta^{10L}\) | \(\beta^{11L},\beta^{11L}\) |
| \(D_r\) | \(8\beta^{11L}\) | \(\beta^{12L}\) |
| \(A_0\) | \(29\beta^{17L}\) | \(\beta^{18L}\) |
| \(C_f\) | \(2\beta^{24L}\) | \(\beta^{25L}\) |
| \(H_0\) | \(7\beta^{32L}\) | \(\beta^{33L}\) |
| \(Z_0\) | \(3L\beta^{28L}\) | \(\beta^{30L}\) |
| \(J_1\) | \(5\sqrt L\,\beta^{36L+1}\) | \(\beta^{39L}\) |
| \(D_0\) | \(14L\beta^{17L}\) | \(\beta^{19L}\) |
| \(F_0\) | \(38\beta^{47L}\) | \(\beta^{48L}\) |
| \(T'_0\) | \(6\beta^{12L}\) | \(\beta^{13L}\) |
| \(G\) | \(12\beta^{48L}\) | \(\beta^{49L}\) |
| \(C_1\) | \(\beta^{56L}\) | \(\beta^{57L}\) |
| \(C_2\) | \(16\beta^{54L}\) | \(\beta^{55L}\) |
| \(O_0\) | \(6\beta^{33L+1}\) | \(\beta^{35L}\) |
| \(W_1\) | \(84\beta^{16L}\) | \(\beta^{17L}\) |
| \(T_1\) | \(9\beta^{17L+1}\) | \(\beta^{19L}\) |

The absorptions use \(L\le\beta^{L-1}\), \(\beta^L\ge100\), and

\[
3L\le\beta^{2L},\qquad14L\le\beta^{2L},\qquad
5\sqrt L\le\beta^{3L-1}.
\]

For example, the three terms in \(J_1/\sqrt L\) are bounded by

\[
2\beta^{36L+1},\qquad2\beta^{30L+1},\qquad\beta^{31L},
\]

and the two terms inside the layer sum defining \(D_0\) are at most

\[
4\beta^{11L+2},\qquad9\beta^{17L}.
\]

These verify the rows with the largest combined depth exponents. The
constant 84 in the \(W_1\) row is the sum \(4+50+24+6\), using its
definition \(2h+50V_0+6(h^2+J_0^2)\). No coefficient has been moved into
a width threshold in this accounting.

## Geometric comparison and endpoint

The numerical comparison survives the substitution. In the notation of
the runtime route, \(a\) is hidden parameter error, \(e\) is normalized
residual error, \(p=T_Ce\), and

\[
\zeta=w_C-w_R+p,\qquad E=a+\|p\|+\|\zeta\|,
\qquad r=\epsilon/\sqrt\lambda.
\]

The lifted residual estimate has damping coefficient

\[
-2+18J_0^2s^2\le-1
\]

when \(6J_0s\le1\). The exact cancellation for \(\dot\zeta\) then
gives, with the same constants as the original derivation,

\[
E(t)\le G\int_0^t
 (M\rho_n+\rho_C+\nu/\sqrt\lambda)(E+r)\,du.
\]

All errors vanish initially. From the integrated residual and selected
readout-velocity bounds,

\[
\int_0^T(M\rho_n+\rho_C+\nu/\sqrt\lambda)
 \le(8+W/2)s+16Ks^2\sqrt{\log(en)}.
\]

Thus the raw exponent is precisely

\[
C_1s+C_2s^2\sqrt{\log(en)},
\qquad C_1=G(8+W/2),\quad C_2=16KG.
\]

The readout decomposition retains the small source term \(sr\), which
is necessary to retain the final factor of \(Y\). It gives

\[
|f_C-f_n|\le O_0\{E+sr\}
 \le O_0r\{s+e^{C_1s+C_2s^2\sqrt{\log(en)}}-1\}.
\]

The factor \(Y\) therefore comes from an explicit vanishing-at-zero
estimate, not from suppressing a label-independent error term. For any

\[
s\le c\le\min\{1,(224FU)^{-1/2},(6J_0)^{-1}\},
\]

the elementary square completion in the runtime route gives

\[
C_{\rm err}
 =O_0\left[1+\sqrt e(C_1+C_2c)e^{C_1c+C_2^2c^4}\right]+8T_1.
\tag{3}
\]

The global prediction-speed bounds give each integrated tail at most

\[
4T_1Y\lambda^{-3/2}e^{-\lambda t/4}.
\]

The source horizon is larger than the \(4\lambda^{-1}\log(en)\)
needed in this step, so both fitted endpoints are included with the
same coefficient (3).

Set \(Q_{\rm rt}=\beta^{60L}\). The table bounds

\[
C_1,C_2,O_0,T_1,6J_0,\sqrt{224FU}\le Q_{\rm rt}.
\]

For \(s\le c\le Q_{\rm rt}^{-1}\), the exponential in (3) is at
most \(e^2\). Hence

\[
C_{\rm err}
 \le9Q_{\rm rt}+2e^2Q_{\rm rt}(Q_{\rm rt}+1)
 <40Q_{\rm rt}^2\le\beta^{122L}.
\]

This proves the checked conditional conclusion

\[
Y\le\lambda\beta^{-60L}\quad\Longrightarrow\quad
\sup_{t\in[0,\infty],\ \|x\|=\sqrt d}|f_C(t,x)-f_n(t,x)|
 \le\beta^{122L}\frac{Y}{\lambda^{3/2}\sqrt n},
\tag{4}
\]

provided the inherited source theorem's label conditions also hold.
Those conditions cannot be replaced by the displayed runtime cap on
the strength of this check alone.

Finally, with \(\lambda=\min(1,\gamma/m)\), covariance trace gives

\[
\lambda^{-3/2}\le B^3(m/\gamma)^{3/2}.
\]

Since \(B\le\beta\) and \(3\le2L\), equation (4) implies the
claimed coefficient \(\beta^{124L}\) in the formulation using

\[
Y(m/\gamma)^{3/2}/\sqrt n.
\]

The stochastic source event and its fixed-data, sufficiently-large-width
qualification remain inherited inputs. Zero labels retain their separate
stationary interpretation. This report certifies an explicit sufficient
linear depth exponent for the deterministic runtime, not optimality,
growing-depth uniformity, or an explicit width threshold.

## Post-freeze independent label and assembly check

2026-10-04. The preceding runtime check was frozen at SHA-256
bfa9a6107ea50025d41f0820da0ed78376b0252976b27c41fc6424517610f0fe
before the supervisor authorized reading the new label candidate. The
following additional inputs were then read completely:

| Input | SHA-256 |
| --- | --- |
| LABEL_DEPTH_RESCALING_ROUTE.md | d06ceea6598bf3f86e0843682c5600365ef01b4b80eaad6544ceec1a9d4ec1f1 |
| EXPLICIT_LABEL_CONSTANTS_ROUTE.md | 0fa619fde5966b55287eaaef6d3c59cc11e3d858964d989741556e173aadcb94 |
| DEPTH_INDEPENDENT_EXPONENT.md | 73c12dafdd05dcae7f287b2ccc49cc237a540ef7b2f26d53204c96bcd9feceda |
| LABEL_SEPARATE_BUDGETS.md | 6800fb4d51cf1adc43cd56d987ef0e13e51b0c8d00c6106452416a624886b594 |

**PASS, conditional on the inherited local insertion and continuation
interfaces.** The rescaling gives the stated sufficient source cap
\(Y/\lambda\le\beta^{-32L}\), retains the previous source coefficients,
and therefore combines with the checked runtime under
\(Y/\lambda\le\beta^{-60L}\). The dimension-optimization route had not
been read at this second freeze.

In this addendum only, \(s=\max(1,4B/a)\) and
\(t=\max(1,32B/a^2)\) are the label route's derivative bounds. The label
ratio is written explicitly as \(Y/\lambda\). The activity allowance is
\(S=16Y/\lambda\). All finite constants have exactly the definitions in
the frozen label route; \(\mathcal B\) denotes its empirical exponential
budget and \(\eta\) its exponent coefficient.

### Feedback powers and the activity modulus

The stopped budget gives

\[
\|k_a^{(\ell)}\|_{p,n}
 \le(S/\eta)(p/e)(2\mathcal B)^{1/p}.
\]

The exact carrier-diagonal Hessian decomposition therefore gives

\[
\|D^2F_a\|_{p,n}
 \le A_H+(SD_H/\eta)p(2\mathcal B)^{1/p},
\qquad \|D^2F_a\|_{2,n}\le H_2.
\]

The second estimate comes from physical RMS bounds and does not acquire
\(\eta^{-1}\). These estimates apply to response endpoint blocks and
normalized residual mixtures. For \(h\ge1\) insertions, assigning
Schatten exponent \(h+2\) to all \(h+2\) factors gives exactly the
normalization \(1/n\) and the trace bound

\[
\frac{2S^h}{h!}
\left[A_H+\frac{SD_H}{\eta}(h+2)
                    (2\mathcal B)^{1/(h+2)}\right]^{h+2}.
\]

Splitting the power gives first sum \(4A_H^2(e^{2A_HS}-1)\) and
second sum

\[
\frac{8e^2D_H^2S^2\mathcal B}{\eta^2}
\sum_{h\ge1}
\left(\frac{2eD_HS^2}{\eta}\right)^h(h+2)^2.
\]

For \(0\le q\le1/2\), the series divided by \(q\) has nonnegative
coefficients and equals 36 at \(q=1/2\). Hence the second sum is at most

\[
576e^3D_H^3\mathcal B S^4/\eta^3.
\]

The zero-insertion term is \(2H_2^2\). Exterior activity and activation
bounds, together with the direct external and learned-column terms, give
the singleton shift

\[
S[D_0+D_1\mathcal B S^4/\eta^3]+o(1),
\qquad D_1=576e^3BD_H^3.
\]

Its cost in the carrier exponential is exactly

\[
\eta D_0+D_1\mathcal B S^4/\eta^2.
\tag{5}
\]

Thus neither the RMS contribution nor the fourth activity power carries
an omitted inverse power of \(\eta\).

The stopped tail bound is

\[
\|k\mathbf1_{\{|k|>SR\}}\|_{2,n}
\le(4S/\eta)\sqrt{2\mathcal B}\,e^{-\eta R/4}.
\]

For activity increment \(0<v\le1\), taking

\[
R=\frac4\eta\log\frac{8\sqrt{2\mathcal B}}{\eta v},
\qquad\Lambda=\log(e+\mathcal B)+\log(1/\eta)
\]

makes the high-carrier changed-gate cost at most \(sSv\). Also
\(R\le\eta^{-1}[10\Lambda+4\log(1/v)]\). Under the candidate's
restriction \(S^2\Lambda/\eta\le1\),

\[
S^2Rv\le10v+4v\log(1/v)
 \le(10+8/e)\sqrt v<14\sqrt v.
\]

This proves its recurrence for \(G\) without any additional
\(\eta^{-1}\) factor. The corresponding conditional Gaussian moment is

\[
\mathcal M(q)=e^{32qG}
 [1+32qG\sqrt\pi\,e^{256q^2G^2}].
\]

For \(\eta=\min(1,B^{-1},D_0^{-1},(128G)^{-1})\) and
\(\mathcal B=64e^2L\), one has \(\mathcal M(2\eta)<6\).
The complex correction below gives \(\mathcal M_c(\eta)<4\).
The explicit feedback condition bounds (5) by two, so the layer-summed
moment ratio is strictly below

\[
\frac{(L-1)4e^2}{64e^2L}<1/16.
\]

Every collision multiplicity uses a fixed finite moment
\(\mathcal M(p\eta)\). The common-cavity proof applies for each fixed
empirical moment degree \(p\), with width tending to infinity before
the infimum over \(p\). The limiting budget-hit probability is therefore
at most \(m16^{-p}\) for every fixed \(p\). No sample maximum has entered
a Gaussian exponential moment.

### Complex queries and unchanged source coefficients

For passive-query traces, the finite endpoint norms use \(H_2\).
Schatten exponents \(2,\infty,2h,\ldots,2h\) give split series

\[
e^{2SA_H}-1,\qquad
\sqrt{2\mathcal B}\sum_{h\ge1}(4eS^2D_H/\eta)^h.
\]

Both are below one under the explicit conditions

\[
SA_H\le1/4,\qquad
16eS^2(D_H/\eta)\sqrt{2\mathcal B}\le1.
\]

At zero insertions both endpoints use Hilbert--Schmidt bounds.
Consequently \(T_Q=8f_*E_Q\) and \(T_J=8f_*E_J\) retain their previous
values, with no inverse-exponent factor in these source constants.
The carrier, response and pole-radius coefficients, including

\[
K_{\rm src}\le\beta^{4L},\qquad
c^{-1}\le\beta^{40L}(d+3)^{3/2},
\]

remain valid. The finite singleton shift divided by
\(S\sqrt{\log(en)}\) tends to zero at fixed \(S,\eta>0\), so it
changes only the eventual width for the improved carrier maximum.

Normalized Hölder and interpolation with exponents \(p\) and
\(2p/(p-2)\) give

\[
\|k_a^{(\ell)}\odot\dot z_a^{(\ell)}\|_{2,n}
\le\frac{2\rho S^2}{\eta}\max(r_\ell,U_\ell)
                    p(2\mathcal B\log(en))^{1/p}.
\]

Taking \(p=\max(4,\log(2\mathcal B\log(en)))\) and differentiating the
backward recursion proves

\[
\|\dot\delta_a^{(\ell)}\|_{2,n}
\le J_\ell^{\rm time}\rho
 [1+(S^2/\eta)\log(e+\log(en))].
\]

The short contour length is at most \(2c/\sqrt{\log(en)}\), and
\(\rho/S\le\lambda/8\). Thus the normalized complex correction has
radius \(O((\log n)^{-1/2}\log\log n)\), with fixed coefficients.
Its two-parameter Gaussian net has mean
\(O((\log n)^{-1/2}(\log\log n)^{3/2})\) and vanishing tail scale.
Every fixed exponential moment tends to one, proving the target
\(\mathbb E e^{2\eta Z_{\rm correction}}\le2\) eventually.
Here width absorbs only fixed coefficients multiplying vanishing
quantities. The persistent variational restriction
\(D_HS^2/\eta\le1/4000\) is retained explicitly.

The rescaling changes fixed coordinate and remainder coefficients but
preserves the strict width powers of the inherited insertion interface.
The stopped dependency order remains local transfer, carrier maximum,
query responses, query poles, complex moment, then budget removal.

### Label envelope and joint conclusion

Every exponent row in the candidate's Section 7 verifies by substitution.
In particular

\[
P_\ell,K_\ell\le\beta^{2L},\quad D_H\le\beta^{5L},\quad
A_H,H_2\le\beta^{8L},\quad E\le\beta^{7L},\quad
D_0\le\beta^{20L},\quad D_1\le\beta^{18L}.
\]

For the last inequality, \(576e^3<10^5\) gives
\(D_1\le\beta^{15L+6}\le\beta^{18L}\). The other recurrences give

\[
V_\ell\le\beta^{6L},\quad G\le\beta^{12L},\quad
\eta^{-1}\le\beta^{22L},\quad
\mathcal B\le\beta^{3L},\quad\Lambda\le\beta^{23L}.
\]

The reciprocal costs of the variational, query, modulus and feedback
entries in \(S_*\) are respectively bounded by

\[
\beta^{(27L+4)/2},\quad
\beta^{(28.5L+2)/2},\quad
\beta^{45L/2},\quad
\beta^{65L/4}.
\]

All are below \(\beta^{24L}\); the other entries are smaller. Thus
\(S_*\ge\beta^{-24L}\). Since \(16\le\beta^L\) and
\(8\sqrt{C_*}\le\beta^{4L}\), the evaluated source cap is even bounded
below by \(\beta^{-25L}\). The stated conservative
\(\beta^{-32L}\) therefore follows.

Intersecting source and runtime caps gives

\[
0<Y/\lambda\le\beta^{-60L}
\quad\Longrightarrow\quad
\sup_{t\in[0,\infty],\,\|x\|=\sqrt d}|f_C-f_n|
\le\beta^{122L}Y/(\lambda^{3/2}\sqrt n).
\]

A sufficient uncapped-gap formulation is

\[
0<Y\le(\gamma/m)\beta^{-62L},\qquad
\sup_{t\in[0,\infty],\,\|x\|=\sqrt d}|f_C-f_n|
\le\beta^{124L}Y(m/\gamma)^{3/2}/\sqrt n,
\]

because \(Y/\lambda\le B^2\beta^{-62L}\le\beta^{-60L}\).
The inherited stochastic insertion theorem, fixed-architecture
quantifiers, unquantified width threshold, and separate zero-label
case remain explicit limitations. No defect requiring correction was
found in the two frozen candidates audited in these first two stages.

## Post-freeze dimension and complete assembly check

2026-10-04. The runtime-plus-label report was frozen at SHA-256
feac55872a7293ca30c36a3de26119ad689e8e73a372f807e38509987a2eaa71
before reading DIMENSION_PREFACTOR_OPTIMIZATION.md. The complete
authorized dimension candidate was then read at SHA-256
8e149122bcd83a8f64bceba97a6617f644f10e59fd97456f3cfa0e10273c8f2e.
**PASS, conditional on the same inherited source interfaces.** No
substantive correction is required.

### Anisotropic complex domain

Use the candidate's time and angular constants

\[
c_t=\min\{1/8,a/(512U_*)\},\qquad
c_a=\min\{1/(8d),a/[128(d-1)V_*]\},
\]

with radii \(r_t=c_t/\sqrt{\ell_n}\),
\(r_\theta=c_a/\sqrt{\ell_n}\), where \(\ell_n=\log(en)\).
For \(d=1\), omit angular quantities and use both queries. The two
short time pieces have total length at most \(2r_t\). Thus the
preactivation displacement from a real time/angle anchor is bounded by

\[
8c_tYSU_*+(d-1)c_aV_*
\le a/64+a/128=3a/128<a/32.
\]

The sphere map and its first two angular derivatives remain bounded by
two because \((d-1)r_\theta<1/8\). This justifies the unchanged query
constants on the enlarged stopped domain. Repeating the stopped
continuation is required; a subset argument from the old equal-radius
domain would not suffice. The candidate does repeat that argument.
The total non-real/backward base-propagator cost is \(1+o(1)\), the
time-only carrier correction still has a vanishing Gaussian moment,
and fixed side lengths do not change the width powers in the insertion
nets. With the new label route, the derivative estimate has its fixed
\(\eta^{-1}\) coefficient; this still multiplies a vanishing complex
correction and introduces no new label condition.

The explicit radius estimates verify as written:

\[
c_t^{-1}\le\beta^{32L}(d+3)^{1/2},\qquad
c_a^{-1}\le\beta^{32L}(d+3)^{3/2}.
\]

The first uses \(512U_*/a\le32\beta^{30L+1}\sqrt{d+3}\);
the second uses
\(128(d-1)V_*/a\le8\beta^{30L+1}(d-1)\sqrt{d+3}\).
Consequently their product has dimension power \(3d/2-1\).

### Fourier tail and lattice count

After \(t=T(1+\cos u)/2\), set
\(\alpha=r_t/(4T)\) and \(r=r_\theta\). The mapped complex time has
imaginary part at most \(r_t/4\) and real excursion at most \(r_t\).
The coordinate Fourier coefficients therefore obey

\[
|\widehat G(k)|\le M_n e^{-\alpha|k_0|-r\|k'\|_1}.
\]

For \(P=6^d/(\alpha r^{d-1})\) and
\(H=2\log(16M_nP/\epsilon)\), splitting an omitted exponential into
two halves gives tail at most \(M_ne^{-H/2}P=\epsilon/16\)
outside \(\alpha|k_0|+r\|k'\|_1\le H\).

Evenness in time and reality leave at most

\[
N=\#\{(j_0,j')\in\mathbb Z_{\ge0}\times\mathbb Z^{d-1}:
\alpha j_0+r\|j'\|_1\le H\}
\]

real coefficient vectors. Replacing angular indices by absolute values
costs at most \(2^{d-1}\). Disjoint unit cubes based at these
nonnegative lattice points lie in the weighted simplex of radius
\(H+\alpha+(d-1)r\). Its volume yields

\[
N\le
\frac{2^{d-1}[H+\alpha+(d-1)r]^d}
 {d!\alpha r^{d-1}}.
\]

The explicit logarithmic conditions give \(H\le7\ell_n\);
\(\alpha+(d-1)r<1/4\). Substitution, with the loose radius
\(9\ell_n\), gives exactly

\[
N\le64\,18^d\,
\frac{c_t^{-1}c_a^{-(d-1)}}{d!}
\lambda^{-1}\ell_n^{3d/2+1}.
\]

This is a genuine retained-coefficient count; the factorial has not
been created by absorbing a dimension factor into the width threshold.

### Finite initial jets and paired actions

The proposed map is valid on the full unit disk. Write

\[
q=\pi T/(8r_t),\quad b_0=\tanh q,\quad
b_1=\tanh(q+\pi/4),\quad \eta_{\rm map}=b_0/b_1,
\quad\psi(\xi)=\frac{\xi-\eta_{\rm map}}{1-\eta_{\rm map}\xi}.
\]

Then

\[
z(\xi)=T/2+(4r_t/\pi)\operatorname{artanh}(b_1\psi(\xi)).
\]

Because \(|b_1\psi|<b_1<1\), the real part of the last inverse
hyperbolic tangent lies between \(\pm(q+\pi/4)\), and its imaginary
part has magnitude below \(\pi/4\). Thus

\[
-r_t<\operatorname{Re}z<T+r_t,\qquad
|\operatorname{Im}z|<r_t,\qquad z(0)=0.
\]

The inverse sends \([0,T]\) to \([0,\xi_*]\), with
\(\xi_*=2\eta_{\rm map}/(1+\eta_{\rm map}^2)<1\).
Consequently each composed Taylor coefficient is a linear combination
of only the first \(j\) initial time derivatives. Cauchy's estimate
gives coefficient bound \(M_n\), and a finite truncation reaches any
prescribed nodal accuracy.

The odd tensor DFT grid contains the entire weighted index set in its
frequency box. Distinct retained indices have distinct residues; every
alias entering a retained coefficient comes from outside that box and
hence outside the retained set. Total alias error is therefore at most
the same \(\epsilon/16\) tail. Nodal error
\(\delta=\epsilon/(32N)\) adds at most
\(|\Lambda|\delta\le2N\delta=\epsilon/16\). The complete uniform error
is at most \(3\epsilon/16\). Evenness and reality persist under both
the initial-jet construction and symmetric DFT restriction.

All time-map coefficients, Taylor operations, DFT operations, index
selection and real-coordinate conversions are scalar linear operations
applied identically to both members of a pair. They therefore commute
exactly with \(W_0\) and \(W_0^\top\), while each member independently
has its own coordinate error bound. Temporary grid values and initial
jets do not become retained arrays.

### Additions and total storage

The counts \(4N+2m+d+1\) for \(d\ge2\) and \(8N+2m+2\) for \(d=1\)
include the exact initialized additions and both points of \(S^0\).
For

\[
F_d=(d+3)^{3d/2-1}/d!,
\]

one has \(F_d\ge d+3\) for \(d\ge2\), and \(F_1=2\).
The trace constraint \(m\lambda\le B^2\) absorbs the additions without
an extra width condition. The numerical inequalities

\[
512\,18^d\le\beta^{2Ld},\qquad3\beta^2\le\beta^{2Ld}
\]

then prove

\[
R\le\beta^{36Ld}F_d\lambda^{-1}\ell_n^{3d/2+1}.
\]

The resulting right side is at least \(d\) and \(m\), as needed for
the runtime's cache inventory. Integrating \(\log x\) gives
\(d!\ge(d/e)^d\), and hence

\[
F_d^2\le e^{2d+6}(d+3)^{d-2}
\le\beta^{2Ld}(d+3)^d.
\]

Thus \(R^2\le\beta^{74Ld}(d+3)^d
\lambda^{-2}\ell_n^{3d+2}\). The explicit runtime inventory remains

\[
\operatorname{size}(C)\le1020(L+1)R^2+10m(d+1).
\]

Passing to the uncapped gap multiplies the leading coefficient by
\(B^4\). The inequality
\(1020(L+1)B^4\le\beta^{10Ld}\) holds for every
\(\beta\ge10,L\ge2,d\ge1\): use \(1020\le\beta^4\),
\(L+1\le\beta^L\), and \(L+8\le10Ld\).
The exponent \(84Ld\) already suffices, so the proposed \(86Ld\)
coefficient has room to spare.

Combining the three independently checked candidates therefore gives
the sufficient bounds

\[
Y\le(\gamma/m)\beta^{-62L},
\]
\[
\operatorname{size}(C)
\le\beta^{86Ld}(d+3)^d(m/\gamma)^2\ell_n^{3d+2}
 +10m(d+1),
\]
\[
\sup_{t\in[0,\infty],\,\|x\|=\sqrt d}|f_C-f_n|
\le\beta^{124L}Y(m/\gamma)^{3/2}/\sqrt n.
\]

These conclusions keep the source theorem's inherited stochastic
interfaces, fixed architecture/data, sufficiently-large-width meaning,
exact-real preprocessing, and separate zero-label case. They do not
assert optimal coefficients, a quantified width threshold, or
promotion to the maintained book.

## Final assembly and certified derivative bounds

2026-10-04. I read the complete final assembly
ARCHITECTURE_CONSTANT_REFINEMENT.md at SHA-256
b33f8b2ebb04eba386f59f125fd4d8f22ff3273bc094f64808db865dd27caba7.
Its preceding version was also read completely before the optional
derivative-bound addition. **PASS at this final hash**, subject to the
inherited scientific interfaces and qualifications already recorded.

The final assembly uses the sharper coefficients already justified by
the inventory above. Squaring the source coefficient costs
\(\beta^{72Ld}\); multiplying by \(1020(L+1)B^4\) costs at most
\(\beta^{10Ld}\). Thus its factorial storage coefficient

\[
\beta^{82Ld}(d+3)^{3d-2}/(d!)^2
\]

is valid. The factorial inequality adds at most \(\beta^{2Ld}\) to
obtain its coarse coefficient \(\beta^{84Ld}(d+3)^d\).
The earlier \(\beta^{86Ld}\) display in this report is simply a
looser bound. The additive term remains \(10m(d+1)\).
The source/runtime label condition \((\gamma/m)\beta^{-62L}\) and
all-time error coefficient \(\beta^{124L}\) are unchanged.
The final assembly explicitly reconciles the anisotropic time radius
with the rescaled-budget factor
\(1+(S^2/\eta)\log(e+\ell_n)\), and correctly scopes angular radii
to \(d\ge2\).

The optional use of certified derivative bounds is also valid.
If \(s,t_\phi\ge1\) bound the first and second derivatives on
\(|\operatorname{Im}z|\le a/2\), every persistent recurrence uses
only \(B,s,t_\phi\), together with \(a^{-1}\). Thus one may use

\[
\beta=\max(10,B,s,t_\phi,16/a).
\]

The runtime must then use its actual real value/derivative norm, bounded
by \(\max(B,s,t_\phi)\); its earlier Cauchy envelope was optional.
Higher derivative constants are still supplied by the outer bounded
holomorphic strip and affect the inherited remainder and width
threshold, rather than these displayed coefficients.

For \(\phi=\tanh\), take \(a=1,B_\phi=2,s=2,t_\phi=4\).
The identity

\[
|\tanh(x+iy)|^2
=\frac{\sinh^2x+\sin^2y}{\sinh^2x+\cos^2y}
\]

shows the full strip is pole free and the magnitude is below two:
for \(|y|<1\), \(\cos y>1/2\), so the ratio is below four.
On \(|y|\le1/2\), \(\cos(2y)>0\), and the ratio is at most one.
The exact identities

\[
\phi'=1-\phi^2,\qquad
\phi''=-2\phi(1-\phi^2)
\]

then give inner-strip derivative bounds two and four. Therefore
\(\beta=16\) is a valid certified choice for all final bounds.
No additional source, runtime, width-uniformity or optimality claim
is inferred from this activation specialization.
