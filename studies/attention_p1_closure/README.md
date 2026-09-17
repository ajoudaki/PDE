# First-order closure for learned attention pooling

Opened 2026-09-16 for the user's request to derive a p=1 dictionary/particle
description of the proposed attention-pooling model, including its treatment
of both wide layers. This is a new architectural investigation.

The model has a fixed number of tokens u_j=x_j/sqrt(d), finite learned query
and key matrices Q,K, attention a_j=softmax_j((Q u_query)^T K u_j/sqrt(d_q)),
first hidden fields tanh(W1 u_j), second hidden field
tanh(W2 sum_j a_j tanh(W1 u_j)), and output c^T h2/n. All blocks train under
unhalved squared loss. The wide blocks use the canonical initialization and
mobilities (n,1,n); Q,K have fixed dimension and unit mobilities. Exact
finite identities, a defined finite closure, and approximation/convergence
claims must remain separate. No layer normalization, additional transformer
blocks, or alternative attention scaling is introduced.

Scientific inputs are this study's own derivations and the established docs/
and code/. No other study or unpromoted result is a research input. The task
authorizes mathematical derivation and meaningful bounded algebraic/numerical
verification, not a training campaign or promotion. Sources and reports stay
flat here; generated checks go in data/generated/attention_p1_closure/.

Root owns this README, the integrated derivation and verification assembly.
Scoped contributors receive explicit independent input and output assignments.
The current status is preparation; no new approximation theorem is claimed.

Initial metadata: HEAD 04b61a12795734cbfc93830bf0a164bab7d101c4, empty Git
index. Pre-existing tracked changes in shared instructions, .gitignore and
book-exporter files are preserved. No Git transaction is requested.
