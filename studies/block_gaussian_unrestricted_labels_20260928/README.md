# Can block Gaussian response memory remove the small-label restriction?

28 September 2026. This new study addresses the changed label regime rather
than importing unpromoted results from the initialization study or earlier
width studies. The scientific target is nonlinear multi-input training with
arbitrary fixed finite label RMS, zero initial readout, fixed depth, smooth
bounded activations (tanh first), and aligned Gaussian initialized blocks.
All learned hidden updates remain globally connected.

## Contract

The primary approximation is the autonomous old-clock Legendre response
closure. Width n=Bk is the number of blocks times block size. The clock has
speed residual RMS; each trained hidden layer retains q forward and q
residual-weighted backward moments per training sample. The initial Gaussian
blocks are kept exactly. The target observable is L2 of a test-input law of
the time-supremum prediction discrepancy. Compact-time, all-time, fixed-block
population, and canonical fully dense population claims must remain distinct.

The authorized work is theoretical exploration, including bounded parallel
proof attempts and ordinary algebra verification. No training campaign,
manuscript change, commit or promotion is planned. Scientific inputs are
self-contained derivations in this study and the maintained docs/ and code/;
no other study is a proof dependency.

## Routes and ownership

Parent: exact moment energy, reachable-state dynamics and loss/stability
obligations; overall synthesis and README.
Scoped fresh author 1: direct block-particle formulation and finite-time
width comparison, in DIRECT_BLOCK_ROUTE.md.
Scoped fresh author 2: nonlinear unrestricted-label fitting/stability route
and genuine obstructions, in FITTING_AND_STABILITY.md.

Each agent initially received the model and a neutral bounded assignment.
The coordinator subsequently supplied calculation hints and checks, including
the scalar compact-clock transfer and joint block-growth localization. These
are collaborative author routes, not independent promotion reviews.

## Results and current status

**ARBITRARY_LABEL_STATE_BOUNDS.md:** for bounded smooth activations and
arbitrary finite labels, the actual unmodified moment closure exists at all
finite physical times. Its readout, clock, backward-response RMS, moment
energies and learned-matrix Frobenius norms have bounds on [0,T] independent
of n,k,q at fixed confidence under Gaussian initialization. The argument uses
finite empirical Gaussian-block moments rather than the maximum block norm.
These are state bounds; they are not width-error or loss-decay estimates.

**DIRECT_BLOCK_ROUTE.md:** the aligned architecture is exactly a system of
finite-dimensional blocks coupled by O(L m^2 q) empirical scalar contractions.
For bounded initial block norms, a complete finite-time sampling argument
gives expected time-supremum squared prediction error C/B for arbitrary
finite labels, including integrated passive tests on bounded input sets. The
constant is independent of B, but depends on k and q. The Hadamard-product
carrier estimate requires a sqrt(k) factor; retaining it gives a stability
constant with growth bounded by a polynomial times exp(C sqrt(k)) at fixed
q and other parameters. Thus k=A log B permits an explicit vanishing-error
comparison of the unmodified Gaussian finite system with a conditioned
block-population family. This does not identify that family with canonical
dense population flow, or construct the unconditioned fixed-k law limit.

**FITTING_AND_STABILITY.md:** for one input and zero readout, canonical
fully trainable dense gradient flow fits every finite label, with residual
at most |y| exp(-2 kappa_0 t) and total residual activity at most
|y|/(2 kappa_0), where kappa_0 is initial readout-feature energy. Its total
parameter path length in the canonical mobility metric is at most
|y|/sqrt(kappa_0). A normalized-margin identity proves these statements;
no frozen-feature or small-motion approximation is used. For the actual
Gaussian-block law and a fixed nonzero input, kappa_0 has a positive
high-probability lower bound independent of k and B, at fixed depth.
The parent additionally derived Var(kappa_0)<=L/(4n), so its fixed positive
lower bound holds with failure probability at most C_L/n for every block
size, including the fully iid dense case k=n.

The same note proves a scalar-clock comparison principle: if a closure
approximates dense training and test observables on the finite response
interval [0,2|y|/kappa_0], then it approximates them at matching physical
times for all time. Clock error is at most training source error divided
by kappa_0; test errors transfer through the dense observable's modulus
in response time. Width-uniform source and modulus estimates are still
required. A separate exact closure-defect identity and a sufficient
accumulated-defect fitting criterion are also recorded.

## Remaining obligations

The unrestricted-label, multiple-input, all-time approximation theorem is
open. Residual-direction rotation produces an explicit extra term in the
normalized-margin calculation. The closure also has an indefinite-sign
loss defect, so dense gradient-flow dissipation cannot simply be assigned
to it. Finally, convergence of the block population as k increases to the
canonical dense model is distinct from particle sampling at fixed k,q.

Finite blocks retain reuse of their fixed Gaussian matrices. The learned
part acts through finite empirical contractions, but this is not independence
of trained neurons or fresh Gaussian noise. No impossibility theorem for
unrestricted labels is claimed, and no generic counterexample substitutes
for the specified Gaussian tanh model.

## Checks and next step

The parent read the complete author derivations, checked canonical residual
signs and mobility normalizations, the moment-energy and defect identities,
the scalar margin and clock comparison, and the Gaussian net-tail argument.
The direct-route backward sensitivity was corrected to retain its necessary
sqrt(k) factor before synthesis. These are internal study results, not book
promotion or a completed independent review. No experiments were run and
no paper or Git history was changed.

Checked source versions (SHA-256, 28 September 2026; parent algebraic proof
read-through and elementary consistency checks):

- ARBITRARY_LABEL_STATE_BOUNDS.md:
  7ded612c3d7cbc810faf91cdeaeac1061146a648be81b2e1d66d81d3dc9083aa
- DIRECT_BLOCK_ROUTE.md:
  d739cd82254a19113e4077cf155af243778de6bb481aa79f602aaa38dfe47e30
- FITTING_AND_STABILITY.md:
  5dac064f187946b465896682d16b7338a68112237027491a767b05fd14754492

The most useful next proof target is compact-response-time approximation
with width-uniform test regularity in the scalar case, where the time-uniform
transfer is now explicit. For the requested multiple-input result, the
decisive fitting obligation is residual-direction or Gram control along
substantial feature motion; block locality alone does not supply it.
