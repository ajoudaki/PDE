// Read-only mechanical validation of the integrated setup document.
// These checks do not validate mathematical proofs or numerical stability.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const dir = path.dirname(new URL(import.meta.url).pathname);
const result = fs.readFileSync(path.join(dir, 'RESULT.md'), 'utf8');
const failures = [];
const requireCheck = (condition, message) => {
  if (!condition) failures.push(message);
};
// A TeX row break such as \\[2mm] is not a \[ display opener.
const count = token => {
  let total = 0;
  for (let at = result.indexOf(token); at !== -1; at = result.indexOf(token, at + token.length)) {
    if (at === 0 || result[at - 1] !== '\\') total++;
  }
  return total;
};
requireCheck(count('\\[') === count('\\]'), 'Unbalanced display math');
requireCheck(count('\\(') === count('\\)'), 'Unbalanced inline math');
requireCheck(!/[\x00-\x08\x0b\x0c\x0e-\x1f]/.test(result), 'Control character');
requireCheck(!/[\t ]+$/m.test(result), 'Trailing whitespace');
requireCheck(!result.includes('setup-orders:insert-here'), 'Unresolved insertion marker');
requireCheck(!/\^\\ell_\*/.test(result), 'Unbraced spherical exponent');
requireCheck(!/(?<!\\)\bqquad\b/.test(result), 'Unescaped qquad command');

function uniqueMatches(pattern, label) {
  const values = [...result.matchAll(pattern)].map(match => match[1]);
  const seen = new Set();
  for (const value of values) {
    requireCheck(!seen.has(value), `Duplicate ${label}: ${value}`);
    seen.add(value);
  }
  return seen;
}
const tags = uniqueMatches(/\\tag\{([^}]+)\}/g, 'equation tag');
const anchors = uniqueMatches(/<a id="([^"]+)"><\/a>/g, 'anchor');
const stack = [];
for (const match of result.matchAll(/\\(begin|end)\{([^}]+)\}/g)) {
  if (match[1] === 'begin') stack.push(match[2]);
  else requireCheck(stack.pop() === match[2], `Mismatched environment: ${match[2]}`);
}
requireCheck(stack.length === 0, 'Unclosed math environment');

let links = 0;
const prose = result.replace(/\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)|\$\$[\s\S]*?\$\$|\$[^$\n]*\$/g, '');
for (const match of prose.matchAll(/\]\(([^)\n]+)\)/g)) {
  const target = match[1];
  if (/^(https?:|mailto:)/.test(target)) continue;
  const [file, anchor] = target.split('#');
  if (!file) requireCheck(anchors.has(anchor), `Missing anchor: ${anchor}`);
  else {
    const destination = path.resolve(dir, file);
    requireCheck(fs.existsSync(destination), `Missing local link: ${file}`);
    if (anchor && destination === path.join(dir, 'RESULT.md')) {
      requireCheck(anchors.has(anchor), `Missing RESULT anchor: ${anchor}`);
    }
  }
  links++;
}
for (const fragment of ['SETUP_INTEGRATION_ORDERS.md', 'SETUP_INTEGRATION_PROOFS.md']) {
  const text = fs.readFileSync(path.join(dir, fragment), 'utf8').trimEnd();
  requireCheck(result.includes(text), `Fragment differs from integrated text: ${fragment}`);
}
// Author completion fragments are mirrored into RESULT; their administrative
// provenance paragraphs are deliberately not part of the theorem text.
const sourceCompletion = fs.readFileSync(path.join(dir, 'SOURCE_INSERTION_COMPLETION.md'), 'utf8');
const backendCompletion = fs.readFileSync(path.join(dir, 'DECODER_WORD_BACKEND.md'), 'utf8');
const decoderCompletion = fs.readFileSync(path.join(dir, 'DECODER_FINITE_CONSTRUCTION.md'), 'utf8');
const completedBlocks = [
  ['insertion-completion:local', sourceCompletion.slice(sourceCompletion.indexOf('The first conclusion'), sourceCompletion.indexOf('## 6.'))],
  ['insertion-completion:finite', sourceCompletion.slice(sourceCompletion.indexOf('## 6.'), sourceCompletion.indexOf('## 10.'))],
  ['decoder-backend', backendCompletion.slice(backendCompletion.indexOf('All parameters in this section'))],
  ['decoder-construction', decoderCompletion.slice(decoderCompletion.indexOf('## 1.'), decoderCompletion.indexOf('Scientific inputs actually read:'))],
];
for (const [name, text] of completedBlocks) {
  const expected = text.trimEnd().replace(/^#{2,3} /gm, heading => '###' + heading);
  const begin = '<!-- ' + name + ':start -->\n';
  const end = '\n<!-- ' + name + ':end -->';
  const at = result.indexOf(begin);
  const stop = result.indexOf(end, at);
  requireCheck(at >= 0 && stop > at, 'Missing completion block: ' + name);
  requireCheck(result.slice(at + begin.length, stop) === expected,
    'Completion fragment differs from integrated text: ' + name);
}
const output = {
  result_sha256: crypto.createHash('sha256').update(result).digest('hex'),
  lines: result.split('\n').length - 1,
  display_pairs: count('\\['), inline_pairs: count('\\('),
  equation_tags: tags.size, explicit_anchors: anchors.size, local_links: links,
  failures,
};
console.log(JSON.stringify(output, null, 2));
if (failures.length) process.exitCode = 1;
