# Independent internal check of the smooth local estimates

2026-10-01. **Verdict: the local claims in Sections 2–5 of
`SMOOTH_CAVITY_ROUTE.md` pass this check under their stated assumptions.**
This covers conditional all-time scalar freezing, concentration of the
specified finite response trace, the ordinary-Euclidean smooth reinsertion
remainder, and its derivative with respect to a bounded supplied forcing.
It does not certify a finite-width-to-population mean estimate, a complete
two-sided population law, or the all-initialization target in `SMOOTH_SETUP.md`.
No substantive mathematical correction to these local claims was found.

## Scope and exact versions

The supervisor assigned an independent internal proof check of these local
statements, with the scientific inputs restricted to the seven complete
files below. Every line of each listed file was read, including all 653
lines of the candidate. Sections 6–7 were read to check the boundary of the
claimed result, not to certify the unproved law proposed there. No prior
review, sibling smooth route, other study, manuscript, archive, experiment,
or Git history was read. Only this report was written.

| Complete input | Lines | SHA-256 |
|---|---:|---|
| `SMOOTH_SETUP.md` | 93 | `a9a2166984c946a5cceebd6f01c168b052e1b74da2b52a2df92c111aa830eee6` |
| `SMOOTH_CAVITY_ROUTE.md` | 653 | `a9060c96186d90f83e82376d904173389835b3a97b0ae3b586192a657e49b687` |
| `FITTING_AND_THRESHOLD.md` | 173 | `edb64134a5a4b5ce620586d0da0d3276ca542b1069b0a48801fa3f5d4cd4d1c2` |
| `CONCENTRATION_ROUTE.md` | 326 | `4331e895f388b238ced358cfa101390b80681c3797fa36b5b8ba7e319312d8f5` |
| `BIAS_CAVITY_ROUTE.md` | 514 | `55291e0646cc53a7a9d484e066bff2830a0ddd947b3f1240f96347440d4f16e8` |
| `WEIGHTED_REMAINDER_ROUTE.md` | 682 | `3afc3f16ed49ceeb441c943592febcd7cf6b5379d78ce21d2fcf6bbc72b52a33` |
| `CLIPPED_POPULATION_ROUTE.md` | 237 | `63bdd715efc7d05875acd4b591d8d2751f38a4f15246f78b7ebfab44c36b5082` |

The candidate prefix before `## 6. `, comprising lines 1–535 and therefore
the frozen local candidate, has SHA-256
`04c21d4eae698d01bf8ba8ec18b8395238e365eb595478000714003e2976045e`.
This identifies the checked local version if later sections are expanded.
The hashes were checked again after reading.

`AGENTS.md`, the solve-math-rigorously and explain-with-canonical-notation
skills, the latter's neural-response reference, and the investigate-conjectures
skill with its adversarial-audit reference were applied. The candidate's
listed `RESOLUTION_UPPER_ROUTE.md` was outside the assigned input set and
was not read. Its hard-clip near-cap estimate is not needed for the present
smooth proof: the needed adaptive linear lemma is given completely in
Section 7 of `WEIGHTED_REMAINDER_ROUTE.md`, and smooth bounded second
derivatives replace that note's near-cap argument. No additional scientific
input is needed for this local verdict.

## 1. Model, fitting, and the derivative distinction

Use the candidate's notation: \(\psi=\operatorname{sech}^2\),
\(u_a=x_a/\sqrt d\), \(\alpha_a=Au_a\), and
\(F(\alpha,p)=M\tanh(p\psi(\alpha)/M)\). The scalar residual RMS is
\(\rho=\|r\|_2/\sqrt m\). Width is \(n\); the data dimensions and the
number of samples are fixed.

The fitting transfer is valid. Before the final hard-clip threshold claim,
`FITTING_AND_THRESHOLD.md` uses the contraction
\(|c_M(q)|\le |q|\), bounded activations, and the readout Gram gap. Those
properties hold for this smooth map. In particular the hidden-motion term
in \(\dot r=-2\Gamma_w r+e\) is bounded directly; no positive Gram
identity for the complete clipped update is needed. The hard-clip
inactivity conclusion is correctly excluded from the transfer.

The actual prediction derivative uses
\(p_b=w\odot\psi(z_b)\), whereas the value update and transpose action
use \(d_a=c_M(w\odot\psi(z_a))\). Differentiating
\(B=W_0+(mn)^{-1}\sum_a v_a k_a^\top\) confirms every term in candidate
equation (5), including the asymmetric pairing \(p_b^\top d_a/n\) and
the key-motion term with prefactor \(\rho/(m\tau)\). No step identifies
these two vectors.

The scalar derivative formula (2) is valid: each positive derivative is a
sum of bounded polynomial factors in \(\tanh\alpha\) times
\(\psi(\alpha)^b x^j\tanh^{(b+j)}x\), where
\(x=p\psi(\alpha)/M\) and \(b+j>0\). Exponential decay of positive
derivatives of tanh controls all powers of \(x\). Thus the required
global first, second, and third scalar derivative bounds hold for fixed
\(M>0\), including unbounded carriers.

The full autonomous vector field still contains the nonsmooth norm
\(\rho\). The first-difference argument only uses
\(|\rho^1-\rho^2|\le\|r^1-r^2\|_2/\sqrt m\); it does not
differentiate this norm or divide by it. The smooth variations later in
the candidate are variations of a different, explicitly forced system in
which the scalar histories are held fixed. This distinction is respected.

## 2. Conditional scalar freezing

Candidate equation (9) is valid on the initialization law conditioned on
\(\mathcal G_n\), for all sufficiently large widths with
\(\Pr(\mathcal G_n)\ge1/2\). All constants may depend on the fixed
data, cap, and margins. It is an all-time normalized-state comparison.

The needed probability argument does not assume that conditioning preserves
Gaussian independence. If \(X\) is any one of the actual scalar
contractions on \(\mathcal G_n\), and \(X^{\mathrm{ext}}\) is its
bounded Lipschitz extension, then

\[
\mathbb E[|X-\mathbb E[X\mid\mathcal G_n]|^2\mid\mathcal G_n]
\le
\frac{\operatorname{Var}(X^{\mathrm{ext}})}{\Pr(\mathcal G_n)}.
\]

Indeed the conditional mean minimizes conditional squared error, so one
may first center at \(\mathbb E X^{\mathrm{ext}}\). The root-space
Lipschitz constants are \(C/\sqrt n\) for \(K,V\) and
\(Ca(t)/\sqrt n\) for \(r,\rho\), with the integrable envelope
\(a(t)=(1+t)e^{-ct}\). Gaussian Poincare then gives exactly (10).
The concentration dependency contains the needed Poincare proof.

The clock and means are consistent:

\[
\bar\tau(t)=1+\int_0^t\bar\rho(s)\,ds,
\qquad |\bar r_a(t)|\le\sqrt m\bar\rho(t).
\]

These follow from Fubini and the pathwise residual bound. One does not need,
and generally does not have, \(\bar\rho=\|\bar r\|_2/\sqrt m\).
Also, because both clocks are at least one,

\[
\left|\frac\rho\tau-\frac{\bar\rho}{\bar\tau}\right|
\le |\rho-\bar\rho|+\bar\rho|\tau-\bar\tau|.
\]

This supplies the key-equation coefficient estimate in (11). The displayed
sequential replacement of residuals before contractions gives the integrable
factor \(\bar\rho\) on the remaining contraction differences. All forced
coordinate bounds follow by direct integration; the forcing need not satisfy
its own empirical contraction identities. Minkowski and Gronwall therefore
prove (9) without requiring a temporal supremum concentration theorem for
\(K,V\).

The passive-query extension is also justified: reconstruction from the
forced states' actual pairings is Lipschitz in their normalized-state
distance. For \(x\) in a fixed bounded set, the first-layer map has a
uniform input norm bound. Thus this particular comparison can be uniform
over that bounded set without a spatial entropy estimate. This does not
upgrade the separate centered-prediction theorem for arbitrary query laws.

## 3. Normalized response-trace concentration

Equations (12)–(18) are valid for the stated supplied deterministic histories
and operator cutoff. They concern the finite functional

\[
R^h_{n,ab}(t,s)=n^{-1}\operatorname{tr}
\bigl[D H_a(U(t))\Phi(t,s)J_b(s)\bigr],
\qquad H_a(U)=\tanh(Au_a).
\]

The source \(r_b(s)\) is excluded from this kernel and included exactly
once when it is integrated in (19) or (25). The sign and factor \(-2/m\)
in \(J_b\) follow from the actual first-weight equation.

The Hilbert–Schmidt estimate does not assert a normalized-L2 Hessian bound.
A diagonal derivative difference has ordinary Frobenius norm at most the
ordinary Euclidean input difference, times a scalar second-derivative
constant. Dividing both by \(\sqrt n\) is legitimate. All other factors
are bounded operators, and
\(\|\Delta W\|_F/\sqrt n\le\|\Delta W\|_{\rm op}\).
Telescoping the fixed finite graph therefore proves (15). Duhamel and the
trace pairing prove (16) with no additional dimension factor.

For the terminal-time derivative, every row of \(\dot A\) is bounded by
\(C\rho(t)\), because the smooth lower signal is bounded by \(M\).
This controls \(\partial_t D H_a\) in operator norm. Its difference is
controlled in normalized Hilbert–Schmidt norm using bounded derivatives of
\(\psi\), the same row-speed bound, and the normalized difference of
the speeds. Thus (17) has the integrable envelope \(C\rho(t)\).
Extending the value at \(t=s\) and the terminal velocity separately, then
integrating the latter, proves the temporal supremum in (18).

For precision, passing this supremum estimate to the actual conditional
mean is valid even though a pointwise minimization alone is not enough.
Let \(E\) denote the operator-cutoff event, let \(X^{\mathrm{ext}}(t)\)
be the extended process, and let \(c(t)=\mathbb E X^{\mathrm{ext}}(t)\).
Conditional Jensen and the triangle inequality give

\[
\mathbb E\!\left[\sup_t
 |X(t)-\mathbb E[X(t)\mid E]|^2\mid E\right]
\le \frac4{\Pr(E)}
 \mathbb E\sup_t|X^{\mathrm{ext}}(t)-c(t)|^2.
\]

The cutoff probability is bounded below for the fixed sufficiently large
cutoff. This supplies the candidate's claimed conditional-mean version.
The estimate is uniform in the fixed source time \(s\), so Minkowski
allows integration against a deterministic integrable source envelope.
No supremum over all source times, nor a comparison with a population
response mean, has been proved here.

## 4. Ordinary-norm row remainder and tagged derivative

Equations (20)–(24) hold conditionally on each cavity with bounded operator
norm. These are ordinary Euclidean/Frobenius norms, without division by
\(\sqrt n\). The removed row \(\omega\sim N(0,I_n/n)\) is Gaussian
under this cavity conditioning. The supplied histories are deterministic;
the paths \(\eta,\chi\) may depend measurably on the row, with fixed
deterministic sup bounds.

The proof does not condition on the realized \(\eta\) or \(\chi\).
For every tangent coordinate it takes absolute values inside the source
integral before bounding the adaptive path. The remaining kernels are cavity
measurable. The Gaussian projection estimate and integrable propagator
variation then give coordinate envelopes \(C_p/\sqrt n\), including
state-coordinate terminal suprema. For algebraic inputs the candidate
correctly applies this estimate to each complete kernel row, rather than
pushing coordinate envelopes through an operator norm.

Consequently, if \(q_j\) is a scalar Taylor defect at a pure tangent input,
then \(\|q_j\|_{L^p}\le C_p/n\). There are at most \(Cn\) coordinates,
so, for \(p\ge2\),

\[
\bigl\|\|q\|_2\bigr\|_{L^p}
\le\left(\sum_j\|q_j\|_{L^p}^2\right)^{1/2}
\le C_p/\sqrt n.
\]

Lower moments follow by monotonicity. The finite graph and its integrable
Lipschitz coefficient \(C\rho(t)\) propagate these ordinary-norm defects,
proving (20). At each algebraic node the same comparison gives the required
fixed-time ordinary-norm remainder bound. This is the needed delocalized
Gaussian argument; scalar smoothness by itself would not give the result.

The derivative estimate (21) is a fresh variation calculation, not a
derivative taken of inequality (20). At a nonlinear node let the actual
eta-input increment be \(t_\eta+e_\eta\), where \(t_\eta\) is its
cavity tangent. After propagating the derivative error linearly, the new
source is bounded by
\(C(|t_\eta|+|e_\eta|)|t_\chi|\). Its pure-tangent product has
ordinary \(L^p\) norm \(C_p/\sqrt n\). For the other product,

\[
\bigl\|\|e_\eta\odot t_\chi\|_2\bigr\|_{L^p}
\le
\bigl\|\|e_\eta\|_2\bigr\|_{L^{2p}}
\bigl\|\|t_\chi\|_2\bigr\|_{L^{2p}}
\le C_p/\sqrt n.
\]

The first factor is the proved ordinary remainder; the second is bounded
by the coordinate tangent moment estimates. This validates (23), closes
the augmented graph comparison, and proves (21) by Gronwall. Constants can
be chosen linear in the sup bound on \(\chi\).

For the feature output in (24), only \(A\) enters \(H_a\), so the state
coordinate supremum envelopes and the state remainder supremum suffice.
Hölder with \(\|\omega\|_2\), using the already proved higher fixed
moments, gives the stated scalar \(L^p\) bounds.

The adaptive trace replacement (25) is valid at least in the RMS norm
proved completely by the supplied adaptive linear lemma. If higher fixed
moments are intended, they follow as well: symmetrize the cavity matrix,
diagonalize it, and expand an even moment of
\(n^{-1}\sum_j\lambda_j(G_j^2-1)\). Independence forces each surviving
index to appear at least twice, giving
\(\|\omega^\top Q\omega-\operatorname{tr}Q/n\|_{L^p}
\le C_p\|Q\|_F/n\le C_p\|Q\|_{\rm op}/\sqrt n\).
Applying this to the initial terminal value and integrable terminal
derivative, then taking absolute values before \(\eta\) or \(\chi\),
proves the same rate for every fixed finite moment. This argument does not
require adaptive sources to be Gaussian.

The lower-column state extension has the same bounded graph structure.
An additive perturbation \(e\) of \(z_b\) directly changes the readout
velocity by \(-(2/m)r_b\psi(z_b)\odot e\), the value velocity by
\(-2r_bF_z(z_b,w)\odot e\), and the first-weight velocity through
\(W_0^\top(F_z(z_b,w)\odot e)\). After factoring \(r_b\), all
source operators are bounded. Direct algebraic derivatives of the output
\(d_a\) remain separate; they are not supplied by the state propagator.

## 5. Exact boundary of this verdict

The forcing derivative holds with the realized forcing path fixed. It is
not a derivative of a self-consistent forcing map, nor does it identify an
average full-graph diagonal response with a single-neuron population
response. That is explicitly left open in candidate Section 7.

The candidate correctly retains the instantaneous derivative
\(F_z(z,w)=-2w\psi(z)\tanh z\,
\operatorname{sech}^2(w\psi(z)/M)\). Its displayed atom in the upper
response is consistent with this direct derivative. This check does not
establish the complete response-measure equations, their law contraction,
or a mesh-independent Gaussian covariance comparison.

The conditional finite-width means used in scalar freezing remain width
dependent. The checked results therefore neither define nor identify the
own smooth population predictor. They also give no all-time control of
the original flow outside the initialized good event. A failure probability
of \(C/n\) alone cannot upgrade the checked conditional bounds to the
unconditional all-time second moment in the setup.

There are only minor presentation repairs: several displays contain
`qquad` without its leading backslash, and Section 5 can explicitly recall
\(s(t)=\int_0^t\rho(u)\,du\) when mentioning the stronger activity
envelope. Neither affects the proof. This internal local pass is not an
independent promotion review or a certification of the requested full
population theorem.
