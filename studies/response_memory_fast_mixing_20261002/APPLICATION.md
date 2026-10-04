# What this study could add to the paper

This is a study-owned interpretation, not manuscript text or a promoted claim.
The empirical result is internally checked. The exact tanh theorem's assembly
passed its separate internal audit; see TANH_TRANSFER.md and
TANH_TRANSFER_REVIEW.md for the precise scope and external theorem inputs.

The response-memory closure retains feature learning with a fixed number of
history coordinates, but its dense initialized mixer still costs quadratic
storage and matrix-action time in the hidden width. That is a real obstacle
to using it as a large population learner. This study changes the distribution
of that fixed environment: fast orthogonal transforms with a carefully chosen
singular spectrum replace the stored Gaussian matrix. The autonomous memory
equations and their moving representations are retained.

The reason to choose the spectrum carefully comes from learning itself.
Forward activity is sent through the matrix, while credit returns through its
transpose. Matching forward random features alone therefore leaves out a
repeated interaction that determines subsequent feature motion. The exact
Gaussian-probe identity exposes a fourth-spectral-moment dependence; the
trained right-basis control shows that even preserving that scalar diagnostic
and the entire singular spectrum does not suffice for arbitrary coordinate
mixing. This supplies a concrete design criterion, rather than treating every
fast random transform as interchangeable.

The theorem has an appropriately different target from approximation
of a particular dense matrix: the two initializations have the same limiting
predictions and empirical feature statistics at any fixed finite collection
of numerical training steps, as width grows. It handles the actual tanh
nonlinearity, zero initial readout, evolving memories, residual feedback and
clock. The proof combines published structured-matrix universality with a
finite-program reduction and a sparse-row clipping argument for adaptive
credit. The transform and the underlying universality theorems are prior art;
their verified application to this autonomous learner is the proposed addition.

For fixed training count m and input dimension d, the resulting q=1 step costs
O(mn log n + m^2 n + mnd), stores O(n) fixed mixer entries, and retains
n(d+1+2m)+1 moving scalars. Thus it is possible to simulate this particular
large nonlinear population without ever storing an n-by-n matrix. The moving
memory count does not grow with the number of completed training steps. Sample
dependence remains, and the theorem does not permit that step count to grow
with width or exchange width with an ODE limit.

The demonstrated use case is wide-population learning simulation, not a new
state-of-the-art image classifier. On the one fixed digits3/8 task, the width
16,384 implementation is 5.22 times faster and uses 5.40 times less peak CUDA
memory than the same-width Gaussian implementation. A much narrower Gaussian
learner is faster still and has the same classification error. Meaningful
claims about general-purpose architecture quality would require competitive
fast-layer/factor baselines and larger tasks; they are not established here.

The restrained paper motivation would therefore be: response-memory dynamics
can support an efficient population-learning architecture, and understanding
the reuse of the fixed environment gives a principled way to build it. The
current evidence supports that specific use case. It does not establish a
transformer replacement, optimal training algorithm, generalization benefit,
or priority for spectral universality.
