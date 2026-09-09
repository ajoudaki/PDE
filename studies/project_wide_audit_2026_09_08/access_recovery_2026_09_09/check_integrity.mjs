// Read-only validation; no historical commands are executed.
import fs from 'node:fs';
import crypto from 'node:crypto';
import path from 'node:path';
const repo='/home/amir/Codes/PDE';
const audit=path.join(repo,'studies/project_wide_audit_2026_09_08');
const recovery=path.join(audit,'access_recovery_2026_09_09');
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const master=fs.readFileSync(path.join(audit,'MASTER_RESEARCH_REPORT.md'));
const result={master:{bytes:master.length,sha256:hash(master)},links:[],snapshots:[],histories:[],temporarySources:[],baseline:{},access:{}};
result.attachments=[];
result.originalProofMatches=[];
for(const m of master.toString('utf8').matchAll(/\]\((\/[^\n]*?)\)/g)){
  const target=m[1]; const lm=target.match(/:(\d+)$/);
  const file=lm?target.slice(0,-lm[0].length):target;
  try{const b=fs.readFileSync(file);const lines=b.toString('utf8').split('\n').length;result.links.push({target,ok:!lm||Number(lm[1])<=lines});}
  catch(e){result.links.push({target,ok:false,error:e.code});}
}
for(const line of fs.readFileSync(path.join(audit,'sources/ARCTAN_DESTINATION_SHA256.txt'),'utf8').trim().split('\n')){
  const m=line.match(/^([0-9a-f]{64})\s+(.+)$/);if(!m)throw Error('Malformed snapshot manifest');
  const b=fs.readFileSync(path.join(repo,m[2]));result.snapshots.push({file:m[2],ok:hash(b)===m[1]});
}
for(const f of JSON.parse(fs.readFileSync(path.join(recovery,'SESSION_INVENTORY.json'),'utf8')).files){
  try{const b=fs.readFileSync(f.file);result.histories.push({task:f.task,file:f.file,bytes:b.length,ok:hash(b)===f.sha256});}
  catch(e){result.histories.push({file:f.file,ok:false,error:e.code});}
}
for(const f of JSON.parse(fs.readFileSync(path.join(recovery,'sources/TEMP_SOURCE_MANIFEST.json'),'utf8'))){
  const b=fs.readFileSync(f.archive);result.temporarySources.push({file:f.archive,ok:hash(b)===f.sha256,sourceStillEqual:b.equals(fs.readFileSync(f.source))});
}
const old=fs.readFileSync(path.join(recovery,'baseline/MASTER_RESEARCH_REPORT.md'));
result.baseline={sha256:hash(old),ok:hash(old)==='09dde386c53621ced229ba41d042829bf5b79fcc6376aaf328dbf2d23b53f5e0'};
for(const p of ['/tmp/tp3-audit.Trwr6N/proofs.tex','/tmp/tensor-programs-iii.txt','/tmp/l2-proof-review-wBzgFS/TWO_HIDDEN_LAYER_PROOF.md','/tmp/l3-arctan-audit-sZue2v/EXACT_RESULTS_AND_GAP.md','/tmp/l3-extension-check-mj4s9q/VERIFIED_SCOPE.md']){
  try{const b=fs.readFileSync(p);result.access[p]={readable:true,bytes:b.length,sha256:hash(b)};}
  catch(e){result.access[p]={readable:false,error:e.code};}
}
for(const f of JSON.parse(fs.readFileSync(path.join(recovery,'ATTACHMENT_MANIFEST.json'),'utf8'))){
  const b=fs.readFileSync(f.file);result.attachments.push({file:f.file,ok:hash(b)===f.sha256});
}
const base=path.join(repo,'studies/four_thread_consolidation');
for(const [source,archive] of [
  ['/tmp/l2-proof-review-wBzgFS/TWO_HIDDEN_LAYER_PROOF.md',path.join(base,'inherited_baselines/L2_ONE_SAMPLE_ARCTAN_GLOBAL_PROOF.md')],
  ['/tmp/l3-arctan-audit-sZue2v/EXACT_RESULTS_AND_GAP.md',path.join(base,'expanded_sources/EXPLAIN_PRIMARY/l3-arctan-audit-sZue2v/EXACT_RESULTS_AND_GAP.md')],
  ['/tmp/l3-extension-check-mj4s9q/VERIFIED_SCOPE.md',path.join(base,'expanded_sources/EXPLAIN_PRIMARY/l3-extension-check-mj4s9q/VERIFIED_SCOPE.md')]
]){result.originalProofMatches.push({source,archive,ok:fs.readFileSync(source).equals(fs.readFileSync(archive))});}
const tex=fs.readFileSync('/tmp/tp3-audit.Trwr6N/proofs.tex');
const texArchive=fs.readFileSync(path.join(recovery,'sources/TP3_PROOFS.tex'));
result.texArchive={sourceSha256:hash(tex),archiveSha256:hash(texArchive),onlyAddedTerminalNewline:texArchive.length===tex.length+1&&texArchive[tex.length]===10&&texArchive.subarray(0,tex.length).equals(tex)};
result.summary={localLinks:result.links.length,continuationSnapshots:result.snapshots.length,histories:result.histories.length,historyBytes:result.histories.reduce((s,x)=>s+(x.bytes||0),0),preservedTemporarySources:result.temporarySources.length,failures:[...result.links,...result.snapshots,...result.histories,...result.temporarySources].filter(x=>!x.ok)};
result.summary.attachments=result.attachments.length;
result.summary.originalProofMatches=result.originalProofMatches.length;
result.summary.failures.push(...result.attachments.filter(x=>!x.ok),...result.originalProofMatches.filter(x=>!x.ok));
if(!result.texArchive.onlyAddedTerminalNewline)result.summary.failures.push({file:'TP3_PROOFS.tex',error:'Unexpected archive difference'});
process.stdout.write(JSON.stringify(result,null,2)+'\n');
