# Numbered mathematics: bounded extension from packet 005

Preservation and full-review rules are unchanged. Packet005 covers frozen
global_nonlinear.md:1–504; packet006 covers505–999. Prepare independently,
accept sequentially. No scientific reproof or reorganization.

- Every tagged display gets its canonical `eq` target spanning the entire
  original `\[` through `\]` block. Delete only its literal `\tag{number}`
  (`equation-tag` edit, target required), preserving surrounding whitespace.
  If that tag is the only non-whitespace content on its source line, replace
  it with `%` instead: a TeX comment keeps Pandoc from treating the resulting
  empty line as a paragraph boundary. This marker changes no mathematical token.
  Insert ` {#eq-ID}` immediately after its closing delimiter (`equation-label`,
  target required). Delimiter conversion remains a separate edit. Untagged,
  unreferenced displays remain unnumbered. Mathematical payloads must match
  exactly after these validated tag edits. No alignment/linebreak edits.
- The bold named theorem marker becomes a native Quarto theorem div:
  `::: {#thm-ID}`, followed by `## original title` and a blank line, replacing
  exactly `**Theorem (original title).** ` (`statement-open`, target required).
  The generated title is environment metadata, not a new structural section.
  Insert `\n\n:::` at the end of the final statement line, before its existing
  newline (`statement-close`, same target). The canonical span begins at the
  original marker and ends at the last statement line. Exclude the subsequent
  proof-architecture commentary. Do not invent a contiguous proof environment
  when a theorem's proof is distributed across later sections.
- Convert numeric equation references, including their parentheses, to native
  `@eq-ID`. Immediately preceding Equation(s)/Formula(s) may be consumed as the
  reference noun, as with Section(s). Preserve descriptive qualifiers and all
  range endpoints/subparts. Reference edits may add a single separating space
  beside original ASCII `--` range punctuation to prevent its being absorbed
  into the native ID. Preserve that punctuation and the full range.
- A composite section locator such as `Section 2(a)` converts its section-number
  prefix and preserves `(a)` verbatim after the native reference. This is a
  section link with an explicit retained locator, as with section references
  qualified by part D; it does not assert a separately labelled item. Do not
  leave the section number raw merely because the item has no native anchor.
- Audit every internal link, numbered reference and explicit named destination.
  Resolve targets from the frozen source; reservations into unmigrated portions
  remain binding. Bare mathematical decimals are not references. Future equation
  targets must point to the complete tagged display, not a nearby section.

Checker extensions must verify typed source intervals, paired tag/label edits,
balanced theorem wrappers and exact boundary placement, math/prose preservation,
and rejection of illegal edits. Rendering is native Quarto, with the already
validated print setup. No new publisher or broad capability campaign.

The PDF class enables its native `enabledeprecatedfontcommands` compatibility
option for existing commands such as `\rm`. Preserve the source notation rather
than rewriting it for the renderer.

006 may initially fail only prefix continuity until actual005 acceptance. After
acceptance, rebase its before-state and remove identical duplicate proposals;
never silently rename labels or change candidate text to hide a conflict.
