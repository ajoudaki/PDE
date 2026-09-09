# Repository refactor: preservation and acceptance contract

Status: inventory; no scientific result is promoted by this plan.

## Scope

Preserve the current research before changing its organization. Recover unique,
relevant source artifacts from accessible temporary directories and the other
user's PDE checkout. Do not import raw assistant sessions, unrelated projects,
credentials, caches, or bulk numerical output into Git. Record omitted generated
artifacts by path, size and hash and retain their bytes outside the source tree.
Already committed data remain recoverable from existing Git history; this work
does not rewrite that history.

## Commit sequence

1. Non-data safety snapshot, including recovered source artifacts and provenance.
2. Mechanical layout change and data separation, with an exact move manifest.
3. Self-contained established documentation and code, with scoped promotion and
   independent review records; exploratory results remain explicitly exploratory.
4. Link, test, isolation, reproducibility and preservation fixes.

Each stage must have a usable rollback point. No existing research is deleted
before the safety snapshot. Excluded data are moved, not destroyed. No old
research task is resumed and no history is rewritten.

## Intended layout

- `docs/`: a short reading index, shared notation and a modest collection of
  substantive, complete chapters. The index distinguishes scientific aims from
  proved statements. It is not a second historical research ledger.
- `code/`: reusable, tested implementations and their tests and reproduction
  commands. No imports, file reads or proof dependencies from exploratory work.
- `studies/`: a flat set of named investigations, including historical source
  and audit collections. Ordinary internal code/test/source directories are
  permitted; nested scientific-program umbrellas are not the navigation model.
- `data/`: ignored generated artifacts and figures, physically separate from
  source. Established outputs have explicit deterministic reproduction commands.

Root README, ignore rules and small execution/configuration files are permitted;
the four scientific directories are not a demand to hide useful project entry
points in another hierarchy.

## Promotion gates

1. The exact model, initialization, optimizer, observables, horizons and limit
   order are stated, without substituting a stronger historical headline.
2. Every proof and nonclassical mathematical dependency is contained in the
   established library. No dangling probability, stability or generation lemma.
3. Every persistent symbol is defined consistently with the shared notation.
4. No established file refers to or depends on exploratory directories, old
   absolute checkout paths, temporary sources or conversation access.
5. Code has a documented interface, relevant correctness tests, explicit output
   locations and all necessary source dependencies in the established tree.
6. Independent isolated reviews inspect the actual promoted versions; source
   history and a PASS on an earlier report are not substitutes.
7. An isolated checkout containing only the established library and its small
   root configuration is sufficient to check the claims and run its tests.

Complete auxiliary theorems may have explicit structural hypotheses. They must
not be represented as the canonical global nonlinear limit if they do not prove
that result. Unclosed hypotheses or incomplete source imports prevent promotion.

## Safety and verification

Maintain source hashes, recovery records, data inventory and old-to-new paths in
this refactor study. Preserve immutable historical proof/review snapshots when
editing a navigational copy would invalidate their hashes. Audit generated links
and code paths after moving. Test the established subset without access to the
exploratory tree. Record test limits and any unpromoted results explicitly.
