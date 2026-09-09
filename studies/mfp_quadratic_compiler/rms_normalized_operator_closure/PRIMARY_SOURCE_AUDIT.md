# Primary-source audit of candidate limit machinery

This is a route audit, not imported proof of the present theorem.

## Tensor-program limits

Yang and Hu, *Feature Learning in Infinite-Width Neural Networks*,
<https://arxiv.org/abs/2011.14522>, proves broad discrete-time muP
feature-learning limits using tensor programs.  Two statements in that paper
are especially relevant here:

1. its width limit keeps gradient descent discrete in time, and it explicitly
   notes that a subsequent continuous-time limit creates separate existence,
   uniqueness, and well-posedness obligations;
2. it distinguishes the usual `N(0,1/n)` middle Gaussian matrix from an
   ordinary mean-field integral kernel and warns that correlations between
   the matrix and its transpose must be retained.

Therefore this machinery supports fixed finite training programs and the
non-lazy classification, but it does not supply the autonomous compact-time
IDE or the two missing analytic gates in `HOSTILE_AUDIT.md`.

## Traffic and diagonal-operator limits

Male, *Traffic Distributions and Independence*,
<https://arxiv.org/abs/1111.4662>, constructs traffic probability precisely
to retain graph operations beyond ordinary noncommutative distributions.
Au--Cebron--Dahlqvist--Gabriel--Male, *Large permutation invariant random
matrices are asymptotically free over the diagonal*,
<https://arxiv.org/abs/1805.07045>, closes algebras under diagonal projection
and proves fixed-graph/fixed-polynomial asymptotics under explicit boundedness
or graph-sum hypotheses.

These sources confirm that a Gaussian matrix together with coordinatewise
diagonal operations naturally asks for a richer object than a circular
operator or an ordinary integral kernel.  But the full traffic distribution
is the collection of all graph-operation evaluations.  Using it as the
evolving state without a smaller finite-generator topology and a positive-time
identification theorem would be exactly the hierarchy repackaging forbidden
by the present contract.  The cited fixed-polynomial theorems also do not
propagate the unbounded adaptive marks in this normalized gradient flow.

## Consequence for this study

The primary literature validates the two candidate languages and also the
precise gap between them and the requested result.  It neither proves a
positive closure nor a universal impossibility theorem for this model.
