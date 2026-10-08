# Causal kernel dynamics: the actual neural circuit without learned matrices

2026-10-07. Lead synthesis and finite-program derivation. This note gives
the explicit neural specialization of RESPONSE_GAUSSIAN_CLOSURE.md, rather
than leaving its queries as an abstract program. It identifies a new useful
part of the mechanism: an instantaneous curvature response propagating
backward through squared activation sensitivities.

The theorem is a **fixed finite Euler-history law**. It is not yet a
finite-dimensional all-time closure at dense-variability accuracy. The
probability laws and derivative responses below are real state information;
a covariance table alone is not their substitute.

## 1. Setup and the few objects being retained

There are \(m\) training inputs and a finite declared panel of \(p\ge m\)
training and passive inputs, all \(v_a=x_a/\sqrt d\) of unit norm. Depth is
\(L\). The training deficit is \(c_a^k=y_a-f_a^k\), only for \(a\le m\).
Take a fixed number of Euler steps of size \(\Delta t>0\). Activations have
bounded derivatives and bounded second derivatives, and may have unbounded
values of at most linear growth. The analytic class in the source satisfies
these conditions.

In each neuron population retain the joint scalar law of the forward
preactivations \(z_{\ell,a}^k\), features \(h_{\ell,a}^k=\phi_\ell(z_{\ell,a}^k)\),
backward carriers \(b_{\ell,a}^k\), gated backward responses
\(\delta_{\ell,a}^k=\phi_\ell'(z_{\ell,a}^k)b_{\ell,a}^k\), and the top
readout \(w^k\). These are scalar fields, not width-\(n\) vectors. Expectations
below are within the indicated population's law.

The two similarity kernels are
\[
 C_{\ell,ab}(k,j)=\mathbb E[h_{\ell,a}^k h_{\ell,b}^j],
 \qquad
 D_{\ell,ab}(k,j)=\mathbb E[\delta_{\ell,a}^k\delta_{\ell,b}^j],
 \qquad C_{0,ab}(k,j)=v_a^\top v_b .
 \tag{1}
\]
Thus \(C\) measures feature agreement at possibly different times; \(D\)
measures agreement of loss-to-layer responses. Neither is centered.

For each adjacent-layer initialized interface \(\ell\ge2\), introduce
centered primitive Gaussian families \(\eta_{\ell,a}^k\) in the upper
population and \(\xi_{\ell,a}^k\) in the lower population, with covariances
\[
 \mathbb E[\eta_{\ell,a}^k\eta_{\ell,b}^j]=C_{\ell-1,ab}(k,j),
 \qquad
 \mathbb E[\xi_{\ell,a}^k\xi_{\ell,b}^j]=D_{\ell,ab}(k,j).
 \tag{2}
\]
Different primitive families and the first-layer Gaussian root are independent.
Coordinates *within* a family are colored by (2), not independently refreshed.
The two families at an interface live in different neuron populations.

Finally, two directed susceptibilities record total local responses:
\[
 R^h_{\ell,ab}(k,j)
   =\mathbb E\!\left[\frac{\partial h_{\ell-1,a}^k}
                              {\partial \xi_{\ell,b}^j}\right],
 \qquad
 R^\delta_{\ell,ab}(k,j)
   =\mathbb E\!\left[\frac{\partial \delta_{\ell,a}^k}
                              {\partial \eta_{\ell,b}^j}\right].
 \tag{3}
\]
A derivative passes through the whole already-built scalar circuit, with
all population moments, covariances, deficits and response coefficients
held fixed. It is not a derivative of a whitened Gaussian coordinate, or a
population-wide perturbation of the data. These are the probes used in the
proved Gaussian cancellation.

There is no assumption of invertible history covariances. If a Gaussian
family has singular support, individual derivatives can depend on their
smooth off-support extension; their response-weighted field sums do not.
This is precisely the null-space invariance proved in the response-law note.

## 2. The closed chronological equations

Let the first-layer root \(z_{1,a}^0\) be a centered Gaussian panel with
covariance \(v_a^\top v_b\). The first layer and readout satisfy
\[
 z_{1,a}^k=z_{1,a}^0+
 \frac{2\Delta t}{m}
 \sum_{j<k}\sum_{b\le m}
 c_b^j(v_b^\top v_a)\delta_{1,b}^j,
 \qquad
 w^k=\frac{2\Delta t}{m}
 \sum_{j<k}\sum_{b\le m}c_b^j h_{L,b}^j .
 \tag{4}
\]
The prediction and current top carrier are
\[
 f_a^k=\mathbb E[w^k h_{L,a}^k]
 =\frac{2\Delta t}{m}
   \sum_{j<k}\sum_{b\le m}c_b^j C_{L,ab}(k,j),
 \qquad b_{L,a}^k=w^k .
 \tag{5}
\]

For each hidden interface \(\ell\ge2\), its forward preactivation is
\[
\begin{aligned}
 z_{\ell,a}^k={}&\eta_{\ell,a}^k\\
 &+\sum_{j<k}\sum_{b\le p}
        R^h_{\ell,ab}(k,j)\delta_{\ell,b}^j\\
 &+\frac{2\Delta t}{m}\sum_{j<k}\sum_{b\le m}
        c_b^j C_{\ell-1,ab}(k,j)\delta_{\ell,b}^j .
\end{aligned}
\tag{6}
\]
The backward carrier in the lower population is
\[
\begin{aligned}
 b_{\ell-1,a}^k={}&\xi_{\ell,a}^k\\
 &+\sum_{j\le k}\sum_{b\le p}
        R^\delta_{\ell,ab}(k,j)h_{\ell-1,b}^j\\
 &+\frac{2\Delta t}{m}\sum_{j<k}\sum_{b\le m}
        c_b^j D_{\ell,ab}(k,j)h_{\ell-1,b}^j .
\end{aligned}
\tag{7}
\]
The symmetry of real products identifies the displayed order of the
arguments in \(C,D\) with the inner products obtained from matrix expansion.

Equations (1)--(7), the pointwise activations/gates and \(c=y-f\) form a
closed chronological scalar-law computation:

1. At a step, compute forward layers from bottom to top. Each new forward
   query input, its covariance row and its susceptibility are known before
   its new primitive Gaussian coordinate is appended.
2. Compute the output and training deficits.
3. Compute backward layers from top to bottom. The new reverse input is
   available before its Gaussian coordinate is appended.
4. The next step uses only this completed history.

There is no unknown learned matrix or dense reference call in these equations.
There is also no claim that a finite list of covariances computes the
expectations in (3): the local scalar laws/circuits are retained.

The sums over \(p\) in the reciprocal terms are *observation* histories,
not training forces. Passive response probes can be included or omitted
without changing the active computation. In the canonical circuit written
with independent primitive coordinates before imposing their covariance,
an active field has no computational dependence on passive primitive
coordinates; its associated derivatives vanish. Diagnostic passive probes
therefore never create a training force. The actual learned writes in (4),
(6), (7), and the deficit in (5), always sum only over \(b\le m\).

## 3. Why these are the dense network's finite-step laws

At finite width, expanding the physical gradient updates gives exactly
\[
 W_\ell^k=W_\ell^0+
 \frac{2\Delta t}{mn}
 \sum_{j<k,b\le m}c_b^j\delta_{\ell,b}^j
                         (h_{\ell-1,b}^j)^\top .
\]
Applying this equality to the current feature gives the last line of (6).
Applying its transpose to the current backward response gives the last
line of (7). The first-layer and readout expansions give (4)--(5).
No approximation has been used in these learned-memory identities.

The only initialized actions remaining are \(W_\ell^0h_{\ell-1,a}^k\)
and \((W_\ell^0)^\top\delta_{\ell,a}^k\). The inverse-Gram-free Gaussian
response theorem identifies their finite-program scalar laws with
\[
 \eta_{\ell,a}^k+
   \sum_{j<k,b}R^h_{\ell,ab}(k,j)\delta_{\ell,b}^j,
 \qquad
 \xi_{\ell,a}^k+
   \sum_{j\le k,b}R^\delta_{\ell,ab}(k,j)h_{\ell-1,b}^j .
\]
Forward queries have no current-step reverse dependence. Reverse queries
may depend on already-computed forward queries in the current step.
The unclipped finite-program theorem then identifies the actual neural
Euler limits, including joint forward/backward pairings and passive outputs.

For every fixed such program with \(Q\) instructions, the quantitative
theorem in FIXED_HISTORY_RATE.md applies: prediction and pairing errors
are at most
\[
 C_r n^{-1/2}[\log(en)]^{2Q+2}
\]
outside probability \(C_r n^{-r}\), at sufficiently large \(n\).
Its constants depend on the fixed program, data, gates and positive
retained-history gaps. Formulae (6)--(7) contain no inverse Gram, but this
fact does not by itself remove those dependencies from the rate proof.

This statement compares with the fixed Euler computation, not the continuous
dense gradient flow. CONTINUOUS_RESPONSE_LIMIT.md proves a separate
conditional qualitative all-time limit and explains why it does not yet
supply the requested simultaneous root-width guarantee.

## 4. The same-time response is an explicit curvature recursion

There is a sharper structural fact within (7). Current-step derivatives
between different panel indices vanish:
\[
 R^\delta_{\ell,ab}(k,k)=0\quad(a\ne b).
\]
Define the diagonal instantaneous susceptibility, locally in this section,
by \(\chi_{\ell,a}^k=R^\delta_{\ell,aa}(k,k)\).
Then
\[
\begin{aligned}
 \chi_{L,a}^k
   &=\mathbb E[w^k\phi_L''(z_{L,a}^k)],\\
 \chi_{\ell,a}^k
   &=\mathbb E[b_{\ell,a}^k\phi_\ell''(z_{\ell,a}^k)]
     +\chi_{\ell+1,a}^k\,
        \mathbb E[(\phi_\ell'(z_{\ell,a}^k))^2],
       \qquad \ell<L .
\end{aligned}
\tag{8}
\]
For \(\ell=1\) the last formula is a useful local derivative identity
rather than a reciprocal term for a nonexistent square initialized
first-layer interface.

Here is the full derivation. At the top, \(w^k\) depends only on past
fields. The current primitive \(\eta_{L,a}^k\) enters its preactivation
with coefficient one, and no other current primitive enters that local
formula. Differentiating \(\delta_{L,a}^k=w^k\phi'_L(z_{L,a}^k)\)
gives the first equality and the diagonal assertion.

Inductively, in population \(\ell\), every term of (7) except the
current-step reciprocal sum is either a primitive from a different family
or a past local field with a frozen coefficient. Thus
\[
 \frac{\partial b_{\ell,a}^k}{\partial\eta_{\ell,b}^k}
 =R^\delta_{\ell+1,ab}(k,k)\phi_\ell'(z_{\ell,b}^k).
\]
The derivative of \(\delta_{\ell,a}^k\) is consequently
\[
 \mathbf1_{a=b}b_{\ell,a}^k\phi_\ell''(z_{\ell,a}^k)
 +R^\delta_{\ell+1,ab}(k,k)
       \phi_\ell'(z_{\ell,a}^k)\phi_\ell'(z_{\ell,b}^k).
\]
Expectation proves the general recursion; a diagonal top response implies
a diagonal response at every lower layer, giving (8).

The current response term in (7) is therefore exactly
\(\chi_{\ell,a}^k h_{\ell-1,a}^k\). It has a concrete meaning:

- \(\mathbb E[b\phi'']\) is carrier-weighted local activation curvature;
  its sign is not constrained to be positive.
- Squared activation sensitivity transmits the higher layer's curvature
  response downward.
- The remaining strict-past response terms record delayed reciprocal
  feedback, including effects that remain for linear activations.

Thus nonlinear curvature is not merely an unspecified change in a kernel.
It creates a sample-specific instantaneous susceptibility, while training
also accumulates directed memory.

At zero readout all backward responses and their susceptibilities are zero.
In continuous-time notation for the initial right derivative, the top
susceptibility begins as
\[
 \left.\frac{d}{dt}\chi_{L,a}(t)\right|_{t=0}
 =\frac2m\sum_{b\le m}y_b\,
   \mathbb E[h_{L,b}(0)\phi_L''(z_{L,a}(0))].
 \tag{9}
\]
This identity needs only the initial derivative, not a theorem for
continuous response measures: the top expression in (8) is well defined
for the initialized Hilbert flow, and its readout starts at zero.
For example, the self-label contribution for top activation \(\tanh\) is
\(-4y_a\,\mathbb E[\tanh^2(z_{L,a}(0))
\operatorname{sech}^2(z_{L,a}(0))]/m\).
Other samples contribute their displayed signed correlations; this example
does not assert a universal sign for their sum.

## 5. What the interaction law says, without a metaphor

Each history term has two independently defined ingredients. In the
learned part of (6), the past sample's unmet label \(c_b^j\) multiplies
feature agreement \(C_{\ell-1,ab}(k,j)\); its backward response
\(\delta_{\ell,b}^j\) is the direction written into the current representation.
In (7), backward agreement \(D_{\ell,ab}(k,j)\) selects which earlier
forward features contribute to the present backward carrier.
These are the dual sides of the same rank-one learning write.

The reciprocal terms have no additional label multiplier because the
sensitivities \(R\) already describe the effect of earlier learning on
the current query. They correct for using *the same initialized map*
in both directions. Removing them changes the limiting law, even in
simple linear forward/reverse query cycles. They are not a small noise
adjustment that can be discarded in a feature-learning regime.

Equations (2) and (8) separate two different notions often both called
a kernel: an undirected similarity sets the strength of a Gaussian
field shared across samples and times; a directed susceptibility tells
how a perturbation at one earlier response changes a later feature.
Neither object replaces the other.

The output takes the especially transparent form (5): it accumulates
past training deficits, weighted by the similarity between today's
query feature and each earlier training feature. Feature learning is
precisely the evolution of those two-time similarities, mediated by
the dual learned writes and the reciprocal susceptibilities.

## 6. Remaining proof obligations

This is an exact specialization of the proved fixed-program scalar law.
It retains full chronological scalar-response laws and their histories;
the number of retained events grows with the chosen discretization.
It does not prove a fixed-dimensional restartable ODE, a uniform growing-
history width rate, or an all-time dense-variability comparison.

The conditional Hilbert-flow result supplies a genuine continuous limiting
network and all-time qualitative prediction convergence under stated source
budgets. A rigorous continuum limit of the explicit response sums, with
their same-time atoms, is a further question. A useful finite explanatory
closure must also approximate that law with a controlled dense-width rate.
Those are the current mathematical gaps, not cosmetic changes of notation.

