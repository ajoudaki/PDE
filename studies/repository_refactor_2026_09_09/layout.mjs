// One-time mechanical migration. Default is a read-only plan.
// Apply only after committing the source and recovery snapshots.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const root=process.cwd(), study='studies/repository_refactor_2026_09_09';
const inventory=JSON.parse(fs.readFileSync(path.join(root,study,'INVENTORY_BEFORE.json'),'utf8'));
const prefix=[];
function map(from,to){prefix.push([from,to]);}
function children(from,convert,except=[]){
  for(const ent of fs.readdirSync(path.join(root,from),{withFileTypes:true}))
    if(ent.isDirectory()&&!ent.name.startsWith('.')&&ent.name!=='__pycache__'&&!except.includes(ent.name))
      map(`${from}/${ent.name}`,`studies/${convert(ent.name)}`);
}
const renamed={
  temporary_deep_linear_joint_audit:'deep_linear_joint_limit',
  temporary_deep_linear_pde_no_go:'deep_linear_closure_boundary',
  temporary_arctan_mfp_reaudit:'arctan_source_reaudit',
  temporary_arctan_mfp_reconstruction:'arctan_source_reconstruction',
  generic_first_stieltjes:'mfp_gaussian_calculus',
  identity_compiler:'mfp_identity_compiler',quadratic_compiler:'mfp_quadratic_compiler',
  cubic_compiler:'mfp_cubic_compiler',sine_compiler:'mfp_sine_compiler',
  nonlinear_activation_operator_ide:'arctan_l2_order_one_readout',
  nonlinear_depth3_operator_ide:'arctan_l3_order_one_readout',
  tanh_depth3_operator_ide:'tanh_l3_operator_limit',
  leaky_arctan_depth3_operator_ide:'leaky_arctan_l3_operator_limit',
};
children('studies/mean_field_peeling',name=>renamed[name]??name.replace(/^temporary_/,'mfp_'),['archive','report']);
map('studies/mean_field_peeling','studies/mfp_program_history');
const resnet={
  'operator_pde/core':'resnet_operator_core',
  'operator_pde/generalization':'resnet_generalization',
  'operator_pde/activation_controls':'resnet_activation_controls',
  'operator_pde/rerun_2026-07-31':'resnet_reproduction_2026_07_31',
  'pde_convergence/01_proof_audit':'resnet_proof_audit',
  'pde_convergence/02_lean_salvage':'resnet_lean_salvage',
  'pde_convergence/03_bridgeability':'resnet_bridgeability',
  'pde_convergence/04_scalar_stress':'resnet_scalar_stress',
  'pde_convergence/05_tail_and_compactness':'resnet_tail_compactness',
  'dense_response/long_horizon':'resnet_dense_long_horizon',
  'dense_response/early_audit':'resnet_dense_early_audit',
};
for(const [from,to] of Object.entries(resnet))map(`studies/resnet_pde/${from}`,`studies/${to}`);
map('studies/resnet_pde','studies/resnet_program_history');
const stieltjes={
  resolution_program:'stieltjes_resolution',theory:'stieltjes_theory_history',
  'numerics/finite_width':'stieltjes_finite_width',
  'numerics/hybrid_mean_field_campaign':'stieltjes_hybrid_campaign',
  'numerics/direct_loewner':'stieltjes_direct_loewner',
  'numerics/global_proxy_campaign':'stieltjes_proxy_campaign',
};
for(const [from,to]of Object.entries(stieltjes))map(`studies/stieltjes_conjecture/${from}`,`studies/${to}`);
map('studies/stieltjes_conjecture','studies/stieltjes_program_history');
for(const [from,to]of Object.entries({arctan_l2:'rcgc_arctan_l2',arctan_l3:'rcgc_arctan_l3',
  generic_l1:'rcgc_shallow',linear_fixed_depth:'rcgc_linear_depth',compiler:'rcgc_compiler'}))
  map(`studies/renormalized_causal_gaussian_calculus/${from}`,`studies/${to}`);
map('studies/renormalized_causal_gaussian_calculus','studies/rcgc_program_history');
map('archive','studies/historical_project_documents/archive');
map('skills','studies/research_workflow_skills');
for(const f of ['AUTONOMOUS_DEEP_FEATURE_LEARNING_THEOREM_AND_PROGRAM_2026-08-21.md',
  'FINITE_CAUSAL_NEURAL_PDE_MASTER_MONOGRAPH_v2.2_2026-07-31.md',
  'UNIFIED_FINITE_CAUSAL_NEURAL_PDE_SYNTHESIS_2026-08-19.md'])
  map(f,`studies/historical_project_documents/${f}`);
prefix.sort((a,b)=>b[0].length-a[0].length);
function relocate(p){for(const [from,to]of prefix)if(p===from||p.startsWith(from+'/'))return to+p.slice(from.length);return p;}
const files=inventory.files.map(f=>({...f,to:f.category==='data'
  ? `data/historical/${relocate(f.path)}`
  : f.category==='backup'?`data/original_backups/${f.path.slice('.backups/'.length)}`:relocate(f.path)}));
const moved=files.filter(f=>f.to!==f.path),targets=new Set();
for(const f of moved){
  if(targets.has(f.to))throw Error(`Duplicate target: ${f.to}`);targets.add(f.to);
  if(path.isAbsolute(f.to)||f.to.split('/').includes('..'))throw Error('Unsafe relative target');
}
const plan={schema:1,baseline:inventory.head,prefixes:prefix,files:moved.map(({path,to,bytes,sha256,category})=>({from:path,to,bytes,sha256,category})),
  removed_aliases:inventory.symlinks,
  notes:['Data and backups are moved without deleting their bytes.','No Git history is rewritten.',
    'Historical source bytes are preserved; link modernization is a separate audited step.',
    'Aliases were only obsolete navigation links; actual target source is retained.']};
if(process.argv[2]!=='--apply'){
  if(process.argv[2]==='--summary')console.log(JSON.stringify({files:moved.length,data:files.filter(f=>f.category==='data').length,
    destinations:[...new Set(files.filter(f=>f.category==='source'&&f.to.startsWith('studies/')).map(f=>f.to.split('/')[1]))].sort()},null,2));
  else {const offset=Number(process.argv[2]??0),count=Number(process.argv[3]??moved.length);console.log(JSON.stringify({...plan,files:plan.files.slice(offset,offset+count),totalFiles:plan.files.length}));}
}else{
  // Check every source and every destination before the first move.
  for(const f of moved){const from=path.join(root,f.path),to=path.join(root,f.to);
    if(fs.existsSync(to))throw Error(`Destination already exists: ${f.to}`);
    const b=fs.readFileSync(from);if(b.length!==f.bytes||crypto.createHash('sha256').update(b).digest('hex')!==f.sha256)
      throw Error(`Source changed since inventory: ${f.path}`);
  }
  for(const f of moved){fs.mkdirSync(path.dirname(path.join(root,f.to)),{recursive:true});fs.renameSync(path.join(root,f.path),path.join(root,f.to));}
  for(const f of moved){const b=fs.readFileSync(path.join(root,f.to));if(b.length!==f.bytes||crypto.createHash('sha256').update(b).digest('hex')!==f.sha256)throw Error(`Destination changed: ${f.to}`);}
  // Remove only the two inventoried symlinks, never their targets.
  for(const f of inventory.symlinks){const p=path.join(root,f.path);if(fs.lstatSync(p).isSymbolicLink()&&fs.readlinkSync(p)===f.target)fs.unlinkSync(p);else throw Error(`Alias changed: ${f.path}`);}
  // Empty source directories only. Cache contents are handled separately.
  function empty(d){for(const e of fs.readdirSync(d,{withFileTypes:true})){if(e.isDirectory())empty(path.join(d,e.name));}
    if(fs.readdirSync(d).length===0)fs.rmdirSync(d);}
  for(const d of ['archive','skills','.backups','studies/mean_field_peeling','studies/resnet_pde','studies/stieltjes_conjecture','studies/renormalized_causal_gaussian_calculus'])
    if(fs.existsSync(path.join(root,d)))empty(path.join(root,d));
  console.log(JSON.stringify({moved:moved.length,verified:moved.length,deletedData:0}));
}
