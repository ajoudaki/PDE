import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

// Read-only corpus reader. All output goes to stdout; no research/session writes.
const root='/home/codex-b/.codex/sessions';
const index='/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/TASK_INDEX.md';
const part=fs.readFileSync(index,'utf8').split('## PDE-2')[1];
const tasks=[...part.matchAll(/\| (\d+) \| ([^|]+) \| ([a-f0-9-]{36})/g)].map(m=>({no:+m[1],name:m[2].trim(),id:m[3]}));
const all=[];
function walk(d){for(const e of fs.readdirSync(d,{withFileTypes:true})){const f=path.join(d,e.name);if(e.isDirectory())walk(f);else if(e.name.endsWith('.jsonl'))all.push(f);}}
walk(root);all.sort();
const [command='inventory',nums='all',startArg='0',countArg='40000']=process.argv.slice(2);
const chosen=nums==='all'?tasks:tasks.filter(t=>nums.split(',').map(Number).includes(t.no));
const digest=x=>crypto.createHash('sha256').update(x).digest('hex');
function textParts(p){if(typeof p==='string')return p;if(Array.isArray(p))return p.map(v=>v.text??(v.type==='image'?'[image block]':JSON.stringify(v))).join('\n');return JSON.stringify(p);}
const out=[],seen=new Set();let duplicate=0,admin=0,totalBytes=0,parseErrors=[];
for(const t of chosen){
 const files=all.filter(f=>path.basename(f).includes(t.id));
 for(const f of files){
  let buf;try{buf=fs.readFileSync(f);}catch(e){out.push({task:t.no,file:f,error:e.code});continue;}
  totalBytes+=buf.length;const rows=buf.toString('utf8').split('\n');let kinds={},dialogueChars=0,toolChars=0;
  for(let j=0;j<rows.length;j++){
   if(!rows[j])continue;let o;try{o=JSON.parse(rows[j]);}catch(e){parseErrors.push({file:f,line:j+1,error:e.message});continue;}
   const p=o.payload??{};const kind=o.type+':'+(p.type??'');kinds[kind]=(kinds[kind]??0)+1;
   let str=null,category=null;
   if(o.type==='response_item'&&p.type==='message'&&['user','assistant'].includes(p.role)){
    category='chat';str=`${p.role} ${p.channel??''}\n${textParts(p.content)}`;dialogueChars+=str.length;
   }else if(o.type==='response_item'&&['function_call','function_call_output','custom_tool_call','custom_tool_call_output'].includes(p.type)){
    category='tools';str=`${p.type} ${p.name??''} ${p.call_id??''}\n${textParts(p.arguments??p.input??p.output??p)}`;toolChars+=str.length;
   }else if(o.type==='compacted'){
    category='chat';str=`compaction summary\n${textParts(p.message??p)}`;dialogueChars+=str.length;
   }else{admin++;}
   if(str!==null&&command==='narrative'&&category==='chat'){
    // Exclude only repeated app metadata, not mathematical/user prose or compactions.
    str=str.replace(/<(recommended_plugins|environment_context|skills_instructions|app-context)>[\s\S]*?<\/\1>/g,'[historical app metadata omitted]');
   }
   if(str!==null&&command!=='inventory'&&(command==='all'||command===category||(command==='narrative'&&category==='chat'))){
    // Exact payload duplicates across inherited branches are read once, not paraphrased.
    const h=digest(str);if(seen.has(h)){duplicate++;continue;}seen.add(h);
    out.push(`\n--- TASK ${t.no} ${t.name}; ${f}:${j+1}; ${o.timestamp??''} ---\n${str}\n`);
   }
  }
  if(command==='inventory')out.push({task:t.no,name:t.name,id:t.id,file:f,bytes:buf.length,sha256:digest(buf),lines:rows.length-1,kinds,dialogueChars,toolChars});
 }
}
if(command==='inventory'){
 console.log(JSON.stringify({files:out,totalBytes,parseErrors},null,2));
}else{
 const str=out.map(x=>typeof x==='string'?x:JSON.stringify(x)).join('');const start=+startArg,count=+countArg;
 console.log(JSON.stringify({tasks:chosen.map(t=>t.no),mode:command,totalChars:str.length,totalBytes,uniqueRecords:seen.size,exactDuplicatesOmitted:duplicate,administrativeRecords:admin,parseErrors,range:[start,Math.min(start+count,str.length)],eof:start+count>=str.length}));
 process.stdout.write(str.slice(start,start+count));
}
