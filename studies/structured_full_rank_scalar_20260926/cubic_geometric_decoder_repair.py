"""Frozen passive endpoint transports; no scalar or dense training."""
from pathlib import Path
import hashlib
import json
import time
import numpy as np
from cubic_scalar_ode import ScalarModel, QueryCoefficients, _initial_responses, _initial_fields


def query_slices(w, W, inputs, queries, batch_size=16):
    """Return separate A[x,a,b,c], B[x,a,b,c] initial response slices."""
    first, second, q0, d0, gamma, beta = _initial_responses(w, W, inputs)
    m, n = second.shape
    A = np.empty((len(queries), m, m, m))
    B = np.empty_like(A)
    dot, pg = inputs@inputs.T, first@first.T/n
    for start in range(0, len(queries), batch_size):
        stop = min(len(queries), start+batch_size)
        X = queries[start:stop]
        p, h, q, d = _initial_fields(w, W, X)
        length = len(X)
        ga = d0[None,:,:]*h[:,None,:]
        ba = ((ga.reshape(length*m,n)@W).reshape(length,m,n)*q0[None,:,:])
        gb = d[:,None,:]*second[None,:,:]
        bb = ((gb.reshape(length*m,n)@W).reshape(length,m,n)*q[:,None,:])
        for dest, g, b, first_cross, input_cross in (
            (A,ga,ba,pg[None,:,:],dot[None,:,:]),
            (B,gb,bb,(p@first.T/n)[:,None,:],(X@inputs.T)[:,None,:])):
            dest[start:stop] = (
                (b.reshape(length*m,n)@beta.reshape(m*m,n).T/n).reshape(length,m,m,m)
                *input_cross[:,:,:,None]
                +(g.reshape(length*m,n)@gamma.reshape(m*m,n).T/n).reshape(length,m,m,m)
                *first_cross[:,:,:,None])
    return A, B


def geometric_predictions(model, state, coeff, B):
    r,z,J,_ = model.unpack(state)
    _,M,N = model.kernel(z,J)
    f0 = model.cubic_prediction(state,coeff)
    D = model.labels+r-model.cubic_prediction(state)
    b = model.alpha**2*np.einsum('xibc,bc->xi',B,J)
    tangent = model.initial_gram+M+M.T+N
    tangent_query = coeff.cross_gram+model.alpha**2*np.einsum('xabc,bc->xa',coeff.cubic,J)
    variants = {}
    for name,matrix,rows in (
        ('moving_features',model.initial_gram+M.T,coeff.cross_gram+b),
        ('cubic_tangent',tangent,tangent_query)):
        condition = float(np.linalg.cond(matrix))
        minimum = float(np.linalg.eigvalsh(matrix)[0]) if name=='cubic_tangent' else None
        record = dict(condition=condition,minimum_eigenvalue=minimum)
        if not np.isfinite(condition) or condition>1e10 or (minimum is not None and minimum<=0):
            record['status']='conditioning_failure'
            variants[name]=(None,record)
            continue
        correction = rows@np.linalg.solve(matrix,D)
        prediction = f0+correction
        record.update(status='ok',correction_circle_rms=float(np.sqrt(np.mean(correction[:256]**2))))
        variants[name]=(prediction,record)
    return variants


def main():
    started = time.monotonic()
    study = Path(__file__).resolve().parent
    root = study.parent.parent
    source = root/'data/generated/structured_full_rank_scalar_20260926/cubic_scalar_20260930'
    output = root/'data/generated/structured_full_rank_scalar_20260926/cubic_feedback_repair_20260930/geometric_decoder'
    output.mkdir(parents=True,exist_ok=False)
    manifest = {'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                'protocol_sha256':hashlib.sha256((study/'CUBIC_FEEDBACK_REPAIR_ROUTE_20260930.md').read_bytes()).hexdigest(),
                'training_runs':0,'budget_seconds':20,'variants':['moving_features','cubic_tangent']}
    (output/'manifest.json').write_text(json.dumps(manifest,indent=2))
    cases = json.loads((source/'summary.json').read_text())['results']
    n = 1024
    w = np.random.default_rng(np.random.SeedSequence([1,1])).normal(size=(n,2))
    W = np.random.default_rng(np.random.SeedSequence([1,101])).normal(size=(n,n))/np.sqrt(n)
    records=[]
    for case in cases:
        task=case['task']
        data=np.load(source/(task+'.npz'))
        angles=data['train_angles'][case['representatives']]
        U=np.c_[np.cos(angles),np.sin(angles)]
        all_angles=np.r_[data['angles'],data['train_angles']]
        X=np.c_[np.cos(all_angles),np.sin(all_angles)]
        model=ScalarModel(data['model_labels'],data['initial_gram'],data['response_gram'])
        coeff=QueryCoefficients(data['query_gram'],data['query_cubic'])
        state=data['state']
        H=_initial_fields(w,W,U)[1]
        assert np.max(abs(H@H.T/n-model.initial_gram))<1e-12
        assert np.max(abs(model.predict(state,coeff)[:256]-data['scalar']))<1e-10
        A,B=query_slices(w,W,U,X)
        C=A+B+B.transpose(0,2,1,3)+B.transpose(0,2,3,1)
        assert np.max(abs(C-coeff.cubic))<1e-12
        variants=geometric_predictions(model,state,coeff,B)
        rec={'task':task,'original_rms':float(case['scalar_dense_rms']),'variants':{}}
        arrays={'angles':data['angles'],'dense':data['dense'],'original':data['scalar'],
                'query_A':A,'query_B':B}
        aliases=256+np.asarray(case['representatives'])
        target=model.labels+state[:model.m]
        for name,(prediction,meta) in variants.items():
            if prediction is not None:
                error=float(np.max(abs(prediction[aliases]-target)))
                valid=np.all(np.isfinite(prediction)) and error<=1e-8
                meta.update(status='ok' if valid else 'alias_or_finite_failure',alias_max_abs=error,
                            circle_rms=float(np.sqrt(np.mean((prediction[:256]-data['dense'])**2))))
                arrays[name]=prediction
            rec['variants'][name]=meta
        records.append(rec)
        np.savez_compressed(output/(task+'.npz'),**arrays)
        (output/'results.partial.json').write_text(json.dumps(records,indent=2))
        print(task,rec['original_rms'],{k:v.get('circle_rms',v['status']) for k,v in rec['variants'].items()},flush=True)
        if time.monotonic()-started>20:
            raise RuntimeError('Frozen 20-second budget exceeded')
    result={'results':records,'elapsed_seconds':time.monotonic()-started,'training_runs':0}
    (output/'results.json').write_text(json.dumps(result,indent=2))
    print('seconds',result['elapsed_seconds'],flush=True)


if __name__=='__main__':
    main()
