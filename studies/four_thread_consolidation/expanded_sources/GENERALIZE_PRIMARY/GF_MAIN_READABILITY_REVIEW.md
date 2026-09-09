# Main exposition readability review

Reviewer: independent destination-task agent `gf_main_readability`.

Scope: read the three source notes in full; read all of `gf_exposition/main.tex`
and the text extracted from the complete ten-page `gf-main.pdf`; visually
inspected every rendered PDF page. The review checks source fidelity at the
exposition level, canonical notation, readability, and preservation of core
ideas. It is not an additional all-details certification of the original proof.

## Assessment of the first rendered draft

The main text meets the requested mid/high mathematical level. It retains the
mechanisms behind the proof, not merely a list of conclusions:

- the normalized rank-one update has operator size of order one;
- RMS/operator bounds provide a width-independent first-exit interval;
- matrix reuse creates response terms rather than independent new noise;
- one backward source pulse carries Delta omega_b;
- weighted time sums permit marginal tail bounds with no history maximum;
- depth constants are selected in opposite directions at zero time before
  reducing the time interval;
- cutoff contributions are added through the backward recursion, avoiding R^L;
- exponential-in-R stability is overcome by Gaussian cutoff tails;
- the finite coarse reference holds the number of Gaussian-program operations
  fixed during the width limit, permitting every vanishing eta_n.

Core equations use the canonical network fields and weights. Disposable
response-coefficient aliases and a hierarchy of norms have been moved out of
the main exposition. The finite/population distinction, same-matrix adjoint,
infinite scalar dimension, fixed-depth time dependence, and separate status
of strict feature activity are explicit.

Typography is clean on all ten inspected pages: no clipping, overlap or
equation splitting errors were found. The writing gives sufficient prose
between equations. The main technical page (6) is the densest but readable.

## Requested small revisions

1. Page 3: replace generic `b^top c/n -> E[bc]` by the concrete canonical
   feature-overlap example using h_a, h_b and H_a, H_b. This prevents the
   example index b from becoming an unrelated vector and avoids lowercase
   population fields.
2. Page 4: add `2 <= ell <= L` to the hidden-preactivation derivative formula.
3. Page 5: define the first appearance of tilde Z as a comparison state.
4. Page 2: change the theorem's broad opening about parameter trajectories
   having a limit to convergence in the stated observable sense. This avoids
   inviting an interpretation of matrix-to-operator norm convergence.
5. Page 6: add the elementary content of Jensen's inequality: the weights sum
   to one and the exponential of their average is at most the average of the
   exponentials. The dependence-free mechanism then becomes visible without
   expecting readers to supply it.
6. Layout: start the references on page 10 explicitly, giving nine exposition
   pages and one reference page instead of splitting the reference list.

## Final verdict: PASS

All six requested revisions were applied and checked in the source. I also
checked the updated PDF's extracted text and rendered page 6 after the prose
revision, then recompiled `gf-main.tex` to incorporate its new explicit
reference-page break. The resulting PDF has exactly ten pages: nine pages of
exposition and one complete reference page. The final compile has no overfull,
underfull, or warning messages. The references on page 10 contain all four
entries.

The revised main exposition satisfies the user's priorities: canonical and
minimal notation, readable mid/high-level arguments, and preservation of the
substantive mathematical mechanisms. No further readability or notation repair
is required. The detailed response recurrences, norm constructions, and
technical convergence passages are appropriately delegated to the appendix.
