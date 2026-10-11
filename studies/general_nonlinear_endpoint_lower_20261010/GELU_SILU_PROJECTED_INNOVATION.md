# Query innovation for general nonconstant analytic activations

Scoped continuation, 2026-10-11. This note proves the projected-Gaussian
innovation propagation required by the supervisor's finite-oracle route.
It also supplies the final fourth-moment argument, which avoids needing
a conditional central limit theorem once a scalar variance lower bound
has been obtained. It does not prove the deferred-decisions representation
or the approximation of gradient flow by a finite oracle transcript.

New scientific inputs were Section 5 of `NONODD_SCALAR_ROUTE.md`, all of
`GELU_SILU_DIRECT_ROUTE.md`, and the supervisor's stated projected-Gaussian
oracle representation. Earlier permitted inputs and skill instructions are
recorded in `GELU_SILU_INNOVATION.md`. The fixed-depth constants below have
now been generalized from GELU/SiLU to arbitrary layerwise nonconstant
Lipschitz activations. That frozen note was not modified.
There were no experiments or external scientific dependencies.

## 1. A uniform one-layer lemma

Let \(P,Q\in\mathbb R^{n\times n}\) be orthogonal projections of
ranks \(k,k'\), respectively. Let \(b\in\mathbb R^n\) satisfy
\(\|b\|\le B\sqrt n\), and let
\(0<\sigma_0\le\sigma\le\sigma_1<\infty\). These objects are
deterministic for this lemma. For \(g\sim N(0,I_n)\), define
\[
 h(g)=\phi\bigl(b+\sigma(I-P)g\bigr),
 \qquad N(g)=\|(I-Q)h(g)\|.
 \tag{1}
\]
Here \(\phi\) is any continuous, nonconstant activation with Lipschitz
constant \(s\).  This includes every nonaffine activation in the compact
paper's class, because its derivative is bounded on the real axis.

Define constants
\[
 K=s\sigma_1,\qquad
 v=\min_{|a|\le2B+1,\;t\in[\sigma_0/\sqrt2,\sigma_1]}
       \operatorname{Var}\bigl(\phi(a+tG)\bigr),
 \quad G\sim N(0,1).
 \tag{2}
\]
Then \(v>0\). Indeed, if one variance were zero, the continuous
function \(\phi\) would be constant on the support of \(a+tG\),
which is all of \(\mathbb R\). This contradicts nonconstancy. The
variance is continuous in \((a,t)\): use the same Gaussian \(G\),
the Lipschitz bound, and the common integrable square bound on the compact
parameter rectangle. A positive continuous function has a positive
minimum on that rectangle.

If
\[
 k\le n/8,\qquad
 k'\le\frac{vn}{4K^2},\qquad
 n\ge\frac{8K^2}{v},
 \tag{3}
\]
then
\[
 \Pr\left\{\frac{\|(I-Q)h(g)\|^2}{n}<\frac v{32}\right\}
 \le\frac{32K^2}{vn}.
 \tag{4}
\]
All constants are uniform over \(P,Q,b,\sigma\) satisfying the
displayed conditions. These four objects may depend on a previously
conditioned training transcript, provided \(B,\sigma_0,\sigma_1\)
remain fixed bounds; (4) is unchanged.

To prove the lemma, first observe that at most \(n/4\) coordinates have
\(|b_i|>2B+1\), because
\[
 \#\{i:|b_i|>2B+1\}
 \le\frac{\|b\|^2}{(2B+1)^2}
 \le\frac{B^2n}{(2B+1)^2}\le n/4.
\]
Also \(P_{ii}\ge0\) and \(\sum_iP_{ii}=k\), so at most \(2k\)
coordinates have \(P_{ii}>1/2\). Consequently at least \(n/2\)
coordinates satisfy both \(|b_i|\le2B+1\) and \(P_{ii}\le1/2\).
For each such coordinate,
\[
 b_i+\sigma((I-P)g)_i
 \ \stackrel{\mathrm{law}}=\ b_i+
           \sigma\sqrt{1-P_{ii}}G,
\]
whose scalar standard deviation lies in the interval in (2). Therefore
\[
 \operatorname{tr}\operatorname{Cov}(h)\ge vn/2.
 \tag{5}
\]

For any deterministic \(a\in\mathbb R^n\), the map \(a^\top h(g)\)
is \(K\|a\|\)-Lipschitz. Gaussian Poincare, proved in Section 4 below,
gives
\[
 \operatorname{Var}(a^\top h)\le K^2\|a\|^2,
 \qquad \operatorname{Cov}(h)\preceq K^2I_n.
 \tag{6}
\]
Since \(I-Q\) is an orthogonal projection,
\[
 \begin{aligned}
 \mathbb EN^2
 &=\operatorname{tr}((I-Q)\operatorname{Cov}(h))
       +\|(I-Q)\mathbb Eh\|^2\\
 &\ge vn/2-k'K^2\ge vn/4.
 \end{aligned}
 \tag{7}
\]
The norm \(N\) is itself \(K\)-Lipschitz. A second application of
Gaussian Poincare yields \(\operatorname{Var}N\le K^2\), whence
\[
 (\mathbb EN)^2=\mathbb EN^2-\operatorname{Var}N
 \ge vn/4-K^2\ge vn/8.
 \tag{8}
\]
On the event \(N^2<vn/32\), (8) implies
\(\mathbb EN-N>\tfrac12\sqrt{vn/8}\). Chebyshev therefore gives
\(K^2/(vn/32)=32K^2/(vn)\), proving (4).

Notice that no covariance lower bound on the whole feature space was
claimed. The lower trace bound (5), combined with the upper operator bound
(6), only says that a projection of rank \(o(n)\) cannot remove most of
the random feature energy. Correlations between activated coordinates
and a large nonzero feature mean are both allowed.

## 2. The conditional Gaussian representation required for depth

The following representation is an explicit hypothesis, to be established
by the supervisor's deferred-decisions argument. Conditional on a training
transcript \(\mathcal T_n\), let the query recursion be
\[
 h^{(1)}=\phi_1(Z),\qquad Z\sim N(0,I_n),
\]
\[
 h^{(j)}=\phi_j\left(
  M_jh^{(j-1)}+
  (I-P_j)G_j(I-Q_{j-1})h^{(j-1)}/\sqrt n\right),
 \quad 2\le j\le L.
 \tag{9}
\]
Here \(M_j,P_j,Q_j\) are measurable with respect to the transcript;
\(P_j,Q_j\) are orthogonal projections of ranks at most \(r_n=o(n)\);
and \(Z,G_2,\ldots,G_L\) are mutually independent conditional on the
transcript, with their unconditioned standard Gaussian laws. The matrices
\(G_j\) have independent \(N(0,1)\) entries. One may set \(Q_L=0\)
when only the preceding-layer innovation is needed. Assume
\[
 \max_{2\le j\le L}\|M_j\|_{\rm op}\le a
 \tag{10}
\]
on a transcript-measurable event \(E_n\), whose probability tends to one;
\(a<\infty\) is fixed independently of width.

To identify the conditioning precisely, at layer \(j\) expose
\(\mathcal T_n,Z,G_2,\ldots,G_{j-1}\), but not \(G_j\) or later
matrices. Then \(h^{(j-1)}\), all projections and \(M_j\) are fixed.
The fresh Gaussian block remains independent of that exposure. Put
\[
 b_j=M_jh^{(j-1)},\qquad
 \sigma_j=\frac{\|(I-Q_{j-1})h^{(j-1)}\|}{\sqrt n}.
 \tag{11}
\]
For a fixed vector \(w\), the coordinates of \(G_jw\) are
independent centered Gaussians of variance \(\|w\|^2\), directly by
independence of the rows. Thus, under the stated conditioning, the
preactivation at layer \(j\) has exactly the law
\[
 b_j+\sigma_j(I-P_j)g_j,\qquad g_j\sim N(0,I_n).
 \tag{12}
\]
If \(\sigma_j=0\), the random term vanishes; the innovation induction
below excludes that case on its good event. An equivalent actual choice
when \(\sigma_j>0\) is
\(g_j=G_jw/\|w\|\), with \(w=(I-Q_{j-1})h^{(j-1)}\).

This argument verifies propagation of independence from the representation
(9). It does not derive (9) merely from finitely many training evaluations:
that is a separate necessary input. In particular, the projections at
layer \(j\) cannot be chosen after observing its unused \(G_j\), and
\(M_j\) cannot retain unrecorded dependence on future unused blocks.

## 3. Fixed-depth innovation and norm recursion

For each layer put
\[
 c_j=|\phi_j(0)|,\qquad
 s_j=\sup_{x\in\mathbb R}|\phi_j'(x)|.
\]
Assume every \(\phi_j\) is nonconstant.  Define
\[
 \nu_1=\operatorname{Var}(\phi_1(G)),\qquad
 H_1=c_1+2s_1,\qquad \kappa_1=\nu_1/32.
\]
Then \(\nu_1>0\): zero variance, continuity and the full support of the
Gaussian law would make \(\phi_1\) constant on \(\mathbb R\).  Recursively,
for \(2\le j\le L\), define
\[
 \begin{aligned}
 B_j&=aH_{j-1},&
 H_j&=c_j+s_j(a+2)H_{j-1},&K_j&=s_jH_{j-1},\\
 v_j&=\min_{|b|\le2B_j+1,\;
           t\in[\sqrt{\kappa_{j-1}/2},H_{j-1}]}
           \operatorname{Var}(\phi_j(b+tG)),&
 \kappa_j&=v_j/32.
 \end{aligned}
 \tag{13}
\]
These constants are finite, fixed and strictly positive where appropriate.
Gaussian Poincare gives \(\nu_1\le s_1^2\), hence
\(\kappa_1\le H_1^2\).  It also gives
\(v_j\le s_j^2H_{j-1}^2\), while
\(H_j\ge2s_jH_{j-1}\).  Thus \(\kappa_j\le H_j^2\), so every next
compact interval in (13) is nonempty.  The positivity argument in Section 1
applies recursively.

For sufficiently large individual widths, conditional on any transcript
in \(E_n\), with probability at least
\[
 1-\frac1n\left(
   \frac{16s_1^2}{\nu_1}+\frac{2L}{9}
        +\sum_{j=2}^L\frac{32K_j^2}{v_j}
              \right),
 \tag{14}
\]
one simultaneously has
\[
 \frac{\|h^{(j)}\|}{\sqrt n}\le H_j,
 \qquad
 \frac{\|(I-Q_j)h^{(j)}\|^2}{n}\ge\kappa_j,
 \quad 1\le j\le L.
 \tag{15}
\]
Thus the unconditional probability of (15) is at least the expression
in (14) minus \(\Pr(E_n^c)\). No claim that these constants are small
or polynomial in the data gap is needed for this fixed-problem result.

For the first layer, the coordinates of \(h^{(1)}\) are independent, giving
\[
 \operatorname{Cov}(h^{(1)})=\nu_1I_n,
 \qquad
 \mathbb E\|(I-Q_1)h^{(1)}\|^2
       \ge\nu_1(n-r_n)\ge\nu_1n/2
\]
once \(r_n\le n/2\). This norm is \(s_1\)-Lipschitz and has variance at
most \(s_1^2\).  Once \(n\ge4s_1^2/\nu_1\), its mean squared is at least
\(\nu_1n/4\). Consequently Chebyshev bounds the probability that its
squared norm is smaller than \(\nu_1n/32\) by
\(16s_1^2/(\nu_1n)\), proving the initial innovation lower bound.
Moreover \(|\phi_1(z)|\le c_1+s_1|z|\), and
\[
 \Pr\{\|Z\|>2\sqrt n\}
 \le\frac{\operatorname{Var}(\|Z\|^2)}{(3n)^2}
 =\frac{2}{9n},
 \tag{16}
\]
because independent standard Gaussians have squared-norm mean \(n\)
and variance \(2n\).

Suppose (15) holds through layer \(j-1\). Conditional on the exposure
in Section 2,
\[
 \|b_j\|/\sqrt n\le aH_{j-1}=B_j,
 \qquad \sqrt{\kappa_{j-1}}\le\sigma_j\le H_{j-1}.
\]
Apply (4) with \(P=P_j\), \(Q=Q_j\), \(v=v_j\) and \(K=K_j\).
Its hypotheses hold for all sufficiently large widths: since depth is
fixed and \(r_n/n\to0\), all finitely many inequalities
\[
 r_n\le n/8,\qquad
 r_n\le v_j n/(4K_j^2),\qquad n\ge8K_j^2/v_j
\]
eventually hold. The conditional innovation failure probability is
at most \(32K_j^2/(v_jn)\).

For the norm upper bound use (12),
\(|\phi_j(z)|\le c_j+s_j|z|\), and
\(\|I-P_j\|_{\rm op}\le1\). On \(\|g_j\|\le2\sqrt n\),
\[
 \|h^{(j)}\|/\sqrt n
 \le c_j+s_j\bigl(\|b_j\|/\sqrt n
                  +\sigma_j\|g_j\|/\sqrt n\bigr)
 \le c_j+s_j(a+2)H_{j-1}=H_j.
 \tag{17}
\]
The conditional complement has probability at most \(2/(9n)\) by
(16). Applying a union bound to successive conditional failure events
proves (14); independence of those good events is unnecessary.

A useful source of (10) is the following transcript-certified bound,
supplied with the supervisor's oracle construction. Suppose the
conditional-mean initialized mixer has the exact representation
\[
 M_{0,j}=W_0^{(j)}Q_{j-1}+P_jW_0^{(j)}(I-Q_{j-1}),\qquad
 M_j=M_{0,j}+\Delta_j,
\]
where both terms on the right defining \(M_{0,j}\) have been revealed
by the transcript, and \(\Delta_j\) is its recorded training update.
Contraction of orthogonal projections gives
\[
 \|M_{0,j}\|_{\rm op}\le2\|W_0^{(j)}\|_{\rm op}.
\]
On the source events \(\|W_0^{(j)}\|_{\rm op}\le8\) and
\(\|\Delta_j\|_{\rm op}\le1\), therefore,
\(\|M_j\|_{\rm op}\le17\). The event
\(\{\max_j\|M_j\|_{\rm op}\le20\}\) is transcript measurable,
and its complement is contained in the union of those source failures.
When their probabilities vanish, it is an admissible \(E_n\) with
\(a=20\). The resulting explicit recursion is
\[
 H_1=c_1+2s_1,\qquad
 H_j=c_j+22s_jH_{j-1},\qquad B_j=20H_{j-1}\quad(j\ge2).
\]
This argument only uses the initial operator bound to estimate the
probability of a transcript-measurable event. It does not condition the
fresh Gaussian in (12) on an operator-norm event, which would change its
law. The initial operator probability and the update estimate are supplied
by their respective initialization and finite-flow estimates. The query
upper bound itself requires only the scalar Gaussian norm event (16),
not any further bound on a fresh matrix's operator norm.

## 4. Gaussian Poincare and the final fourth-moment implication

For completeness, the Gaussian Poincare inequality used above is
\[
 \operatorname{Var}(F(G))\le\mathbb E\|\nabla F(G)\|^2,
 \qquad G\sim N(0,I_N).
 \tag{18}
\]
One proof is the following Gaussian interpolation. Define
\(T_tF(x)=\mathbb E F(e^{-t}x+\sqrt{1-e^{-2t}}G')\), with an
independent standard Gaussian \(G'\). Differentiating the Gaussian
integral and integrating its density derivative by parts gives
\(\partial_tT_tF=\Delta T_tF-x^\top\nabla T_tF\). A further
integration by parts against the standard Gaussian density gives
\[
 \frac{d}{dt}\mathbb E(T_tF(G))^2
 =-2\mathbb E\|\nabla T_tF(G)\|^2.
\]
Since \(\nabla T_tF=e^{-t}T_t\nabla F\), Jensen's inequality and
Gaussian stationarity bound the right-hand gradient energy by
\(e^{-2t}\mathbb E\|\nabla F(G)\|^2\). Integrate from zero to
infinity and use \(T_tF\to\mathbb EF(G)\) in Gaussian \(L^2\) to
obtain (18), since \(2\int_0^\infty e^{-2t}dt=1\).
For smooth functions with polynomial growth these differentiations and
integrations follow by Gaussian domination and truncation. Lipschitz
functions follow by smooth approximation with the same Lipschitz bound;
this includes the norm in (1). The squared centered Lipschitz functions
used next have at most quadratic growth and satisfy the same truncation
argument.

Let \(F\) be a scalar \(K_F\)-Lipschitz function of a standard
Gaussian vector and put \(X=F-\mathbb EF\). Applying (18) first to
\(F\), then to \(X^2\), gives
\[
 \mathbb EX^2\le K_F^2,\qquad
 \operatorname{Var}(X^2)\le4K_F^2\mathbb EX^2\le4K_F^4,
 \qquad \mathbb EX^4\le5K_F^4.
 \tag{19}
\]
Now condition on two independent runs' transcripts and query histories
through layer \(L-1\). Suppose a final-layer argument supplies fixed
constants \(c>0\) and \(K_*<\infty\), uniform in width and in the
admissible conditioning, such that
\[
 \operatorname{Var}(F-\widetilde F)\ge cE/n,
 \qquad
 \operatorname{Lip}(F-\widetilde F)^2\le K_*^2E/n,
 \quad E=\|u\|^2+\|\widetilde u\|^2>0,
 \tag{20}
\]
where the remaining independent Gaussian variables are the two fresh
final-layer query vectors. The readouts \(u,\widetilde u\) are fixed
under this conditioning. For the usual scalar
\(F=u^\top\phi(b+\sigma(I-P)g)/\sqrt n\), its Lipschitz constant
is at most \(s\sigma\|u\|/\sqrt n\); thus the upper bound in
(20) follows from the already proved bound \(\sigma\le H_{L-1}\).
Only the scalar variance lower bound in (20) remains to be supplied by
the supervisor's separate weighted covariance argument.

Put \(D=F-\widetilde F\), \(\mu=\mathbb ED\), and
\(V=\operatorname{Var}D\). Since
\(|x+y|^4\le8(|x|^4+|y|^4)\), (19) and (20) yield
\[
 \begin{aligned}
 \mathbb ED^4
 &\le8\left(5K_*^4E^2/n^2+\mu^4\right)\\
 &\le8\max\{1,5K_*^4/c^2\}\left(V^2+\mu^4\right)\\
 &\le8\max\{1,5K_*^4/c^2\}(\mathbb ED^2)^2.
 \end{aligned}
 \tag{21}
\]
To derive the needed second-moment inequality directly, put
\(A=\{D^2\ge\mathbb ED^2/2\}\). Splitting the expectation over
\(A\) and its complement, then applying Cauchy--Schwarz, gives
\[
 \tfrac12\mathbb ED^2
 \le\mathbb E[D^2\mathbf1_A]
 \le(\mathbb ED^4)^{1/2}\Pr(A)^{1/2}.
\]
Together with (20)--(21), this proves
\[
 \Pr\left\{|F-\widetilde F|\ge\sqrt{cE/(2n)}\right\}
 \ge\frac1{32\max\{1,5K_*^4/c^2\}}>0.
 \tag{22}
\]
The conditional means are arbitrary throughout. The probability in (22)
may be small but is independent of width; this is enough for the requested
positive-probability endpoint separation. A normal approximation and a
comparison of a small variance constant with a fixed training perturbation
are unnecessary for this step.

The proved contributions of this note are (4), the conditional fixed-depth
propagation (14)--(15) under the exact representation (9), and the
conditional scalar implication (22). Establishing (9), controlling the
finite-oracle approximation error, and proving the final weighted scalar
variance bound remain separate inputs.
