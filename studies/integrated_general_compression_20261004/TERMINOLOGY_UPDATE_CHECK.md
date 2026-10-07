# Method names: terminology-only equivalence check

Date: 2026-10-06. Scope: the user-requested names **Legendre compression**
and **Harmonic compression** in the integrated study's current RESULT and
README. This is editorial maintenance, not a new theorem or proof audit.

## Outcome and version binding

Author check: PASS. After the enumerated naming/markup normalization,
both complete documents are byte-for-byte identical to their versions
in commit `7ee13decc7ff43d289ec64c0b2463906afbb3090`.
Only the explicitly marked naming/provenance paragraphs are excluded
from that comparison; those paragraphs were read separately.

| Document | Audited predecessor SHA-256 | Renamed SHA-256 |
|---|---|---|
| RESULT.md | `e24e2f519bd597159f1745ce46e9f9ad27c8772e9ef80807907b63557401c562` | `9c4bc51b9e78489cc9ce910024993994759fefd6652e4f2a16789e5640c32f2d` |
| README.md | `a1297389cdb229b0c96678831502c3083c33f10055dcccbc6fdecce52823cf17` | `fb1467325ff65a3f4454b3764cff037a969b256e76d0fc645fa773aea65b1d23` |

The shared normalized RESULT hash is
`8c7c4a24c1cf4fe5ac33f78d3bdba4cb360ebebaff0fbbafb7cd8317ccbd8f7c`.
The shared normalized README hash is
`1ef1f8c6b913ad988a7817ea56d62bedf1f1bbb005a6293fb9fc0c5195d30b1d`.

## Exact change scope

- Active method prose, headings, tables, equation labels and their references
  now use Harmonic in place of Compact/compact. Two resulting redundant
  labels are shortened to “Harmonic projector bounds” and “Harmonic decay.”
  Legendre compression
  remains the first method's name.
- The two public predictor labels formerly using `\mathrm{compact}` now
  use `\mathrm{Harm}`, parallel to the unchanged Legendre label.
- All proof-local `C`/`c` subscripts and coefficient definitions remain
  unchanged. A short explanatory note maps the existing compressed-model
  subscript to Harmonic compression.
- Eighteen current fragment identifiers use `harmonic-*`; all eighteen
  original `compact-*` identifiers remain as aliases. The expansion-proof
  fragment is `harmonic-expansion-proof`. Every previous explicit
  document anchor still resolves.
- The ordinary mathematical uses “compact witness,” “on compact” and
  “Compactness” remain unchanged. The former method name occurs visibly
  only in the explicit historical-name explanation.
- Historical source filenames and the four original internal audit reports
  are untouched. Their input/final hashes continue to identify the original
  reviewed bytes; this record supplies the editorial bridge to the renamed
  document without pretending those reviews inspected later bytes.
- No setup, coefficient, bound, assumption, construction, storage count,
  mathematical dependency or proof argument changed. No other study,
  maintained book, paper or Git index was edited.

## Checks

- Whole-text equivalence under the explicit normalization below: PASS
  for both documents.
- Current RESULT: 67 unique explicit anchors, including all 49 original
  anchors and 18 new ones; all fragment links resolve.
- Equation tags: 172, all unique; display delimiters: 480 opening and
  480 closing; inline delimiters: 2109 opening and 2109 closing.
- Original ordinary uses of compact/compactness: preserved separately,
  so the broad name normalization cannot hide an incorrect replacement.
- Historical audit files compared against the predecessor commit: no diff.
- Scoped `git diff --check`: PASS.

The name/provenance paragraphs delimited by `method-names` comments are
the only added prose. Removing explicit anchors for the equivalence check
is accompanied by the separate anchor preservation/uniqueness/link check.
Blank-line normalization only removes surplus empty lines around those
editorial additions. No algebraic simplification is performed.

## Reproduction

Run this read-only check from the repository root with Bash and Node.
Git supplies each predecessor through a pipe; Node does not spawn a
child process or write a file.

```bash
pde_naming_base=7ee13decc7ff43d289ec64c0b2463906afbb3090
pde_naming_dir=studies/integrated_general_compression_20261004
for pde_naming_file in RESULT.md README.md; do
  node - "$pde_naming_file" 3< <(git show "$pde_naming_base:$pde_naming_dir/$pde_naming_file") <<'JS'
const fs=require('fs'),crypto=require('crypto');
const name=process.argv[2],dir='studies/integrated_general_compression_20261004/';
const before=fs.readFileSync(3,'utf8'),after=fs.readFileSync(dir+name,'utf8');
const hash=s=>crypto.createHash('sha256').update(s).digest('hex');
function canonical(s){
 return s.replace(/<!-- method-names:start -->[\s\S]*?<!-- method-names:end -->\n/g,'')
  .replace(/^<a id="[^"]+"><\/a>\n/gm,'')
  .replaceAll('#compact-harmonic-proof','#harmonic-expansion-proof')
  .replaceAll('#compact-','#harmonic-')
  .replaceAll('\\mathrm{compact}','\\mathrm{Harm}')
  .replaceAll('corollary-exact-compact-storage','corollary-exact-harmonic-storage')
  .replace(/\b[Cc]ompact\b/g,'Harmonic')
  .replaceAll('Harmonic harmonic projector bounds','Harmonic projector bounds')
  .replaceAll('Harmonic harmonic decay','Harmonic decay')
  .replace(/\n{3,}/g,'\n\n').trimEnd()+'\n';
}
if(canonical(before)!==canonical(after))throw new Error('Unexpected edit: '+name);
const out={name,beforeSha256:hash(before),afterSha256:hash(after),normalizedSha256:hash(canonical(after)),equivalent:true};
if(name==='RESULT.md'){
 const oldIds=[...before.matchAll(/<a id="([^"]+)">/g)].map(x=>x[1]);
 const ids=[...after.matchAll(/<a id="([^"]+)">/g)].map(x=>x[1]);
 const tags=[...after.matchAll(/\\tag\{([^}]+)\}/g)].map(x=>x[1]);
 const links=[...after.matchAll(/\]\(#([^)]+)\)/g)].map(x=>x[1]);
 out.structure={anchors:ids.length,newAnchors:ids.length-oldIds.length,preservedOldAnchors:oldIds.every(x=>ids.includes(x)),uniqueAnchors:new Set(ids).size===ids.length,tags:tags.length,uniqueTags:new Set(tags).size===tags.length,unresolvedFragments:links.filter(x=>!ids.includes(x)),display:[after.split('\\[').length-1,after.split('\\]').length-1],inline:[after.split('\\(').length-1,after.split('\\)').length-1],remainingCompactProse:after.split('\n').filter(x=>/\b[Cc]ompact\b/.test(x)&&!/^<a id=/.test(x))};
 for(const fragment of ['in the compact witness','on compact\n','Compactness']){
  if(after.split(fragment).length!==before.split(fragment).length)throw new Error('Changed ordinary compact use: '+fragment);
 }
}
console.log(JSON.stringify(out));
JS
done
```

Also compare the four original INTEGRATED_*_AUDIT.md files against the
same predecessor commit and run scoped `git diff --check`.

## Claim boundary

This check carries the earlier audit record across a terminology-only
revision; it is not an additional independent mathematical audit and
does not change any prior qualification or promotion status.
Historical supporting notes are intentionally not rewritten.
No full Markdown/TeX render or numerical experiment was run.
The separate editorial verification below is complete.

## Separate editorial verification

Reviewer: scoped subagent `audit_method_rename`, 2026-10-06. Verdict:
PASS for the terminology-only revision at the exact renamed hashes in
the version table above. No scientific content change was found.

The allowed inputs were RESULT.md, README.md, their versions at
`7ee13decc7ff43d289ec64c0b2463906afbb3090`, this check record, and the
four original audit reports for byte preservation and hash provenance
only. The reviewer inspected every changed line and all added marked
paragraphs; this was not a rereading or re-proving of the full theorem.
No other study or maintained scientific source was read.

The reviewer independently ran the whole-document normalization using
Node with predecessor text supplied by outer-shell `git show` through
file descriptors. Both comparisons passed and reproduced both normalized
hashes above. A separate comparison extracted the mathematical blocks,
removed equation tags, and applied only the public predictor-label mapping:
all 480 existing display blocks and 2,108 existing inline expressions in
RESULT, and all 10 inline expressions in README, matched byte-for-byte
in their original order. The additional inline expression in RESULT is
the explanatory subscript in the marked naming paragraph. This confirms
preservation of proof-local coefficient notation independently of the
broader prose-name normalization.

All 49 original RESULT anchors remain unique and in place. Each of the
18 old `compact-*` anchors is immediately adjacent to its corresponding
new `harmonic-*` alias. All 37 local links in RESULT and 6 in README
resolve; these checks removed math blocks before extracting Markdown
links. All 172 equation tags remain unique. The ordinary compact-set
wording is unchanged, and the remaining old method-name occurrences are
the declared historical explanations and preserved identifiers.

An explicit `git diff --exit-code` against the predecessor commit for
the four named audit reports returned zero with no output. Their final
binding records still name the predecessor RESULT hash
`e24e2f519bd597159f1745ce46e9f9ad27c8772e9ef80807907b63557401c562`;
none claims to have audited the renamed bytes. Scoped `git diff --check`
also passed. The new naming/provenance paragraphs accurately describe
that distinction and the unchanged mathematical status.

The required canonical-notation skill path was inaccessible with
permission denied, as already disclosed in the study. This editorial
verification introduced no mathematical interpretation and did not
repeat or extend the earlier proof audits. No rendering, training
experiment, Git-index write or commit was performed. The reviewer's
only file edit was this completion record.
