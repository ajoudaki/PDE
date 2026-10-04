# Supervised population addresses: the final candidate fails its practical gate

This candidate replaces per-example or feature-PCA addresses with two label
populations for classification and four training-target quantile bins for
regression. It is a substantive architectural alternative: it avoids a stored
initial first-layer dictionary and groups writes by supervision. It still does
not outperform tuned factors across the tested domains. Its definition and
42-fit terminal protocol were frozen before fitting; all outcomes are retained.

## Definition and correspondence

Under the empirical law of training pairs(x,y), let c(y) denote a class or
training-quantile bin, p_c its positive training fraction, and
psi_c(x,y)=1[c(y)=c]/sqrt(p_c). Then E[psi_c psi_d]=1[c=d]. The input-field
moments use current sources E[r delta psi_c] and rho E[h psi_c], the ordinary
Legendre dilation, and the exact unit forward prefix/zero backward prefix.
The paired-moment reconstruction remains W0-2/(n tau) times the weighted sum
of backward/forward outer products. This is projection on the joint input-label
law; orthogonality and the product-tail identity have the same proof there.

At query time the predictor uses only x, the moving first weights/readout,
and this reconstructed hidden matrix. No query label or class is needed.
The labels organize TRAINING writes. Future changed class priors or stochastic
minibatches would require additional normalization analysis and are not tested.
The instantaneous update omits within-class forward/backward correlations;
there is no inherited descent, fitting or trajectory theorem. These caveats
are not removed by increasing temporal order.

Use the frozen Fashion/HAR binary labels for C2; housing training-target quartiles
for C4. The matched candidate has q12 or q6, respectively, and correction rank
bound24. The second candidate has q1 and smaller state. Both share the canonical
two tanh hidden layers, width256, zero readout, initial Gaussian laws, outer
mobilities256, step1/64, and T128. Rank24 factors use prior pilot-selected
mobilities. Four fresh seeds4501–4504 supply confirmation; only validation
chooses checkpoints16,32,64,128. Targets used for bins are training targets only.

## All confirmation outcomes

Median validation-selected test RMSE over four fresh seeds:

| Learner | Fashion | HAR | Housing |
|---|---:|---:|---:|
| Population q1 |0.681572|0.057427|0.316459|
| Population, rank bound24 |0.681839|0.057991|0.316495|
| Tuned rank24 factors |0.677056|0.047361|0.320119|

The primary matched population/factor median PAIRED ratios are1.00571,
1.20431,0.99726; seed wins are0/4,0/4,3/4. None reaches5% improvement.
The ratio of separate medians in the table is not the primary paired statistic.
The registered cross-domain gate therefore fails. The q1 candidate gives
similar results and usually slightly improves upon the higher-order candidate,
but is not a state-matched superiority claim. Higher temporal resolution does
not fix omitted within-population interactions or guarantee better task loss.

All42fits complete with finite states. Six half-step checks change selected
test RMSE by at most9.69e-6; every selected time is unchanged. Captured/eager
four-step parity is exactly zero for all three learner classes, and every
empirical address Gram passes the1e-5 tolerance. The grouping/prefix source
uses the already checked InputFieldFlow implementation, with complete frozen
source snapshots. The [independent review](STAGE2_LABEL_INDEX_INDEPENDENT_REVIEW.md)
then passed202CPU assertions, rebuilt the data bitwise from raw sources,
verified all42 records/168 checkpoint choices and test scores, and reproduced
one Housing trajectory bitwise. It records the limits of retrospective hashes
and the absence of saved train/validation prediction vectors for the other fits.

The42instrumented fits total91.872seconds, excluding interpreter startup.
The dictionary needs no initialized first-layer copy; training caches its
M-by-C indicator values and class probabilities/thresholds. Fixed Gaussian
mixing and evolving outer weights remain. No optimized memory/speed advantage
is established by these state counts. Class grouping and supervised prototypes
are existing ideas; no novelty is claimed merely for naming labels as addresses.

## Decision and evidence

This final candidate helps rule out a simple rescue of the earlier PCA result:
putting labels into the addresses, and matching the temporal-state rank budget,
does not produce the desired cross-domain advantage in these experiments.
It does not rule out all supervised dictionaries or nonlinear memory systems.
No additional bins, rates, architectures or datasets were searched after failure.

Source/protocol: stage2_label_index.py and STAGE2_LABEL_INDEX_PROTOCOL.md.
All raw arrays, source/config/environment snapshots, per-fit records and hashes
are in generated stage2_label_index01. Recomputable paired summaries are produced
by stage2_label_index_analyze.py in stage2_label_index_analysis01. The parent
contract's pre-execution amendment charged these42fits to its root reserve;
earlier route failures remain unchanged. Nothing was promoted or added to paper.
