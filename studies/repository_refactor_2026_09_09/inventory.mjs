// Read-only, deterministic inventory for the one-time repository migration.
// Usage: git ls-files -z | node studies/repository_refactor_2026_09_09/inventory.mjs HEAD_ID
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const tracked = new Set(fs.readFileSync(0,'utf8').split('\0'));
const skip = new Set(['.git', '.agents', '.codex', '.venv', 'node_modules',
  '__pycache__', '.pytest_cache', '.ruff_cache', '.mypy_cache', '.ipynb_checkpoints']);
const sourceExt = new Set(['.md','.tex','.py','.cpp','.c','.h','.hpp','.rs','.lean',
  '.mjs','.js','.ts','.sh','.toml','.yaml','.yml','.bib','.sty','.lua','.diff','.sha256']);
const dataExt = new Set(['.npz','.npy','.pt','.csv','.tsv','.png','.jpg','.jpeg','.svg',
  '.pdf','.jsonl','.zip','.gz','.tar','.log','.aux','.fls','.fdb_latexmk','.toc','.out','.lock']);

function kind(name, bytes) {
  const ext=path.extname(name).toLowerCase(), base=path.basename(name);
  if (name.startsWith('data/')) return ['data','separate generated/preserved data directory'];
  if (name.startsWith('.backups/')) return ['backup','pre-existing recovery copy; inventory, do not stage blindly'];
  if (sourceExt.has(ext)) return ['source','code, mathematical document, or source configuration'];
  if (dataExt.has(ext)) return ['data','generated output, build artifact, or mixed binary bundle'];
  if (ext === '.json') {
    if (/project_wide_audit|four_thread_consolidation|repository_refactor/.test(name))
      return ['source','research recovery or audit provenance'];
    if (/manifest|freeze|hash|config|lock|precommit|certificate|recurrence|contract|gate|audit/i.test(base)
        && bytes <= 1000000 && !/\/outputs\//.test(name))
      return ['source','small configuration, exact certificate, or audit/provenance record'];
    return ['data','generated numerical, symbolic-table or run output'];
  }
  if (ext === '.txt' || !ext || ext === '.html' || ext === '.term')
    return ['source','text source or historical research record; retained conservatively'];
  return ['review','unclassified file requires explicit decision'];
}

const files=[],symlinks=[];
function walk(dir) {
  for (const ent of fs.readdirSync(dir,{withFileTypes:true}).sort((a,b)=>a.name.localeCompare(b.name))) {
    if (skip.has(ent.name)) continue;
    const absolute=path.join(dir,ent.name), relative=path.relative(root,absolute);
    if (ent.isSymbolicLink()) {symlinks.push({path:relative,target:fs.readlinkSync(absolute)}); continue;}
    if (ent.isDirectory()) {walk(absolute);continue;}
    if (!ent.isFile()) continue;
    const buf=fs.readFileSync(absolute);
    const [category,reason]=buf.subarray(0,4).equals(Buffer.from([127,69,76,70]))
      ? ['data','compiled executable; source retained separately'] : kind(relative,buf.length);
    files.push({path:relative,bytes:buf.length,sha256:crypto.createHash('sha256').update(buf).digest('hex'),
      tracked:tracked.has(relative),category,reason});
  }
}
walk(root);
const totals={};
for(const f of files) {const s=totals[f.category]??={files:0,bytes:0,newBytes:0};s.files++;s.bytes+=f.bytes;if(!f.tracked)s.newBytes+=f.bytes;}
const offset=Number(process.argv[3]??0),count=Number(process.argv[4]??files.length);
console.log(JSON.stringify({schema:1,root,head:process.argv[2]??null,totals,symlinks,totalFiles:files.length,files:files.slice(offset,offset+count)}));
