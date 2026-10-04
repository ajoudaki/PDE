# Final architectural candidate: supervised population addresses

Chosen after the PCA-indexed and gating outcomes; all choices below are fixed
before any fit of this candidate. Existing comparisons remain negative evidence.
This is a different explicit address choice within the reopened indexing lead,
not a new scientific source or an imported unpromoted study.

Define an empirical joint law of training pairs(x,y). Classifications use C=2
groups(y=-1,y=+1). Housing uses C=4groups separated by the25th,50th,75th percentiles
of its1024training targets. Ties go to the upper bin. Let p_c be each group's
training fraction, and set psi_c(x,y)=1[group(y)=c]/sqrt(p_c). Empty groups fail
the domain. These functions are exactly orthonormal under the empirical joint
law. The original input-field moment equations and reconstruction apply with
these coefficients; every source uses the known current TRAINING label.
The network's query prediction uses only its reconstructed matrix and query x,
never the query's unknown label. A stochastic/new-data law or changing class
prior would require separate normalization and is not silently assumed here.

The product-tail identity is the orthogonal-projection identity on the joint
input-label probability space. It supplies no fitting/descent/tracking theorem.
In particular the instantaneous update averages forward and backward fields
within label populations and can still omit relevant within-population
correlations. More temporal order cannot generally recover that spatial loss.
Class means, prototypes and supervised partitioning are established ideas;
no priority is claimed merely for using labels as indices.

Fixed stage2_data01; all1024training rows, width256, canonical two-hidden-layer
tanh/mobilities/zero-readout/prefix, T128, step1/64. Three learners:
(a) population q1; (b) population q=24/C (q12classification,q6housing), giving
rank bound24; (c) conventional rank24factors at the previously selected factor
mobilities(fashion.25,HAR4,housing4). No new factor search. Four fresh seeds
4501–4504, all three domains and all three learners=36fits. Repeat learner(b)
and factors at seed4501, all domains, at half step1/128=6fits. Terminal42fits;
no extra dictionary/bin/order/rate/curriculum variants after outcomes.

Select checkpoints16,32,64,128 using validation RMSE only. Test data never choose
addresses, quantiles, seed, model or checkpoint. Primary positive gate is the
matched-rank population learner improving median PAIRED test RMSE over factors
by>=5% on at least two domains, with>=3/4wins there and<=5% median worsening on
the remaining domain. Failure remains failure, irrespective of cheap q1 success.
q1 is a secondary mechanism comparison and has fewer moving coordinates; do not
pretend it is parameter matched. A smaller moving state alone is not an advantage.

Validity gates: exact empirical basis Gram error<1e-5float32, source loss-gradient
and moment-normalization checks from existing independently checked InputFieldFlow,
captured/eager checks<2e-5, finite states, TF32off, one CPU thread. Refinement
requires selected test RMSE change<1% of training label RMS and<one-third any
claimed paired advantage. Record every seed/checkpoint/prediction/hash and
dictionary group probabilities. Store true memory/base/basis costs; there is
no retained initialized-first-layer dictionary here. Time is instrumented wall
time, not a optimized-system speed claim. GPU0 only when independent replay
releases it;42fits charged to amended root reserve before execution.
