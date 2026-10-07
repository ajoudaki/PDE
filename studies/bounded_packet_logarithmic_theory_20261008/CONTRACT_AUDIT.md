# Conditional contract audit: covariance-balanced packets

This is a scoped audit of the proposed extension of the paper's compression
contract to `BoundedGaussianPackets`. It proves the implication from the
hypothetical fluctuation and short-time estimates below; it does **not** prove
those estimates. No empirical results or other studies were used.

## Contract and model scope

The paper defines

\[
 \|f-g\|_*=
 \sup_{t\in[0,\infty]}\sup_{\|x\|_2=\sqrt d}|f(t,x)-g(t,x)|,
 \qquad
 b_n=\inf\{b\ge0:
   \Pr(\|f_n-\widetilde f_n\|_*\le b)\ge0.9999\},
\]

where the two width-\(n\) dense runs are independent. Thus \(b_n\) is a
deterministic quantile of a law, not the realized discrepancy of a sampled
pair. The requested extension would assert

\[
 \Pr\bigl(\|f^{\rm packet}_{q(n)}-f_n^{\rm ind}\|_*\le3b_n\bigr)
 \ge0.99
\]

at every sufficiently large individual width \(n\). The reference has the
ordinary Gaussian dense initialization and is independent of the packet
construction. This is a statement about exact physical gradient flow and
absolute prediction error.

This extension is distinct from the paper's existing Logarithmic decoder.
The latter uses selected packets, a metric, a finite transcript, regeneration
of width-\(n\) empirical interactions, and an ensemble median. In particular,
the Logarithmic subsection of `paper/methods.tex` explicitly warns that a
small training metric cannot replace an empirical sum for a new feature
outside its recorded source family. The current code's class docstring and
`claim_scope` explicitly say that `BoundedGaussianPackets` does not preserve
the adaptive Logarithmic posterior and has no such theorem guarantee.
Consequently an obstruction for this ordinary small-network flow would
refute the requested extension, not the paper's distinct decoder theorem
or the existence of some other compressed representation.

## Admissible fixed problem

Take two hidden layers, both with activation \(\phi=\tanh\), and

\[
 m=d=2,\qquad x_1=\sqrt2e_1,\quad x_2=\sqrt2e_2,
 \qquad y=(\lambda,0),\quad \lambda>0.
\]

Here \(\lambda\) denotes the label amplitude, not a rate constant used locally
in the appendix. The code takes normalized inputs
\(v_a=x_a/\sqrt d=e_a\): `dense_fields` multiplies its input directly and
does not itself divide by \(\sqrt d\). Supplying \(x_a\) directly to that
function would change the model.

Both inputs have the required norm, they span \(\mathbb R^2\), and
\(m\ge d\). The population covariance recursion can be evaluated structurally.
For a standard real Gaussian \(G\), put

\[
 s=\mathbb E\tanh^2(G),\qquad
 \gamma=\mathbb E\tanh^2(\sqrt s\,G).
\]

Independence and oddness give
\(Q^{(0)}=I_2\), \(Q^{(1)}=sI_2\), and
\(Q^{(2)}=\gamma I_2\). Since \(\tanh^2(u)>0\) for \(u\ne0\),
and \(\tanh^2(u)<1\) for every finite real \(u\), both
\(s\) and \(\gamma\) lie strictly between zero and one. Thus the paper's
unweighted feature gap is precisely the displayed \(\gamma>0\), and
\(m/\gamma>2\). In particular it is not \(\gamma/2\).

The activation satisfies the strip assumptions directly. Choose strip
half-width \(a=1/2\). For \(z=u+iv\) with \(|v|<a\),

\[
 |\cosh z|^2=\sinh^2u+\cos^2v\ge\cos^2(1/2)>0,
 \qquad
 |\tanh z|^2=
 \frac{\sinh^2u+\sin^2v}{\sinh^2u+\cos^2v}\le1.
\]

Hence \(\tanh\) is holomorphic there, real on the real axis, and
\(|\phi'|<2\), \(|\phi''|<4\). The appendix's activation envelope can
therefore be taken to be \(\beta=32\), since \(16/a=32\).
The label RMS is \(Y=\lambda/\sqrt2\). For example, the fixed choice

\[
 \lambda=\frac{\gamma}{2\sqrt2}\,32^{-60}>0
\]

gives \(Y=(\gamma/4)32^{-60}\), strictly within the stated sufficient
allowance \(Y\le(\gamma/m)\beta^{-30L}\). The paper explicitly states that
this sufficient cap implies its full common recurrence allowance. That
implication is imported as a paper result here; its coefficient ledgers
were not audited. The label amplitude is fixed as \(n\) changes.

## Exact correspondence with the packet code

Use `source_width = n` and `width = q`, with \(n,q\ge2\). In the ideal
Gaussian, exact-real interpretation, let
\(A_s\in\mathbb R^{n\times2}\), \(A_q\in\mathbb R^{q\times2}\), and
\(R\in\mathbb R^{q\times2}\) have independent standard Gaussian entries;
let \(G_q\in\mathbb R^{q\times q}\) have independent
\(N(0,1/q)\) entries. These arrays are mutually independent. Define

\[
 H_s=\tanh(A_s),\qquad H_q=\tanh(A_q),\qquad
 \Sigma_n=\frac1n H_s^\top H_s.
\]

Take the lower Cholesky factor \(J_n\) with
\(J_nJ_n^\top=\Sigma_n\), and write the thin QR factorization of \(R\)
with positive diagonal as \(R=UT\), so \(U^\top U=I_2\). The packet
preactivations and hidden mixer are exactly

\[
 Z_q=\sqrt q\,U J_n^\top,\qquad
 B_q=G_q+(Z_q-G_qH_q)H_q^\dagger,
\]

where \(H_q^\dagger=(H_q^\top H_q)^{-1}H_q^\top\).
The Gaussian arrays passed through \(\tanh\) have joint densities, so the
two feature columns have full rank almost surely when their row count is
at least two. Thus the Cholesky factor and displayed inverse exist almost
surely. The code's triangular solve is precisely this pseudoinverse action.
It follows algebraically that

\[
 B_qH_q=Z_q,\qquad Z_q^\top Z_q/q=\Sigma_n.
\]

These are covariance identities before the second \(\tanh\); they do not
assert equality of the nonlinear top-feature Gram. In code notation,
`w` is the first-layer matrix \(A_q\), `c` is the paper's readout \(w\),
and `matrix` is \(B_q\). The retained arrays then follow the same
`dense_rhs` flow, with the width normalization equal to \(q\).

At zero initial readout the hidden weight velocities vanish. Since
\(m=2\), the readout velocity is
\(\dot w(0)=\lambda\tanh(Z_q)e_1\). Consequently the exact initial
prediction velocity at the first training input is

\[
 \dot f_q^{\rm packet}(0,x_1)
   =\frac{\lambda}{q}\sum_{i=1}^q\tanh^2((Z_q)_{i1}).
\]

For an independent ordinary dense initialization
\((A_n,B_n,w_n=0)\), the corresponding identity is

\[
 \dot f_n^{\rm ind}(0,x_1)
   =\frac{\lambda}{n}\sum_{i=1}^n
       \tanh^2((B_n\tanh A_n)_{i1}).
\]

These identities are derived from the code, not imported asymptotic theorems.
The Gaussian idealization must replace finite pseudorandom seeds and numerical
rank decisions by the stated probability law and exact rank. This audit makes
no claim that a machine implementation has this asymptotic law at arbitrarily
large widths.

## Conditional implication for growing polylogarithmic width

Let \(q=q(n)\to\infty\) be an integer sequence with
\(q(n)\le C[\log(en)]^K\), where \(C,K\) are fixed. Put

\[
 D_n=\dot f_q^{\rm packet}(0,x_1)-\dot f_n^{\rm ind}(0,x_1).
\]

The following two statements are **hypotheses**, not results established by
this audit:

1. For some \(\sigma>0\),
   \(\sqrt q\,D_n\Rightarrow N(0,\sigma^2)\).
2. For a fixed \(t_0>0\), there are nonnegative random variables
   \(K_n=O_{\mathbb P}(1)\) such that, for all \(0\le t\le t_0\),

   \[
   |f_q^{\rm packet}(t,x_1)-t\dot f_q^{\rm packet}(0,x_1)|
   +|f_n^{\rm ind}(t,x_1)-t\dot f_n^{\rm ind}(0,x_1)|
   \le K_nt^2.
   \]

Here tightness \(K_n=O_{\mathbb P}(1)\) means that for every
\(\eta>0\), some finite \(M\) satisfies
\(\limsup_n\Pr(K_n>M)\le\eta\). A deterministic uniform remainder bound
implies this hypothesis. High-probability bounds with arbitrarily small
fixed failure probability and constants depending on that probability
also suffice. The interval and bounds must concern the actual nonlinear
flows in physical time.

The only dense accuracy result imported into the implication is the paper's
independent-dense upper theorem at failure probability \(10^{-4}\).
For the fixed problem above it supplies, at all sufficiently large
individual widths,

\[
 \Pr(\|f_n-\widetilde f_n\|_*\le U_n)\ge0.9999,
 \qquad
 U_n=C_*\,n^{-1/2}\log(en)e^{\sqrt{\log(en)}}.
\]

The constant \(C_*\) contains the fixed label, activation, depth, dimension,
sample and gap factors. By the definition of the quantile,
\(b_n\le U_n=n^{-1/2+o(1)}\). No sampled dense-pair event needs to be
intersected with the packet event: this is a deterministic bound on
\(b_n\). The dense lower theorem is not needed.

For \(t_n=1/q\), eventually \(t_n\le t_0\). The remainder hypothesis gives

\[
 \left|q^{3/2}
   \bigl(f_q^{\rm packet}(t_n,x_1)-f_n^{\rm ind}(t_n,x_1)\bigr)
   -\sqrt q\,D_n\right|\le\frac{K_n}{\sqrt q}.
\]

Polylogarithmic growth and the dense upper estimate imply
\(q^{3/2}b_n\le q^{3/2}U_n\to0\). If the requested all-time error event
holds, its restriction to this particular time and training input therefore
implies

\[
 |\sqrt q\,D_n|\le3q^{3/2}b_n+K_n/\sqrt q.
\]

To make the probability conclusion explicit, fix \(\eta>0\), choose the
tightness constant \(M\), and fix \(a>0\). For sufficiently large \(n\),
\(3q^{3/2}b_n+M/\sqrt q\le a\), so

\[
 \limsup_n\Pr(\|f_q^{\rm packet}-f_n^{\rm ind}\|_*\le3b_n)
 \le \eta+\Pr(|N(0,\sigma^2)|\le a).
\]

The Gaussian law has no atom at zero. Letting first \(a\downarrow0\) and
then \(\eta\downarrow0\) proves the conditional conclusion

\[
 \Pr(\|f_q^{\rm packet}-f_n^{\rm ind}\|_*\le3b_n)\longrightarrow0.
\]

Thus the requested 99% success statement would fail at every sufficiently
large individual width, under the two hypotheses. A training input is an
allowed witness for the full-sphere norm. A time tending to zero is also
allowed because the contract is uniform over all physical training times.
No fitted-endpoint obstruction is needed; a failure to have a required
fitted limit only makes the discrepancy infinite under the paper's convention.

## Probability qualifications and bounded packet widths

The phrase “nondegenerate \(q^{-1/2}\) fluctuations” needs a precise
probabilistic meaning. Nonzero variance alone is insufficient: a law can
have probability 0.999 at zero and still have positive variance. More
generally, if a velocity anti-concentration estimate gives

\[
 \liminf_n\Pr(|\sqrt qD_n|>a)\ge p
\]

for fixed \(a>0\), and the uniform remainder bound is available only on
events of asymptotic probability at least \(1-\varepsilon\), the same
argument gives a failure probability of at least \(p-\varepsilon\).
To contradict 99% success, one needs \(p-\varepsilon>0.01\).
Under the Gaussian limit but only one such remainder event,
the success limsup is at most \(\varepsilon\); one cannot claim success
tends to zero without the stronger tightness or vanishing-failure input.
No independence between the fluctuation and remainder events is needed.

For a fixed integer width \(q\ge2\), the growing-\(q\) CLT does not apply.
A sufficient replacement is a velocity limit \(D_n\Rightarrow D\) with
\(\Pr(D=0)=0\), together with the same tight short-time remainder.
Choose \(t_n=n^{-1/4}\). Then

\[
 \frac{f_q^{\rm packet}(t_n,x_1)-f_n^{\rm ind}(t_n,x_1)}{t_n}
   =D_n+O_{\mathbb P}(t_n),
 \qquad \frac{b_n}{t_n}\to0.
\]

The preceding probability argument again gives success tending to zero.
The non-atomicity of this fixed-width limit is an additional hypothesis
requiring proof elsewhere. If “polylogarithmic” permits bounded or
oscillating integer budgets, this fixed-width case must be combined with
the growing-width argument; it cannot be silently covered by a CLT
requiring \(q\to\infty\).

## Provenance and remaining obligations

The assigned sources were the setting in `paper/main.tex`,
`paper/results.tex`, the Logarithmic subsection of `paper/methods.tex`,
the shared setup, common label allowance and independent-dense upper
statements in `paper/integrated_appendix.tex`, and the exact
`BoundedGaussianPackets`, `dense_fields`, and `dense_rhs` implementations
in `paper/figures/capture_trajectory.py`.

Imported paper claims are the sufficient label cap's implication of the
full recurrence allowance, and the high-confidence all-time dense upper
certificate with its eventual-width qualification. Their full proofs were
outside this audit. The contract, decoder distinction, and normalization
are source definitions. The admissibility check, initial-velocity identities,
and conditional probability implication were derived here. The packet
velocity CLT, any fixed-width non-atomic limit, and the tight remainder
estimate for both actual flows remain separate proof obligations. No
conclusion about finite-step numerical trajectories follows without an
additional discretization analysis.
