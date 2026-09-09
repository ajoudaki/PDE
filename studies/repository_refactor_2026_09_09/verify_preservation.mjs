// Read-only preservation checks; run from the repository root.
// Snapshot verification:
// node .../verify_preservation.mjs --git-requests | git cat-file --batch |
//   node .../verify_preservation.mjs --verify-git
// Current retained bytes: node .../verify_preservation.mjs --filesystem
import fs from 'node:fs';
import crypto from 'node:crypto';

const base = 'studies/repository_refactor_2026_09_09/';
const recovered = 'studies/recovered_sources_2026_09_09/';
const inventory = JSON.parse(fs.readFileSync(base + 'INVENTORY_BEFORE.json'));
const moves = JSON.parse(fs.readFileSync(base + 'MOVE_MANIFEST.json'));
const byOld = new Map(moves.files.map(f => [f.from, f.to]));
byOld.set('requirements-lock.txt',
  'studies/historical_project_documents/requirements-lock-2026-07-31.txt');
// The new inventory helper inventoried itself before receiving pagination and
// ELF detection edits. It is migration tooling, not pre-existing user research.
// Its committed edition is preserved, but is not byte-identical to that self-row.
const toolingException = base + 'inventory.mjs';
const sources = inventory.files.filter(f => f.category === 'source' && f.path !== toolingException);
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const mode = process.argv[2];

if (mode === '--git-requests') {
  for (const f of sources) {
    if (/[\r\n]/.test(f.path)) throw Error('Unexpected newline in original path');
    console.log('25dfbf2:' + f.path);
  }
} else if (mode === '--verify-git') {
  const bytes = fs.readFileSync(0);
  let at = 0, verified = 0, total = 0;
  const failures = [];
  for (const f of sources) {
    const end = bytes.indexOf(10, at);
    if (end < at) throw Error('Truncated git batch header');
    const header = bytes.subarray(at, end).toString();
    at = end + 1;
    const match = /^([0-9a-f]+) blob (\d+)$/.exec(header);
    if (!match) {
      failures.push({path: f.path, header});
      continue;
    }
    const length = Number(match[2]);
    const blob = bytes.subarray(at, at + length);
    at += length;
    if (bytes[at++] !== 10) throw Error('Truncated git batch payload');
    if (length !== f.bytes || sha(blob) !== f.sha256) failures.push({path: f.path});
    else { verified++; total += length; }
  }
  if (at !== bytes.length) throw Error('Unexpected trailing git batch bytes');
  console.log(JSON.stringify({snapshot: '25dfbf2', verified, bytes: total,
    toolingException, failures}));
  if (failures.length) process.exitCode = 1;
} else if (mode === '--filesystem') {
  const counts = {}, changedSources = [], failures = [];
  for (const f of inventory.files) {
    const target = byOld.get(f.path) ?? f.path;
    if (!fs.existsSync(target)) { failures.push({original: f.path, target, reason: 'missing'}); continue; }
    const bytes = fs.readFileSync(target);
    if (bytes.length !== f.bytes || sha(bytes) !== f.sha256) {
      if (f.category === 'source') changedSources.push({original: f.path, target,
        before: f.sha256, after: sha(bytes)});
      else failures.push({original: f.path, target, reason: 'changed retained data/backup'});
    } else {
      const c = counts[f.category] ??= {files: 0, bytes: 0};
      c.files++; c.bytes += bytes.length;
    }
  }
  const records = [];
  for (const name of ['VERIFIED_ORIGINAL.jsonl', 'VERIFIED_TAR_SUPPLEMENT.jsonl']) {
    for (const line of fs.readFileSync(recovered + 'manifests/' + name, 'utf8').trim().split('\n')) {
      const f = JSON.parse(line);
      records.push({...f, target: recovered + f.path});
    }
  }
  for (const f of JSON.parse(fs.readFileSync(recovered + 'manifests/CHECKPOINT_SUPPLEMENT.json')))
    records.push({...f, target: f.to});
  for (const f of JSON.parse(fs.readFileSync(recovered + 'manifests/SESSION_SUPPLEMENT.json')))
    records.push({...f, target: f.to});
  const restored = JSON.parse(fs.readFileSync(base + 'RESTORED_CONFIGURATIONS.json'));
  let restoredFiles = 0;
  for (const f of restored.files) {
    if (!fs.existsSync(f.to)) { failures.push({target: f.to, reason: 'missing restored metadata'}); continue; }
    const bytes = fs.readFileSync(f.to);
    if (bytes.length !== f.bytes || sha(bytes) !== f.sha256)
      failures.push({target: f.to, reason: 'changed restored metadata'});
    else restoredFiles++;
  }
  let recoveredFiles = 0, recoveredBytes = 0;
  for (const f of records) {
    if (!fs.existsSync(f.target)) { failures.push({target: f.target, reason: 'missing recovered source'}); continue; }
    const bytes = fs.readFileSync(f.target);
    if (bytes.length !== f.bytes || sha(bytes) !== f.sha256)
      failures.push({target: f.target, reason: 'changed recovered source'});
    else { recoveredFiles++; recoveredBytes += bytes.length; }
  }
  console.log(JSON.stringify({unchanged: counts, changedSources,
    recovered: {files: recoveredFiles, bytes: recoveredBytes}, restoredFiles, failures}));
  if (failures.length) process.exitCode = 1;
} else {
  throw Error('Choose --git-requests, --verify-git, or --filesystem');
}
