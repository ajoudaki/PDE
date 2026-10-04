"""Independent, CPU-only audit of frozen stage-two geometry/certificate inputs."""
import ast
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import resource
import sys
import time
import types

resource.setrlimit(resource.RLIMIT_CPU, (300, 300))
import numpy as np
import scipy
from scipy.integrate import solve_ivp
import torch

ROOT = Path(__file__).resolve().parents[2]
STUDY = Path(__file__).resolve().parent
DATA = ROOT / 'data/generated/response_memory_use_cases_20261001'
OUT = DATA / 'stage2_geometry_review01'
OUT.mkdir(exist_ok=True)
torch.set_num_threads(1)
started = time.process_time()
hashes = {}

def sha(p):
    p = Path(p)
    value = hashlib.sha256(p.read_bytes()).hexdigest()
    hashes[str(p.relative_to(ROOT))] = value
    return value

def read(p):
    sha(p)
    return json.loads(Path(p).read_text())

def source(name, path, selected=None):
    """Load assigned classes only; omit the unused maintained dictionary import."""
    sha(path)
    tree = ast.parse(path.read_text())
    if selected:
        tree.body = [n for n in tree.body if isinstance(n,(ast.FunctionDef,ast.ClassDef)) and n.name in selected]
    else:
        tree.body = [n for n in tree.body if not (isinstance(n,ast.ImportFrom) and n.module=='pde.observable_initialization')]
    module = types.ModuleType(name)
    module.__file__ = str(path)
    module.torch = torch
    if selected:
        module.LowRankFlow = sys.modules['baseline_compact_flow'].LowRankFlow
    sys.modules[name] = module
    exec(compile(tree,str(path),'exec'),module.__dict__)
    return module

base = source('baseline_compact_flow',STUDY/'baseline_compact_flow.py')
field = source('input_field',STUDY/'input_field.py')
selected = source('stage2_index_experiment',STUDY/'stage2_index_experiment.py',{'pca','TunedFactors'})
new = source('audit_new_gate',STUDY/'stage2_root_gate.py')
old = source('audit_old_gate',DATA/'stage2_root_gate01/stage2_root_gate.py')

# Frozen provenance and numerical capture results, without re-running GPU work.
manifests={}
for folder in ('stage2_root_gate01','stage2_root_gate_diagnostics01'):
    manifest=read(DATA/folder/'manifest.json')
    matches={n:sha(DATA/folder/n)==v for n,v in manifest['sources'].items()}
    assert all(matches.values())
    manifests[folder]={'source_hash_matches':matches,'capture':read(DATA/folder/'capture_checks.json'),
                       'completion':read(DATA/folder/'completion.json')}

# Independently differentiate the actual parameterization in multiple dimensions.
rng=np.random.default_rng(10022026)
errors={'autograd':0.,'jvp':0.,'rank_excess':0.,'source_parity':0.,'ungated_parity':0.,
        'decomposition':0.,'zero_residual':0.,'replication':0.,'pca':0.}
branches=set()
cases=0
for q in (1,3,7):
    for trial in range(12):
        n,m,d,C=9,13,5,2
        X=rng.normal(size=(m,d));X/=np.linalg.norm(X,axis=1,keepdims=True)
        y=rng.normal(size=m)
        Q,_=np.linalg.qr(rng.normal(size=(m,C)));basis=Q*np.sqrt(m)
        kw=dict(width=n,depth=2,activation='tanh',seed=trial+87,device='cpu',dtype=torch.float64,
                hidden_gain=1.,readout_std=1.,order=q)
        a=new.CertifiedField(X,y,basis,gated=True,**kw)
        b=old.CertifiedField(X,y,basis,gated=True,**kw)
        c=field.InputFieldFlow(X,y,basis,**kw)
        with torch.no_grad():
            a.c.copy_(torch.tensor(rng.normal(size=n)))
            for moment in a.moments:moment.add_(torch.tensor(rng.normal(size=moment.shape))*.4)
            a.s.fill_(.7)
            # Select a broad gate ramp without any training or outcome selection.
            a.kappa.fill_(10. if trial%2 else .00001)
            for target in (b,c):
                for target_v,source_v in zip(target.state,a.state):target_v.copy_(source_v)
            b.kappa.copy_(a.kappa)
        velocity,metrics,V=a.fields_and_velocity()
        oldvel,oldmetrics,oldV=b.fields_and_velocity()
        errors['source_parity']=max(errors['source_parity'],float((V-oldV).abs().max()),
            float((metrics[:6]-oldmetrics).abs().max()),*(float((v-u).abs().max()) for v,u in zip(velocity,oldvel)))
        gamma=float(metrics[3]);branches.add('zero' if gamma==0 else 'one' if gamma==1 else 'ramp')
        w,c_read,A,B,s=[v.clone().requires_grad_() for v in a.state]
        weights=torch.arange(q,dtype=torch.float64)*2+1
        def matrix(A,B,s):
            ans=a.matrices[0].clone()
            for j in range(q):
                for k in range(C):ans=ans-2*weights[j]*torch.outer(A[j,:,k],B[j,:,k])/(n*(1+s))
            return ans
        W=matrix(A,B,s)
        h=torch.tanh(w@a.inputs.T);g=torch.tanh(W@h)
        prediction=c_read@g/n
        loss=(prediction-a.labels).square().mean()
        gradients=torch.autograd.grad(loss,(w,c_read,A,B,s))
        derivative=sum((g*v).sum() for g,v in zip(gradients,velocity))
        errors['autograd']=max(errors['autograd'],abs(float(derivative-metrics[5])))
        _,dW=torch.autograd.functional.jvp(matrix,(A,B,s),tuple(velocity[2:]))
        errors['jvp']=max(errors['jvp'],float((dW-gamma*V).abs().max()))
        errors['rank_excess']=max(errors['rank_excess'],float(torch.linalg.svdvals(V)[2*C:].max()))
        errors['decomposition']=max(errors['decomposition'],float(abs(metrics[8])))
        assert float(derivative)<1e-10
        a.gated=False
        errors['ungated_parity']=max(errors['ungated_parity'],*(float((v-u).abs().max()) for v,u in zip(a.rhs(),c.rhs())))
        a.labels.copy_(a.predict(a.inputs));a.gated=True
        errors['zero_residual']=max(errors['zero_residual'],*(float(v.abs().max()) for v in a.rhs()))
        cases+=1

# Verify the imported PCA basis and its initial feature-Gram commutation.
pca_initial_commutator=0.
for _ in range(3):
    h=torch.tensor(rng.normal(size=(9,13)),dtype=torch.float64)
    basis,_,_,reported=selected.pca(h,3)
    P=basis@basis.T/13
    A=h.T@h
    errors['pca']=max(errors['pca'],float((basis.T@basis/13-torch.eye(3)).abs().max()),reported)
    pca_initial_commutator=max(pca_initial_commutator,float((A@P-P@A).abs().max()))
assert pca_initial_commutator<1e-10

# Exact replication of scalar binary states at width five, including derivatives.
for q in (1,3,7):
    models=[]
    u=np.arctanh([.75,.25,.25]);r_read=-.013
    backward=rng.normal(size=q)*.003;forward=rng.normal(size=q)*.004;forward[0]+=2*5/12
    for n in (1,5):
        model=new.CertifiedField(np.eye(3),np.array([-1.,1.,1.]),np.ones((3,1)),
            width=n,depth=2,activation='tanh',seed=52,device='cpu',dtype=torch.float64,
            hidden_gain=1.,readout_std=1.,order=q,gated=False)
        with torch.no_grad():
            model.w.copy_(torch.tensor(u).expand(n,3));model.c.fill_(r_read)
            model.matrices[0].fill_(.02/n);model.s.fill_(1.)
            model.moments[0].copy_(torch.tensor(backward)[:,None,None].expand(q,n,1))
            model.moments[1].copy_(torch.tensor(forward)[:,None,None].expand(q,n,1))
        models.append(model)
    va,ma,Wa=models[0].fields_and_velocity();vb,mb,Wb=models[1].fields_and_velocity()
    errors['replication']=max(errors['replication'],float((ma[:6]-mb[:6]).abs().max()),
        float((models[0].predict(np.eye(3))-models[1].predict(np.eye(3))).abs().max()),
        float((5*Wb-Wa).abs().max()),*(float((b-a).abs().max()) for a,b in zip(va,vb)))

# Four independently implemented scalar ODE solves at untested orders/epsilons.
ode=[]
for q in (3,8):
    for eps in (.03,.015):
        weights=2*np.arange(q)+1
        initial=np.r_[np.arctanh([.75,.25,.25]),0.,1.,np.r_[5/12,np.zeros(q-1)],np.zeros(q)]
        labels=np.array([-1.,1.,1.])
        def scalar(state):
            u=state[:3];w=state[3];tau=state[4];hbar=state[5:5+q];dbar=state[5+q:]
            v=eps-2*np.sum(weights*hbar*dbar)/tau
            h=np.tanh(u);h2=np.tanh(v*h);residual=w*h2-labels
            rho=np.linalg.norm(residual)/np.sqrt(3)
            du=-2/3*residual*w*(1-h2*h2)*v*(1-h*h)
            dw=-2*np.mean(residual*h2)
            R=np.mean(residual*w*(1-h2*h2));H=h.mean()
            dh=np.array([rho*H-rho/tau*(j*hbar[j]+sum(weights[k]*hbar[k] for k in range(j))) for j in range(q)])
            db=np.array([R-rho/tau*(j*dbar[j]+sum(weights[k]*dbar[k] for k in range(j))) for j in range(q)])
            dv=-2*np.sum(weights*(dh*dbar+hbar*db))/tau+2*rho*np.sum(weights*hbar*dbar)/(tau*tau)
            df=dw*h2+w*(1-h2*h2)*(dv*h+v*(1-h*h)*du)
            return np.r_[du,dw,rho,dh,db],2*np.mean(residual*df)
        result=solve_ivp(lambda t,z:scalar(z)[0],(0,3*np.pi*np.sqrt(3/5)),initial,
                         method='DOP853',rtol=1e-12,atol=1e-14)
        assert result.success
        derivative=scalar(result.y[:,-1])[1]
        ode.append({'q':q,'epsilon':eps,'derivative':derivative,'normalized':derivative/(eps*eps/36),'nfev':result.nfev})
        assert derivative>0

# Random-matrix test of the quantified noncommutation obstruction.
commutation=[]
for _ in range(10):
    H=rng.normal(size=(4,7));Z,_=np.linalg.qr(rng.normal(size=(7,2)));P=Z@Z.T
    A=H.T@H;J=(A@P+P@A)/2
    vals,vecs=np.linalg.eigh(J);a=np.linalg.norm(P@A@P,2);b=np.linalg.norm(P@A@(np.eye(7)-P),2)
    bound=-b*b/(2*(np.sqrt(a*a+b*b)+a));B=np.zeros((4,7));B[0]=vecs[:,0]
    pairing=float(np.sum((B@H.T)*(B@P@H.T)))
    assert vals[0]<=bound+1e-12 and abs(pairing-vals[0])<1e-12 and pairing<0
    commutation.append({'lambda_min':vals[0],'upper_bound':bound,'realized_pairing':pairing})

# Recompute test errors from predictions, selections from validation, and all diagnostics.
rows=read(DATA/'stage2_root_gate01/results.json')
summary={};raw_error=0.;derivative_error=0.;gate_error=0.;increases=0
for folder in sorted((DATA/'stage2_root_gate01').glob('fit_*')):
    r=read(folder/'result.json');sha(folder/'arrays.npz');arr=np.load(folder/'arrays.npz')
    truth=arr['target'];pred=arr['predictions'];metrics=arr['metrics']
    assert r['selected_index']==int(np.argmin([c['val'] for c in r['checkpoints']]))
    assert r['selected']==r['checkpoints'][r['selected_index']]
    for i,checkpoint in enumerate(r['checkpoints']):
        recomputed=float(np.sqrt(np.mean((pred[i].astype(float)-truth)**2)))
        raw_error=max(raw_error,abs(recomputed-checkpoint['test']))
    if len(metrics):
        observed={'sampled_hidden_ascent_fraction':float(np.mean(metrics[:,3]>1e-10)),
                  'sampled_ungated_loss_ascent_fraction':float(np.mean(metrics[:,5]>1e-10)),
                  'sampled_actual_loss_ascent_fraction':float(np.mean(metrics[:,6]>1e-10)),
                  'mean_gate':float(metrics[:,4].mean()),'minimum_gate':float(metrics[:,4].min()),
                  'maximum_hidden_contribution':float(metrics[:,3].max())}
        assert observed==r['diagnostics']
        derivative_error=max(derivative_error,float(np.max(abs(metrics[:,5]-(-metrics[:,2]+metrics[:,3])))),
            float(np.max(abs(metrics[:,6]-(-metrics[:,2]+metrics[:,4]*metrics[:,3])))))
        increases+=int(np.sum(np.diff(metrics[:,1])>1e-10))
        if r['kind']=='gated':
            labels=np.load(DATA/'stage2_data01'/f"{r['domain']}.npz")['y_train']
            expected=np.clip(-metrics[:,3]/(.001*np.mean(labels**2)),0,1)
            gate_error=max(gate_error,float(np.max(abs(expected-metrics[:,4]))))
            assert metrics[:,6].max()<=1e-10

for domain in ('fashion','har','housing'):
    domainrows=[r for r in rows if r['domain']==domain]
    main=[r for r in domainrows if r['dt']==1/32]
    entry={'test_medians':{},'paired_ratios':{},'diagnostics':{},'refinement':{}}
    for method in ('field','gated','factor'):
        chosen=[r for r in main if r['kind']==method]
        entry['test_medians'][method]=float(np.median([r['selected']['test'] for r in chosen]))
        if method!='factor':entry['diagnostics'][method]=[r['diagnostics'] for r in chosen]
    for other in ('field','factor'):
        ratios=[next(r['selected']['test'] for r in main if r['seed']==seed and r['kind']=='gated')/
                next(r['selected']['test'] for r in main if r['seed']==seed and r['kind']==other) for seed in (4101,4102,4103)]
        entry['paired_ratios'][other]={'median':float(np.median(ratios)),'wins':int(sum(r<1 for r in ratios))}
    for method in ('field','gated'):
        r=[r for r in domainrows if r['seed']==4101 and r['kind']==method]
        entry['refinement'][method]=abs(r[0]['selected']['test']-r[1]['selected']['test'])
    entry['practical_pass']=all(v['median']<=.95 and v['wins']==3 for v in entry['paired_ratios'].values())
    summary[domain]=entry

decomposition={};replay_error=0.
for folder in sorted((DATA/'stage2_root_gate_diagnostics01').glob('fit_*')):
    r=read(folder/'result.json');sha(folder/'arrays.npz');arr=np.load(folder/'arrays.npz');a=arr['metrics']
    original=next(p for p in (DATA/'stage2_root_gate01').glob('fit_*') if (lambda t:t['domain']==r['domain'] and t['seed']==4101 and t['kind']=='field' and t['dt']==1/32)(json.loads((p/'result.json').read_text())))
    b=np.load(original/'arrays.npz')
    replay_error=max(replay_error,float(np.max(abs(arr['predictions']-b['predictions']))),float(np.max(abs(a[:,:7]-b['metrics']))))
    decomposition[r['domain']]={'positive_hidden':float(np.mean(a[:,3]>1e-10)),
        'positive_spatial':float(np.mean(a[:,7]>1e-10)),'positive_lag':float(np.mean(a[:,8]>1e-10)),
        'identity_error':float(np.max(abs(a[:,3]-a[:,7]-a[:,8]))),'last_relative_block':float(a[-1,10]),
        'sampled_sums':a[:,[3,7,8]].sum(0).tolist()}

# Frozen data identity, embedding and subject separation checks, no network access.
dataset={};dm=read(DATA/'stage2_data01/manifest.json')
for name,metadata in dm['datasets'].items():
    path=DATA/'stage2_data01'/f'{name}.npz';assert sha(path)==metadata['sha256'];a=np.load(path)
    assert not set(a['index_train'])&set(a['index_val'])
    if name=='har':
        sets=[set(a['subject_'+s]) for s in ('train','val','test')]
        assert not sets[0]&sets[1] and not sets[0]&sets[2] and not sets[1]&sets[2]
    dataset[name]={'norm_error':max(float(np.max(abs(np.linalg.norm(a['X_'+s],axis=1)-1))) for s in ('train','val','test')),
                   'label_rms':float(np.sqrt(np.mean(a['y_train']**2)))}
    for method,change in summary[name]['refinement'].items():assert change<.01*dataset[name]['label_rms']
for name,spec in dm['sources'].items():assert sha(DATA/'stage2_data01/raw'/name)==spec['sha256']

# Recompute the original twelve-solve oracle's preregistered scalar gates.
frozen=read(DATA/'stage2_challenge/finite_q_v2_20261002/results.json')
fine={(r['q'],r['epsilon']):r for r in frozen['rows'] if r['rtol']==1e-12}
coarse={(r['q'],r['epsilon']):r for r in frozen['rows'] if r['rtol']==1e-10}
normalized=[r['loss_derivative']/(r['epsilon']**2/36) for r in frozen['rows']]
oracle_tolerance=max(abs(fine[k]['normalized']-coarse[k]['normalized']) for k in fine)
assert all(r['success'] for r in frozen['rows']) and all(0.99<x<1.01 for x in normalized)
assert oracle_tolerance<1e-7
assert all(abs(fine[q,.01]['normalized']-1)<=.35*abs(fine[q,.02]['normalized']-1)+1e-7 for q in (1,2,4))

for name in ('STAGE2_CHALLENGE_THEORY.md','MODEL_RECONCILIATION.md','INPUT_FIELD_DERIVATION.md',
             'STAGE2_ROOT_GATE_PROTOCOL.md','STAGE2_DATA_PROTOCOL.md','stage2_data.py','stage2_root_gate_analyze.py'):
    sha(STUDY/name)
for path in (ROOT/'paper/main.tex',ROOT/'paper/results.tex',
             DATA/'stage2_challenge/finite_q_v2_20261002/check_finite_q.py',
             DATA/'stage2_challenge/finite_q_v2_20261002/results.json'):
    sha(path)
assert max(errors.values())<1e-9,errors
assert raw_error<2e-7 and gate_error<1e-6 and replay_error==0
output={'command':sys.argv,'script_sha256':sha(Path(__file__)),'cpu_seconds':time.process_time()-started,
    'environment':{'python':sys.version,'numpy':np.__version__,'torch':torch.__version__,'scipy':scipy.__version__,
                   'platform':platform.platform(),'threads':torch.get_num_threads()},
    'source_manifests':manifests,'certificate_errors':errors,'certificate_cases':cases,'gate_branches':sorted(branches),
    'initial_pca_commutator_max':pca_initial_commutator,'frozen_oracle_recomputed_tolerance_change':oracle_tolerance,
    'independent_scalar_odes':ode,'commutator_cases':commutation,'raw_test_rmse_error':raw_error,
    'recorded_derivative_identity_error':derivative_error,'gate_recompute_error':gate_error,
    'sampled_loss_increase_count':increases,'diagnostic_replay_error':replay_error,
    'datasets':dataset,'comparisons':summary,'decomposition':decomposition,'hashes':hashes}
(OUT/'results.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({k:v for k,v in output.items() if k not in ('hashes','source_manifests','commutator_cases')},indent=2))
