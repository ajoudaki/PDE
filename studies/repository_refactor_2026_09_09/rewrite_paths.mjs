// Mechanical navigation/import repair; immutable research evidence is excluded.
// Default reports a compact plan. --apply performs only the listed text changes.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
const root=process.cwd(),base='studies/repository_refactor_2026_09_09';
const moves=JSON.parse(fs.readFileSync(`${base}/MOVE_MANIFEST.json`,'utf8'));
const before=JSON.parse(fs.readFileSync(`${base}/INVENTORY_BEFORE.json`,'utf8'));
const forward=new Map(moves.files.map(f=>[f.from,f.to]));
const inverse=new Map(moves.files.map(f=>[f.to,f.from]));
const prefixes=moves.prefixes;
function mapped(p){if(forward.has(p))return forward.get(p);for(const [a,b] of prefixes)if(p===a||p.startsWith(a+'/'))return b+p.slice(a.length);return p;}
function immutable(p){return /(^|\/)(sources|expanded_sources|inherited_baselines|archive|recovered|reviews?|audits?|source_audits|document_reviews|baseline|historical_project_documents)(\/|$)/i.test(p)
 || /recovered_sources_2026_09_09|repository_refactor_2026_09_09/.test(p)
 || /(?:audit|review|freeze|manifest|sha256|hash)/i.test(path.basename(p));}
const repairs=[];
for(const old of before.files.filter(f=>f.category==='source')){
 const current=forward.get(old.path)??old.path;
 if(!current.startsWith('studies/')||immutable(current)||!['.md','.py','.sh','.tex','.mjs'].includes(path.extname(current))||!fs.existsSync(current))continue;
 const original=fs.readFileSync(current,'utf8');let text=original;
 if(path.extname(current)==='.md'){
  text=text.replace(/\]\((<?)([^)\n]+?)(>?)\)/g,(whole,left,target,right)=>{
   if(/^(https?:|mailto:|#|codex:)/.test(target))return whole;
   const suffix=(target.match(/(:\d+)?(#[^\s]*)?$/)||[''])[0];let bare=target.slice(0,target.length-suffix.length);
   if(!bare)return whole;let rel;
   if(bare.startsWith(root+'/'))rel=bare.slice(root.length+1);
   else if(path.isAbsolute(bare))return whole;
   else rel=path.posix.normalize(path.posix.join(path.posix.dirname(old.path),bare));
   const next=mapped(rel);if(!fs.existsSync(path.join(root,next)))return whole;
   let link=path.posix.relative(path.posix.dirname(current),next)||'.';
   return `](${left}${link}${suffix}${right})`;
  });
 }
 // Absolute source paths and fully qualified imports/commands are unambiguous.
 for(const [from,to] of prefixes){
  text=text.split(root+'/'+from).join(root+'/'+to);
  if(from.startsWith('studies/')){
   if(path.extname(current)!=='.md')text=text.split(from).join(to);
   const modFrom=from.replaceAll('/','.'),modTo=to.replaceAll('/','.');
   text=text.split(modFrom).join(modTo);
  }
 }
 if(current==='studies/project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md'&&text!==original){
  text=text.replace('\n','\n\nNavigation-only relocation edition, 9 September 2026. Mathematical text and claim statuses are unchanged; historical reviews apply to the preserved pre-relocation bytes, not this new link-edited hash. See the [move ledger](../repository_refactor_2026_09_09/PLAN.md).\n');
 }
 if(text!==original){
  repairs.push({path:current,originalPath:inverse.get(current)??current,
    before:crypto.createHash('sha256').update(original).digest('hex'),after:crypto.createHash('sha256').update(text).digest('hex')});
  if(process.argv.includes('--apply'))fs.writeFileSync(current,text);
 }
}
console.log(JSON.stringify({files:repairs.length,repairs}));
