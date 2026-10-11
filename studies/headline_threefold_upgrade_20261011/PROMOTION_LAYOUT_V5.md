# Promotion v5 layout diagnosis

## Verdict

**One required formatting defect; no other required or optional defect found in the assigned new-material scope.**

The only required repair is the overlong inline parameter tuple on PDF page 924. The minimal meaning-preserving repair is to put the existing tuple in display math, without changing any symbols, punctuation, label, or surrounding prose. This is sufficient from this layout review: no second source change is required.

## Frozen input and coverage

- Candidate source/diff: `data/generated/headline_threefold_upgrade_20261011/promotion_v5/docs/08b-trajectory-compression.qmd` and `promotion_v5/chapter.diff`.
- Render inspected: `data/generated/headline_threefold_upgrade_20261011/promotion_v5/data/generated/DTDL/DTDL.pdf`, SHA-256 `c6e1a1b970e886ba69be088dc95b4f548c12f8dc833498b5245e677ea266b968`, 1810 pages.
- Opening/headline interface: PDF pages 873--878.
- New polynomial-width section: PDF pages 922--945, including Theorem 33, Lemma 29, Proposition 9, Proposition 10, and the Taylor assembly gates.
- New efficient-setup section: PDF pages 966--991, including Proposition 15, Lemmas 34--36, both source-space constructions, the Gaussian sampler, and both cost tables.
- Closing nonlinear-learning and headline-assembly interfaces: PDF pages 991--1001, including the changed assembly proof opening on page 1000.

I extracted word bounding boxes for the complete added ranges and the changed interfaces, then raster-inspected the section openings, formal-statement openings and endings, dense displayed-equation pages, both tables, the Gaussian-sampler interface, and the final assembly interface. The structural artifact reports no duplicate identifiers, missing cross-references, or nonheading section cross-references; the PDF build diagnostics contain no unresolved-reference or malformed-environment warning in scope.

## Required defect

### PDF page 924: inline parameter tuple crosses the right text margin

Source: v5 `docs/08b-trajectory-compression.qmd`, lines 3318--3321 (the tuple is on line 3320):

```markdown
All training sources and the responses
$R_{ba}^{(j)}=D_\Theta z_b^{(j)}\nabla_\Theta(nf_a)$, where
$\Theta=(W^{(1)},\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},W^{(L+1)})$,
are holomorphic near this rectangle.
```

Evidence: the page-924 bounding-box scan reaches `xMax = 601.554 pt` on a 612 pt page; ordinary body text in this layout ends near `x = 530 pt`. Thus the run remains inside the physical page boundary but substantially crosses the established right text margin. The overflowing run is the tail of the tuple, beginning with the final `nW^{(L)}` and continuing through `W^{(L+1)}` and the closing punctuation. The raster view confirms visible intrusion through the text margin rather than a harmless bounding-box anomaly.

Minimal patch:

```markdown
All training sources and the responses
$R_{ba}^{(j)}=D_\Theta z_b^{(j)}\nabla_\Theta(nf_a)$, where

$$
\Theta=(W^{(1)},\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},W^{(L+1)}),
$$

are holomorphic near this rectangle.
```

This changes only line breaking. It preserves the tuple, its order and scaling, the comma joining it to the sentence, and all mathematical meaning. No new equation label is needed.

## No further defects

- No other word box in the complete added ranges or interfaces crosses the physical page edge or the established text margin. The next-largest right extent in the scanned new pages was `xMax = 535.295 pt` on page 985 and is visibly within the text block.
- No displayed equation is clipped vertically or horizontally in the remaining added material.
- Proposition 15's four-row initializer table on page 967 and the asymptotic-order table on page 990 are complete, aligned, and legible; neither has a missing rule, truncated cell, or malformed row.
- All newly added theorem/lemma/proposition headings and proof boundaries inspected in the PDF are formed correctly. There are no detached headings, empty statements, or proof-end marks stranded by a malformed environment.
- The section transitions at pages 922--923, 944--945, 966--968, 990--992, and the headline assembly at page 1000 are coherent and unclipped.
- No broken label/link text, unresolved `??`, or malformed section reference was found in scope.

## Classification

- **Required:** page 924 display conversion above.
- **Optional:** none.
- **Out of scope:** unrelated pre-existing book layout outside the changed opening/headline/assembly interfaces and newly added width/setup material.
