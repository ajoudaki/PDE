# Preregistration: first-passage cooperative drift and gate closure

**Frozen before any outputs from this experiment are generated:** 23 August
2026.

## Question

The earlier endpoint experiment found that every sampled coordinate with
\(|R_{2,i}|\geq2\) at feature time four had a closed middle gate and that
\(R_{2,i}Z_{2,i}\) was almost always positive.  That observation does not say
whether the alignment is created dynamically or is merely an endpoint
selection effect.  This experiment follows first passages of a large query.

For the exact unit feature flow put

\[
 V=\dot Z_2=S+H,\qquad
 S=\|X_1\|_n^2D_2R_2,\qquad H=G_1D_1^2Q_1.
\]

The self term always points in the sign of \(R_2\).  A cooperative
slow-tube-exclusion mechanism predicts that a coordinate which first becomes
large while its gate is open and \(Z_2R_2\leq0\) normally has
\(\operatorname{sgn}(R_2)V>0\), then aligns, closes its gate, or drops below
the threshold in a dimension-free time.  Persistent opposing cancellation
would contradict that particular mechanism.  Neither outcome is a proof or
disproof of the desired tail theorem.

## Exact simulated fields

In addition to \(R_2,D_2,Z_2,S,H,V\), compute

\[
 \dot Z_3=\|X_2\|_n^2B_3+G_2D_2V,
\]

\[
 \dot B_3=D_3X_3-2Z_3D_3B_3\dot Z_3,
 \qquad
 \dot R_2=\|B_3\|_n^2X_2+G_2^{\mathsf T}\dot B_3.
\]

The implementation must audit these identities against a centered finite
difference on a small common draw; this derivative audit is diagnostic rather
than part of the formal support rule.

For \(L\in\{1.5,2,3\}\), a first passage occurs at the first mesh time at
which \(|R_2|\geq L\) after being below \(L\).  At that passage record

1. \(D_2\), the sign of \(Z_2R_2\), and
   \(\operatorname{sgn}(R_2)V/(|S|+|H|+10^{-12})\);
2. \(\operatorname{sgn}(R_2)\dot R_2\);
3. the opposing-bath ratio \(|H|/(|S|+10^{-12})\) when \(SH<0\);
4. the subsequent times to sign alignment \(Z_2R_2>0\), gate closure
   \(D_2<1/2\), and exit below \(L\), with right censoring at time four.

Over the whole path record the occupation and longest consecutive duration of

\[
 \mathcal O_L=\{|R_2|\geq L,\ D_2\geq1/2,\ Z_2R_2\leq0\},
\]

and of the stricter opposing slow tube

\[
 \mathcal C_L=\mathcal O_L\cap
 \{\operatorname{sgn}(R_2)V\leq |S|/4\}.
\]

## Simulation fixed in advance

- exact unscaled-arctangent unit feature flow and canonical iid Gaussian
  initialization;
- explicit midpoint, primary step \(h=0.01\), feature horizon four;
- widths \(512,1024,2048,4096\) and respectively \(64,32,16,8\)
  independent replicas (32768 coordinate paths per width);
- float32 state and float64 aggregation;
- master seed `2026082389`, with deterministic disjoint seeds by width and
  batch;
- a common-draw step-halving audit at width 512 with 16 replicas and a
  common-draw float32/float64 audit at width 256 with 16 replicas.

The analysis script and all thresholds below are frozen before simulation.

## Frozen interpretation

Only cells with at least 100 first passages and at least 25 open-misaligned
first passages are used for a formal comparison.  With right-censored times
replaced by their remaining horizon (a conservative convention), define for
the open-misaligned subgroup:

- \(p_{\rm coop}\): fraction with
  \(\operatorname{sgn}(R_2)V>0\) at first passage;
- \(m_{\rm resolve}\): median of the first time to any of alignment, gate
  closure, or exit;
- \(m_{\mathcal O}\) and \(m_{\mathcal C}\): median total occupations among
  all first-passage paths.

An **evidence-against-cooperative-drift** flag fires at \(T=4,L=2\) if the
eligible width-4096 cell satisfies any of

\[
 p_{\rm coop}<0.75,\qquad m_{\rm resolve}>0.25,
 \qquad m_{\mathcal C}>0.10,
\]

or if \(m_{\mathcal O}(4096)\) exceeds both `0.10` and 1.5 times its
width-512 value.  A **formal-support** flag requires an eligible width-4096
cell, no evidence-against flag, and additionally

\[
 p_{\rm coop}>0.90,\qquad m_{\rm resolve}<0.10,
 \qquad m_{\mathcal C}<0.05.
\]

The other thresholds, conditional distributions, maxima, \(L=1.5,3\), and
the \(\dot R_2\) statistic are diagnostic.  The formal rule deliberately does
not call the mechanism supported when large crossings are too rare or almost
never occur in the open-misaligned state.

## Numerical audits and claim boundary

For eligible probabilities the common-draw step-halving discrepancy must be
below `0.08`; for medians and occupations it must be below `0.04` in absolute
feature time.  Float32/float64 thresholds are `0.03` and `0.02`, respectively.
The algebraic residuals for \(V=S+H\), \(\dot Z_3\), and \(\dot R_2\) must be
below `1e-4` in float32 and `1e-9` in float64.

Passing would motivate a stopping-time/leave-two-out proof based on signed
occupation.  It cannot establish a rare-event probability, an Orlicz bound,
finite-width convergence, or any contract rung.  Failing rejects only this
specific cooperative first-passage mechanism.
