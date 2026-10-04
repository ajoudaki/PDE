# What the sample normalization does, and does not, force

2026-10-04. Bounded clarification of the dataset-dependence theorem.
This note proves algebraic refinements and exact fixed-feature identities;
it does not establish a larger-label deep-compression theorem or a
compression lower bound. The complete relevant study proofs were already
read, and their unchanged versions were verified. No new study input,
experiment, manuscript edit or Git mutation is involved.

## 1. Trace, gap, and label normalization

Let $Q=Q^{(L)}$ be the deterministic initialized top-feature Gram from
the existing covariance recursion. Each entry is a normalized feature
inner product; there is no division by the number of samples in $Q$.
If the last activation is bounded by $B_\phi$, then

\[
 Q_{aa}\le B_\phi^2,\qquad
 \frac1m\operatorname{tr}Q\le B_\phi^2.
\]

Thus the average eigenvalue is bounded independently of $m$. It need
not be bounded below solely from boundedness of the activation. Put
$\gamma=\lambda_{\min}(Q)>0$. Ignoring the harmless cap at one,
the earlier theorem uses $\lambda=\gamma/m$, and
$Y=\|y\|_2/\sqrt m$ is label RMS. The division by $m$ comes
from the mean-loss residual equation, not from an additional normalization
of neuron features.

The sharpened full compression certificate currently requires

\[
             Y\le c\frac\gamma m
                       e^{-C\sqrt{\log(em)}}.
\]

There is no result in this study proving that the factor $1/m$ here
is necessary for the actual deep compression problem. The normalized
smallest eigenvalue bounds the worst-direction decay rate, but a rate
bound alone is not a necessary bound on label amplitude.

## 2. The precise loss in the real-fitting certificate

The complete energy proof in DATASET_LABEL_DEPENDENCE.md gives, on a
stopped initialized-Gram tube and in the canonical mobility metric,

\[
 \int_0^\infty\rho(t)\,dt\le CY/\lambda,\qquad
 \|w(t)\|_n\le CY/\sqrt\lambda,\qquad
 \max_a\|h_a^{(L)}(t)-h_a^{(L)}(0)\|_n
              \le CY^2/\lambda^{3/2}.
\]

Here $\rho$ is residual RMS and $\|u\|_n=\|u\|_2/\sqrt n$.
The normalized feature matrix $H_L/\sqrt{mn}$ initially has smallest
singular value at least $\sqrt\lambda$. The proof bounds its operator
perturbation by the RMS of the displayed individual feature bounds.
It therefore closes by imposing

\[
            CY^2/\lambda^{3/2}\le c\sqrt\lambda,
            \quad\hbox{equivalently}\quad Y\le c\lambda.
\]

This is where $Y\le c\gamma/m$ enters. The estimate replaces the
actual residual quadratic form by its smallest-eigenvalue lower bound
and does not exploit label alignment or cancellation between samples'
feature movements. It is a sufficient perturbative certificate. It
does not prove that fitting or compression fails outside its tube.

## 3. Exact fixed-feature diagnostic, with its limited scope

For this paragraph only, fix a feature matrix
$H=[h_1,\ldots,h_m]\in\mathbb R^{n\times m}$ with
$Q=H^\top H/n\succ0$. Train only the readout, from $w(0)=0$,
with $f=H^\top w/n$ and $\dot w=2H(y-f)/m$. Then

\[
 c(t)=e^{-2Qt/m}y,\qquad
 w(t)=HQ^{-1}(I-e^{-2Qt/m})y.
\]

Indeed $\dot c=-2Qc/m$, and integrating the readout velocity gives
the second formula. At the fitted endpoint,

\[
                        \|w(\infty)\|_n^2=y^\top Q^{-1}y.
\]

This is also the minimum normalized squared norm of any fitting
readout: all fitting readouts equal $HQ^{-1}y$ plus a vector in
$\ker H^\top$, orthogonal to the displayed solution.

If $Q=\gamma I_m$, this cost is $mY^2/\gamma$. Keeping the
readout RMS of order one would then allow label scale
$Y=O(\sqrt{\gamma/m})$, whereas the current real deep-fitting
certificate asks for the smaller scale $O(\gamma/m)$ when
$\gamma/m$ is small. This comparison does not prove the larger
label range for moving hidden layers. The fixed-feature flow itself
fits every finite label vector, without a small-label condition.

Label direction matters as well. If
$Q=a\mathbf1\mathbf1^\top+\gamma I_m$ with $a>0$ and
$y=Y\mathbf1$, then the average trace is $a+\gamma$, while

\[
 y^\top Q^{-1}y=\frac{mY^2}{am+\gamma},\qquad
 \rho(t)=Y e^{-2(am+\gamma)t/m}.
\]

Both the readout cost and training rate are well controlled independently
of $m$ at fixed $a,\gamma$. The small eigenvalue in orthogonal label
directions is irrelevant to this particular frozen-feature fit. These
matrices are elementary spectral diagnostics, not asserted constructions
of the actual trained canonical network. Moving features can couple
directions, so neither diagnostic proves or disproves a sharper full
deep-compression theorem.

## 4. Changing the loss scale does not repair the existing proof

Multiplying the loss by $\alpha>0$ multiplies every velocity by
$\alpha$. Uniqueness gives
$\theta_\alpha(t)=\theta_1(\alpha t)$, and hence

\[
 \int_0^\infty\rho_\alpha(t)\,dt
     =\alpha^{-1}\int_0^\infty\rho_1(t)\,dt.
\]

The integrated parameter velocities retain the compensating factor
$\alpha$. For summed rather than mean loss, $\alpha=m$:
the rate uses $\gamma$ rather than $\gamma/m$, but the update
coefficients also acquire $m$. The parameter path and fitted endpoint
are identical. A new label theorem must therefore improve estimates of
the motion, not merely rescale time or change the name of the gap.

## 5. The storage bound before collapsing its two terms

Write $\ell=\log(en)$,
$a=d(L+5)+1$, and $b=L+6$. The existing source construction gives
the following source-space dimension per layer:

\[
 R\le C\{\lambda^{-1}(\ell^a+m\ell^b)+d\}.
\]

The two terms count sphere-query sources and training-only response
sources. Positive cubature selects $O(R^2)$ neurons per layer;
storing their dense trained connecting matrices costs $O(R^4)$ real
coordinates. Consequently the existing proof gives the more informative
total-storage bound

\[
 \mathrm{size}\le C\lambda^{-4}
                  (\ell^{4a}+m^4\ell^{4b})+Cm(d+1).
\]

To verify this refinement, absorb fixed-$d$ lower-order terms using
$\lambda\le1$, $m\ge1$, $\ell\ge1$, and use
$(u+v)^4\le8(u^4+v^4)$. With $\lambda=\gamma/m$ this is

\[
 \mathrm{size}\le C\gamma^{-4}
               (m^4\ell^{4a}+m^8\ell^{4b})+Cm(d+1).
 \tag{1}
\]

Thus the user's $m^8$ reading of the coarser bound is correct. Formula
(1) avoids assigning that coefficient to the larger logarithmic power.
Since $a-b=(d-1)(L+5)=:\Delta>0$ for $d\ge2$, if

\[
 \ell^\Delta\ge m,
 \quad\hbox{equivalently}\quad
 n\ge\exp(m^{1/\Delta}-1),
\]

then the first term in (1) dominates, and storage is at most
$C m^4\gamma^{-4}\ell^{4a}+Cm(d+1)$. This is a valid explicit
additional-width simplification, not a joint growing-data theorem or
a uniform elimination of the second term at arbitrary widths. The
original source-probability width threshold is still required.

Neither $m^8$ nor $m^4$ is proved necessary. The training-source span
count, the quadratic cubature count and the dense-edge count are upper
bounds for one construction. Dependencies among response coefficients
may reduce the actual source span. Exact preservation of a full-rank
$m$-sample top feature Gram forces at least $m$ selected top neurons
in this construction; it does not imply an $m^4$ or $m^8$ lower bound,
nor a lower bound for every autonomous representation.

Finally, rescaling time alone does not remove the horizon factor in
this source approximation. The proven physical-time horizon is
$T\asymp(m/\gamma)\ell$ and strip radius is
$r\asymp\ell^{-(L+4)}$. Under $\tau=t/m$, they become
$T/m$ and $r/m$, so the approximation ratio $T/r$ is unchanged.
Keeping radius $r$ in the new clock would assume an unproved larger
physical-time strip. A better approximation or a smaller dynamical
representation remains a mathematical question, not a notation change.

## 6. Check and conclusion

The real-fitting author independently reconstructed the threshold loss,
fixed-feature solution and exact loss-rescaling identity. The source-
constant author independently reconstructed (1), its additional-width
simplification and the strip rescaling. The coordinator checked all
displayed algebra against the unchanged sources:

- DATASET_LABEL_DEPENDENCE.md,
  `bfd01ccacf6c78337331cf16a0c7137353d31c9a7e4d3b08357af7e32f356f52`;
- DATASET_DEPENDENCE.md,
  `304363d4587c94ee997bc2fb573446d30a6cd878fce547f1a78e6390ca4f4170`.

The bounded conclusions pass this internal check. Sample-average trace
normalization is already correct in $Q$. The extra inverse-sample factor
in the label certificate and the high storage powers have no matching
necessity theorem. There is explicit looseness, especially in the storage
count and worst-label-direction estimates, but no proof yet removing
all such dependence for the actual all-layer training dynamics.
