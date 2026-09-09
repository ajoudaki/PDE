# Exact research contract

The user asks for a general-depth extension of the three-input global joint limit, now using exactly
\[
\phi_\theta(z)=(1-\theta)z+\theta\arctan z,
\qquad 0<\theta\le1,
\]
with no offset, gain change, variance normalization, residual architecture, frozen hidden layer, or optimizer substitution. There are still three fixed normalized inputs; their pairwise cosines lie strictly in \((-1+\delta,1-\delta)\). Labels remain in \(\{-1,1\}\). Depth \(L\) denotes the number of hidden layers.

Retain the Gaussian initialization, raw Hilbert metric, full raw gradient flow, simultaneous raw gradient descent with width-dependent step \(n^{-2}\), and all specified prediction/kernel/path/velocity joint limits. Width tends to infinity at each separately fixed depth and compact physical horizon. Global population existence, the stated uniqueness and restartability, and all-time nonaffinity are distinct from infinite-time convergence of finite networks. No joint depth-width limit is requested or substituted.

The desired conclusion is a sufficient positive threshold \(\theta_*(\delta,L)\), uniform over admissible geometries, dimensions and labels, preferably a positive \(\theta_*(\delta)\) that works for every separately fixed depth. Constants of the resulting theorem may depend on depth unless additional uniformity is actually proved. Sharpness of an initialization eigenvalue bound is not sharpness of a sufficient training threshold.

The earlier completed three-input shifted/gain-activation theorem concerns a different activation. The exact odd-mixture global three-input theorem must be established independently; it is not an already proved base case to which depth induction may be applied.

Authorized work: theoretical analysis, local proof artifacts, read-only primary-source retrieval where relevant, independent adversarial agents. No numerical experiments, publication, messages to others, original-task resumption or Git commit.

Current claim levels: complete sharp arbitrary-depth Gaussian-initialization estimates are being audited. The global trained three-input theorem and any sufficient coefficient threshold remain unresolved. A conditional continuation criterion must display its additional hypotheses and cannot be promoted to the requested unconditional result.
