#!/usr/bin/env node
/** Lossless scientific Markdown-to-LaTeX conversion for the working paper.
 * This is deliberately local and small: every supported source block is
 * accounted for, unsupported syntax fails, and no study file is input by TeX.
 * Run from the repository root with --check to compile an isolated wrapper.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { spawnSync } from 'node:child_process';

const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..');
const sourcePath = path.join(root, 'studies/integrated_general_compression_20261004/RESULT.md');
const outPath = path.join(root, 'paper/integrated_appendix.tex');
const scratchBase = path.join(root, 'data/generated/integrated_general_compression_20261004');
const source = fs.readFileSync(sourcePath, 'utf8');
const sourceHash = crypto.createHash('sha256').update(source).digest('hex');
const lines = source.split('\n');
const first = lines.findIndex(l => l.includes('<a id="headline-results">'));
const last = lines.findIndex(l => l.includes('<a id="integrated-audit">'));
if (first < 0 || last <= first) throw new Error('Scientific boundaries not found');
const selected = lines.slice(first, last).join('\n');
const tags = [...selected.matchAll(/\\tag\{([^{}]+)\}/g)].map(m => m[1]);
if (new Set(tags).size !== tags.length) throw new Error('Source equation tags are not unique');
const slug = s => s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
const tagLabel = new Map(tags.map((t, i) => [t, `int:eq-${String(i + 1).padStart(4, '0')}-${slug(t)}`]));
const shortTag = t => /^(?:[A-Za-z]+(?:-[A-Za-z])?\.[0-9]+[a-z]?|IC\.stop|WB\.cor|S\.[0-9]+(?:[a-z])?)$/.test(t);
const used = new Set(), omitted = [], anchors = new Set(), targets = new Set();
const mathInventory = [], tables = [], blocks = [], externalLinks = [], tagReferences = new Map();
const displayLayouts = [];
const modernizedMath = {fractions: 0, binomials: 0, removedBoxes: 0};
let inlineMathCount = 0, pendingAnchors = [], i = first;
const tex = [];
const texEscape = s => s.replace(/[\\{}%&#_$~^]/g, c => ({'\\':'\\textbackslash{}', '~':'\\textasciitilde{}', '^':'\\textasciicircum{}'}[c] || `\\${c}`))
  .replace(/–/g, '--').replace(/“/g, '``').replace(/”/g, "''");
const regexEscape = s => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

function modernMath(s) {
  // The working-paper style uses unboxed equations. Preserve the existing
  // argument group exactly, removing only the decorative boxing command.
  s = s.replace(/\\boxed(?=\s*\{)/g, () => { modernizedMath.removedBoxes++; return ''; });
  // Translate a brace-delimited TeX infix fraction/binomial exactly. Search
  // with a brace stack, since numerators themselves can have nested groups.
  for (;;) {
    const stack = []; let hit = null;
    for (let p = 0; p < s.length; p++) {
      if (s[p] === '\\' && /[\\{}]/.test(s[p + 1] || '')) { p++; continue; }
      if (s[p] === '{') stack.push(p);
      else if (s[p] === '}') stack.pop();
      else if (s[p] === '\\') {
        const m = s.slice(p).match(/^\\(over|choose)(?![A-Za-z])/);
        if (m) { hit = {start: stack.at(-1), p, endCommand: p + m[0].length, kind: m[1]}; break; }
      }
    }
    if (!hit) return s;
    if (hit.start === undefined) throw new Error('Undelimited TeX infix fraction');
    let depth = 1, end = hit.endCommand;
    for (; end < s.length; end++) {
      if (s[end] === '\\' && /[\\{}]/.test(s[end + 1] || '')) { end++; continue; }
      if (s[end] === '{') depth++;
      else if (s[end] === '}' && --depth === 0) break;
    }
    if (end === s.length) throw new Error('Unclosed infix fraction');
    const numerator = s.slice(hit.start + 1, hit.p).trim(), denominator = s.slice(hit.endCommand, end).trim();
    const command = hit.kind === 'over' ? 'frac' : 'binom';
    modernizedMath[hit.kind === 'over' ? 'fractions' : 'binomials']++;
    s = s.slice(0, hit.start) + `\\${command}{${numerator}}{${denominator}}` + s.slice(end + 1);
  }
}

function protectInline(s, table = false) {
  const saved = [];
  const save = v => { const id = saved.length; saved.push(v); return `ZZINTTOKEN${id}ZZ`; };
  let text = '', pos = 0;
  while (pos < s.length) {
    if (s.startsWith('\\(', pos)) {
      const end = s.indexOf('\\)', pos + 2);
      if (end < 0) throw new Error(`Unclosed inline math near ${s.slice(pos, pos + 80)}`);
      const body = modernMath(s.slice(pos + 2, end)).replace(/,/g, ',\\allowbreak '); inlineMathCount++;
      text += save(table ? `\\inttablemath{${body}}` : `\\(${body}\\)`); pos = end + 2;
    } else if (s[pos] === '$' && (pos === 0 || s[pos - 1] !== '\\')) {
      let end = pos + 1;
      while (end < s.length && (s[end] !== '$' || s[end - 1] === '\\')) end++;
      if (end === s.length) throw new Error(`Unclosed dollar math: ${s}`);
      const body = modernMath(s.slice(pos + 1, end)).replace(/,/g, ',\\allowbreak '); inlineMathCount++;
      text += save(table ? `\\inttablemath{${body}}` : `\\(${body}\\)`); pos = end + 1;
    } else if (s[pos] === '`') {
      const end = s.indexOf('`', pos + 1);
      if (end < 0) throw new Error(`Unclosed code span: ${s}`);
      text += save(`\\texttt{${texEscape(s.slice(pos + 1, end))}}`); pos = end + 1;
    } else { text += s[pos++]; }
  }
  return {text, saved, save};
}

function inline(s, table = false) {
  const p = protectInline(s, table);
  let text = p.text;
  // References are converted outside math only. The named short tags remain
  // visibly unchanged, whereas long descriptive tags become equation numbers.
  for (const t of [...tags].sort((a, b) => b.length - a.length)) {
    const re = new RegExp(`\\(${regexEscape(t)}\\)`, 'g');
    text = text.replace(re, () => {
      tagReferences.set(t, (tagReferences.get(t) || 0) + 1);
      return p.save(`\\eqref{${tagLabel.get(t)}}`);
    });
  }
  text = text.replace(/\[([^\]\n]*)\]\(([^)\n]*)\)/g, (_, label, url) => {
    const rendered = texEscape(label.replace(/Part III/g, 'the proof appendix').replace(/Part II/g, 'the detailed statements').replace(/Part I/g, 'the certificate interfaces'));
    if (url.startsWith('#')) {
      const id = `int:${url.slice(1)}`; targets.add(id);
      return p.save(`\\hyperref[${id}]{${rendered}}`);
    }
    if (!/^https?:\/\//.test(url)) throw new Error(`Noninternal scientific dependency: ${url}`);
    externalLinks.push({label, url});
    return p.save(`\\href{${url}}{${rendered}}`);
  });
  // Emphasis is shallow in the supplied source; handle it before escaping.
  text = text.replace(/\*\*([^*]+)\*\*/g, (_, x) => p.save(`\\textbf{${texEscape(x)}}`));
  text = text.replace(/(?<!\*)\*([^*]+)\*(?!\*)/g, (_, x) => p.save(`\\emph{${texEscape(x)}}`));
  text = texEscape(text);
  text = text.replace(/Euclidean\/Frobenius/g, 'Euclidean/\\allowbreak Frobenius');
  text = text.replace(/Part III/g, '\\hyperref[int:integrated-proofs]{the proof appendix}')
    .replace(/Part II/g, '\\hyperref[int:detailed-statements]{the detailed-statement appendix}')
    .replace(/Part I/g, '\\hyperref[int:headline-results]{the certificate-interface appendix}');
  // Nested tokens occur when a reference or math expression is a link label.
  let old;
  do { old = text; text = text.replace(/ZZINTTOKEN(\d+)ZZ/g, (_, n) => p.saved[Number(n)]); } while (text !== old);
  text = text.replace(/\}--(?=\\(?:hyperref|eqref))/g, '}--\\allowbreak ');
  if (/ZZINTTOKEN/.test(text)) throw new Error('Unrestored inline token');
  return text;
}

function emit(s, start, end, type) {
  for (let n = start; n <= end; n++) used.add(n);
  blocks.push({type, start: start + 1, end: end + 1});
  tex.push(`% SOURCE ${start + 1}--${end + 1}: ${type}\n${s}`);
}
function emitPending() {
  const out = pendingAnchors.map(id => `\\label{int:${id}}`).join('\n');
  pendingAnchors = []; return out;
}
function tableCells(line) {
  const cells = []; let buf = '', math = null;
  for (let n = 0; n < line.length; n++) {
    if (line.startsWith('\\(', n) && !math) { math = '\\)'; buf += '\\('; n++; continue; }
    if (math === '\\)' && line.startsWith('\\)', n)) { math = null; buf += '\\)'; n++; continue; }
    if (line[n] === '$' && line[n - 1] !== '\\') { math = math === '$' ? null : '$'; buf += '$'; continue; }
    if (line[n] === '|' && !math && line[n - 1] !== '\\') { cells.push(buf.trim()); buf = ''; }
    else buf += line[n];
  }
  cells.push(buf.trim());
  if (cells[0] === '') cells.shift();
  if (cells.at(-1) === '') cells.pop();
  return cells;
}
function nextStartsBlock(n) {
  const l = lines[n] || '';
  return /^\s*(?:#{2,6} |<a id=|<!--|\\\[|\$\$|\|)/.test(l)
    || /^\s*(?:[-*]|\d+\.)\s+/.test(l);
}

tex.push(`% Static scientific appendix. Generated from RESULT.md SHA256 ${sourceHash}.
% Rebuild: node studies/integrated_general_compression_20261004/paper_appendix_build.mjs --check
% Required packages: amsmath, amssymb, mathtools, mathrsfs, graphicx, array, booktabs, longtable, hyperref.
% No study file is read by LaTeX. Source line comments and build manifest audit coverage.
\\providecommand{\\inttablemath}[1]{\\begingroup
  \\setbox0=\\hbox{$\\textstyle #1$}%
  \\ifdim\\wd0>\\linewidth\\typeout{INTTABLE:\\the\\inputlineno:\\the\\wd0:\\the\\linewidth}\\fi
  \\ifdim\\wd0>\\linewidth\\resizebox{\\linewidth}{!}{\\box0}\\else\\box0\\fi
  \\endgroup}
\\providecommand{\\intdisplay}[1]{\\begingroup
  \\setbox0=\\hbox{$\\displaystyle #1$}%
  \\dimen0=\\dimexpr\\linewidth-5em\\relax
  \\ifdim\\wd0>\\dimen0\\typeout{INTDISPLAY:\\theHequation:\\the\\wd0:\\the\\dimen0}\\fi
  \\ifdim\\wd0>\\dimen0\\resizebox{\\dimen0}{!}{\\box0}\\else\\box0\\fi
  \\endgroup}
\\clearpage
`);

while (i < last) {
  const l = lines[i];
  if (!l.trim()) { used.add(i++); continue; }
  if (/^<!--/.test(l)) {
    const start = i;
    while (i < last && !lines[i].includes('-->')) i++;
    if (i >= last) throw new Error('Unclosed HTML comment');
    omitted.push({start: start + 1, end: i + 1, reason: 'HTML conversion/provenance comment'});
    i++; continue;
  }
  const anchor = l.match(/^\s*<a id="([^"]+)"><\/a>\s*$/);
  if (anchor) {
    if (anchors.has(`int:${anchor[1]}`)) throw new Error(`Duplicate anchor ${anchor[1]}`);
    anchors.add(`int:${anchor[1]}`); pendingAnchors.push(anchor[1]); used.add(i++); continue;
  }
  // The only historical paragraph within the scientific body is removed by
  // content boundaries, retaining its following scientific qualifications.
  if (l.startsWith("This section consolidates the current study's source bridge")) {
    const start = i;
    while (i < last && lines[i].trim()) i++;
    omitted.push({start: start + 1, end: i, reason: 'Historical source-read and skill-access provenance'});
    continue;
  }
  const heading = l.match(/^(#{2,6})\s+(.*)$/);
  if (heading) {
    let title = heading[2];
    if (title.startsWith('I. ')) title = 'Complete certificate interfaces and notation';
    else if (title.startsWith('II. ')) title = 'Detailed statements and computational costs';
    else if (title === 'III. Proofs') title = 'Complete proofs and constructions';
    else if (title === 'Read scope and claim boundary') title = 'Scope and claim boundary';
    else if (title === 'Interfaces and provenance') title = 'Finite interfaces';
    const level = heading[1].length;
    const cmd = level === 2 ? 'section' : level === 3 ? 'subsection' : level === 4 ? 'subsubsection' : 'paragraph';
    const anchorsHere = emitPending();
    emit(`\\${cmd}{${inline(title)}}\n${anchorsHere}${level >= 5 ? '\n\\mbox{}\\par\\smallskip' : ''}`, i, i, 'heading');
    if (heading[2].startsWith('I. ')) tex.push(`
The first-layer matrix denoted by \\(A\\) in the detailed formulas below is
exactly \\(W^{(1)}\\) in the main text. The hidden matrices
\\(W^{(2)},\\ldots,W^{(L)}\\), readout \\(w\\), physical time, and all
normalizations are unchanged. In particular, \\(h^{(0)}=x/\\sqrt d\\),
and the prediction is \\(w^\\top h^{(L)}/n\\). This correspondence avoids
changing proof-local notation or introducing a second model.
`);
    i++; continue;
  }
  if (l.trim() === '\\[' || l.trim() === '$$') {
    const start = i, closer = l.trim() === '\\[' ? '\\]' : '$$';
    i++; const raw = [];
    while (i < last && lines[i].trim() !== closer) raw.push(lines[i++]);
    if (i === last) throw new Error(`Unclosed display at ${start + 1}`);
    let body = raw.join('\n');
    const found = [...body.matchAll(/\\tag\{([^{}]+)\}/g)];
    if (found.length > 1) throw new Error(`Multiple tags at source ${start + 1}`);
    const tag = found[0]?.[1];
    if (tag) body = body.replace(/\\tag\{[^{}]+\}\s*/g, '');
    body = modernMath(body);
    if (tag === 'S.8' || tag === 'FC.7' || tag === 'VD.1' || body.trim().startsWith('c_t=\\frac{a}{64YSU}') || body.trim().startsWith('\\kappa_L(M)=1,')) {
      const parts = body.split(/\\q{1,2}uad\b/).map(s => s.trim());
      body = `\\begin{gathered}\n${parts.join('\\\\\n')}\n\\end{gathered}`;
      displayLayouts.push({sourceLine: start + 1, tag: tag || null, layout: 'Wrap a chain of separate definitions at its existing quad separators; all mathematical tokens preserved.'});
    }
    if (tag === 'Logarithmic complete costs') {
      const rows = body.replace(/\\begin\{array\}\{c\|c\|c\}/, '').replace(/\\end\{array\}/, '').replace(/\\hline/g, '').trim().split(/\\\\/).map(r => r.split('&').map(c => c.trim()));
      if (rows.length !== 4 || rows.some(r => r.length !== 3)) throw new Error('Changed complete-cost array layout');
      const entries = [];
      for (const row of rows.slice(1)) for (let c = 1; c <= 2; c++) {
        const formula = row[c].replace(/\n(?=\+)/g, '\\\\\n').replace(/\n(?=\\log\()/g, '\\\\\n{}\\times ');
        entries.push(`${rows[0][0]}:\\ ${row[0]}\\quad(${rows[0][c]})`, formula);
      }
      body = `\\begin{gathered}\n${entries.join('\\\\[3pt]\n')}\n\\end{gathered}`;
      displayLayouts.push({sourceLine: start + 1, tag, layout: 'Stack the phase/word-operation/peak-word array without dropping any entry; wrap one product with explicit multiplication and one sum.'});
    }
    body = body.replace(/\\begin\{split\}/g, '\\begin{aligned}').replace(/\\end\{split\}/g, '\\end{aligned}');
    const equationAnchors = emitPending();
    const declarations = tag ? `\\label{${tagLabel.get(tag)}}` : '';
    const env = tag ? 'equation' : 'equation*';
    const rendered = [equationAnchors ? `\\phantomsection\n${equationAnchors}` : '', `\\begingroup\\renewcommand{\\theHequation}{intdisplay.${mathInventory.length + 1}}`, `\\begin{${env}}`, `\\intdisplay{\n${body.trim()}\n}`, tag && shortTag(tag) ? `\\tag{${tag}}` : '', declarations, `\\end{${env}}`, '\\endgroup'].filter(Boolean).join('\n');
    emit(rendered, start, i, 'display');
    mathInventory.push({start: start + 1, end: i + 1, tag: tag || null, retainedNamedTag: !!tag && shortTag(tag), bodyHash: crypto.createHash('sha256').update(raw.join('\n')).digest('hex')});
    i++; continue;
  }
  if (l.startsWith('|')) {
    const start = i, raw = [];
    while (i < last && lines[i].startsWith('|')) raw.push(lines[i++]);
    if (raw.length < 2 || !/^\|[ |:\-]+\|\s*$/.test(raw[1])) throw new Error(`Malformed table ${start + 1}`);
    const rows = raw.map(tableCells), headers = rows[0], data = rows.slice(2);
    if (data.some(r => r.length !== headers.length)) throw new Error(`Unequal table cells at ${start + 1}`);
    const out = [emitPending(), '\\begingroup\\small', '\\setlength{\\LTleft}{0pt}\\setlength{\\LTright}{0pt}', '\\renewcommand{\\arraystretch}{1.2}', '\\begin{longtable}{@{}>{\\raggedright\\arraybackslash}p{0.25\\linewidth}>{\\raggedright\\arraybackslash}p{0.71\\linewidth}@{}}', '\\toprule'];
    if (headers.length === 2) {
      out.push(`${inline(headers[0], true)} & ${inline(headers[1], true)} \\\\ \\midrule`, '\\endhead');
      for (const row of data) out.push(`${inline(row[0], true)} & ${inline(row[1], true)} \\\\`);
    } else {
      // A stacked full-width table preserves every original row/column mapping
      // and avoids shrinking multi-parameter certificates to unreadable type.
      out.push('\\multicolumn{2}{@{}l@{}}{\\textit{Detailed comparison}} \\\\ \\midrule', '\\endhead');
      for (const row of data) {
        out.push(`\\multicolumn{2}{@{}p{0.96\\linewidth}@{}}{\\textbf{${inline(headers[0], true)}: ${inline(row[0], true)}}} \\\\`);
        for (let k = 1; k < headers.length; k++) out.push(`${inline(headers[k], true)} & ${inline(row[k], true)} \\\\`);
        out.push('\\addlinespace[0.45em]');
      }
    }
    out.push('\\bottomrule', '\\end{longtable}', '\\endgroup');
    emit(out.filter(Boolean).join('\n'), start, i - 1, 'table');
    tables.push({start: start + 1, end: i, columns: headers.length, rows: data.length, cells: (data.length + 1) * headers.length, layout: headers.length > 2 ? 'stacked comparison table' : 'two-column table'});
    continue;
  }
  const item = l.match(/^\s*([-*]|\d+\.)\s+(.*)$/);
  if (item) {
    const start = i, ordered = /\d/.test(item[1]), env = ordered ? 'enumerate' : 'itemize';
    const out = [emitPending(), `\\begin{${env}}`];
    while (i < last) {
      const m = lines[i].match(/^\s*([-*]|\d+\.)\s+(.*)$/);
      if (!m || /\d/.test(m[1]) !== ordered) break;
      const chunks = [m[2]]; i++;
      while (i < last && lines[i].trim() && !nextStartsBlock(i)) chunks.push(lines[i++].trim());
      out.push(`\\item${ordered ? `[${m[1]}]` : ''} ${inline(chunks.join(' '))}`);
      while (i < last && !lines[i].trim()) i++;
    }
    out.push(`\\end{${env}}`); emit(out.filter(Boolean).join('\n'), start, i - 1, 'list'); continue;
  }
  if (/^(?:```|>|\s*\$\$)/.test(l)) throw new Error(`Unsupported source block ${i + 1}: ${l}`);
  const start = i, para = [];
  while (i < last && lines[i].trim() && (i === start || !nextStartsBlock(i))) para.push(lines[i++].trim());
  emit(`${emitPending()}\n${inline(para.join(' '))}\n`, start, i - 1, 'paragraph');
}
if (pendingAnchors.length) tex.push(emitPending());
const missingRefs = [...targets].filter(t => !anchors.has(t));
if (missingRefs.length) throw new Error(`Missing source link targets: ${missingRefs.join(', ')}`);
const omittedLines = new Set(omitted.flatMap(r => Array.from({length: r.end - r.start + 1}, (_, k) => r.start + k - 1)));
const uncovered = [];
for (let n = first; n < last; n++) if (!used.has(n) && !omittedLines.has(n)) uncovered.push(n + 1);
if (uncovered.length) throw new Error(`Uncovered source lines ${uncovered.join(',')}`);
if (mathInventory.filter(m => m.tag).length !== tags.length) throw new Error('Lost an equation tag');
let output = tex.join('\n\n').trimEnd() + '\n';
if (/\\(?:input|include)\s*\{/.test(output)) throw new Error('Static appendix unexpectedly inputs another file');
if (/ZZINTTOKEN|^#{2,}|<a id=|<!--/m.test(output)) throw new Error('Unsupported markup remains');
if (/\\(?:over|choose)(?![A-Za-z])/.test(output)) throw new Error('Unmodernized infix fraction or binomial remains');
if (/\\boxed(?![A-Za-z])/.test(output)) throw new Error('A decorative equation box remains');
const emittedLabels = [...output.matchAll(/\\label\{([^}]+)\}/g)].map(m => m[1]);
if (new Set(emittedLabels).size !== emittedLabels.length) throw new Error('Duplicate emitted LaTeX labels');
const emittedReferences = [...output.matchAll(/\\(?:eqref|ref)\{([^}]+)\}|\\hyperref\[([^\]]+)\]/g)].map(m => m[1] || m[2]);
const danglingLatexReferences = [...new Set(emittedReferences)].filter(label => !emittedLabels.includes(label));
if (danglingLatexReferences.length) throw new Error(`Dangling emitted references: ${danglingLatexReferences.join(', ')}`);
fs.mkdirSync(path.dirname(outPath), {recursive: true});
fs.writeFileSync(outPath, output);
fs.mkdirSync(scratchBase, {recursive: true});
const scratch = fs.mkdtempSync(path.join(scratchBase, 'paper_rewrite_appendix_'));
const manifest = {sourcePath, sourceHash, outPath, outputHash: crypto.createHash('sha256').update(output).digest('hex'), sourceRange: [first + 1, last], selectedLineCount: last - first, coveredLineCount: used.size, omitted, uncovered, blocks, mathInventory, inlineMathCount, tables, displayLayouts, modernizedMath, anchors: [...anchors], internalLinkTargets: [...targets], missingRefs, emittedLabelCount: emittedLabels.length, emittedReferenceCount: emittedReferences.length, danglingLatexReferences, externalLinks, tags: tags.map(t => ({source: t, label: tagLabel.get(t), named: shortTag(t), proseReferences: tagReferences.get(t) || 0})), unsupportedMarkup: []};
fs.writeFileSync(path.join(scratch, 'conversion_manifest.json'), JSON.stringify(manifest, null, 2) + '\n');
if (process.argv.includes('--check')) {
  const wrapper = `\\documentclass[11pt]{article}
\\usepackage[T1]{fontenc}\\usepackage[utf8]{inputenc}\\usepackage{lmodern}
\\usepackage[margin=1in]{geometry}
\\usepackage{amsmath,amssymb,amsthm,mathtools,mathrsfs,graphicx,array,booktabs,longtable,tabularx}
\\usepackage[numbers]{natbib}\\usepackage[colorlinks=true]{hyperref}
\\usepackage{microtype}
\\setlength{\\emergencystretch}{2em}
\\begin{document}\\appendix
\\input{${outPath}}
\\end{document}
`;
  fs.writeFileSync(path.join(scratch, 'appendix_wrapper.tex'), wrapper);
  const r = spawnSync('latexmk', ['-pdf', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', 'appendix_wrapper.tex'], {cwd: scratch, encoding: 'utf8', maxBuffer: 20 * 1024 * 1024});
  fs.writeFileSync(path.join(scratch, 'build_output.txt'), `${r.stdout}\n${r.stderr}`);
  manifest.compileExit = r.status;
  const log = fs.readFileSync(path.join(scratch, 'appendix_wrapper.log'), 'utf8');
  manifest.resizedMath = [...log.matchAll(/INT(DISPLAY|TABLE):([^:\n]+):([0-9.]+)pt:([0-9.]+)pt/g)].map(m => ({kind:m[1],id:m[2],widthPt:Number(m[3]),availablePt:Number(m[4]),scale:Number(m[4])/Number(m[3])}));
  manifest.overfull = [...log.matchAll(/Overfull \\[hv]box[^\n]*/g)].map(m => m[0]);
  manifest.undefinedReferences = [...log.matchAll(/(?:Hyper reference|Reference) `([^']+)'[^\n]*undefined/g)].map(m => m[1]);
  manifest.duplicateDestinations = (log.match(/duplicate ignored/g) || []).length;
  fs.writeFileSync(path.join(scratch, 'conversion_manifest.json'), JSON.stringify(manifest, null, 2) + '\n');
  if (r.status !== 0) { console.log(r.stdout.slice(-11000)); console.log(r.stderr); }
}
console.log(JSON.stringify({sourceHash, outputHash: manifest.outputHash, sourceRange: manifest.sourceRange, coveredLines: used.size, omittedLines: omittedLines.size, displays: mathInventory.length, tags: tags.length, inlineMath: inlineMathCount, tables: tables.length, tableRows: tables.reduce((s,t)=>s+t.rows,0), anchors: anchors.size, missingRefs, scratch, compileExit: manifest.compileExit}, null, 2));
if (manifest.compileExit) process.exitCode = manifest.compileExit;
