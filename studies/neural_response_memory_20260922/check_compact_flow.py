"""CPU equation checks; --gpu adds bounded n=2048 CUDA/legacy-basis checks."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import time
import zipfile
import numpy as np
import torch

from compact_flow import Flow, FrozenFlow
from run_compact_flow import dataset, resolve, run, summarize, load_npz
# Frozen old equations are a verification oracle only, never a runtime dependency.
HERE = Path(__file__).resolve().parent
sys.path.append(str(HERE/'legacy_experiments.zip'))
from activation_moment_engine import ActivationDenseEngine, ActivationMomentEngine


def main():
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float32)
    generator = torch.Generator().manual_seed(741)
    inputs = torch.randn((8, 2), generator=generator, dtype=torch.float64)
    labels = torch.tensor([1., -1.] * 4, dtype=torch.float64)
    checks, maximum = 0, 0.

    def close(actual, expected):
        nonlocal checks, maximum
        torch.testing.assert_close(actual, expected, atol=3e-12, rtol=3e-12)
        assert bool(torch.isfinite(actual).all())
        maximum = max(maximum, float((actual - expected).abs().max()))
        checks += 1

    def make(depth, activation, order=None):
        return Flow(inputs, labels, width=7, depth=depth, activation=activation,
                    order=order, seed=773, device='cpu', dtype=torch.float64)

    # Same initialization and evolving physical/moment coordinates as the
    # established three-layer implementation, with three simultaneous steps.
    for activation in ('relu', 'gelu', 'selu'):
        for order in (None, 1, 2, 3):
            new = make(3, activation, order)
            arguments = (2, 7, inputs, labels) if order is None else (2, 7, order, inputs, labels)
            kind = ActivationDenseEngine if order is None else ActivationMomentEngine
            old = kind(*arguments, activation=activation, seed=773, device='cpu', dtype=torch.float64)
            state = old.initial_state()
            assert len(new.state) == len(state.tensors())
            for index in range(4):
                for actual, expected in zip(new.state, state.tensors()):
                    assert actual.dtype == torch.float64 and actual.device.type == 'cpu'
                    close(actual, expected)
                close(new.predict(inputs), old.predict(state, inputs))
                before = [value.clone() for value in new.state]
                velocity, reference = new.rhs(), old.rhs(state)
                for actual, expected in zip(velocity, reference.tensors()):
                    close(actual, expected)
                for actual, expected in zip(new.state, before):
                    close(actual, expected)
                if index < 3:
                    new.step(.0003)
                    state = state.add_scaled(reference, .0003)

    custom = (lambda z: torch.tanh(z) + .05 * z,
              lambda z: 1 - torch.tanh(z).square() + .05)
    # Autograd is independent of the implementation's manual backward pass.
    for depth in (1, 2, 4):
        for activation in ('tanh', custom):
            model = make(depth, activation)
            phi = torch.tanh if activation == 'tanh' else custom[0]
            for _ in range(3):
                parameters = [value.detach().clone().requires_grad_(True) for value in model.state]
                hidden = phi(parameters[0] @ inputs.T)
                for matrix in parameters[1:-1]:
                    hidden = phi(matrix @ hidden)
                prediction = parameters[-1] @ hidden / model.n
                loss = (prediction - labels).square().mean()
                gradients = torch.autograd.grad(loss, parameters)
                close(model.predict(inputs), prediction.detach())
                mobilities = [model.n] + [1] * (depth - 1) + [model.n]
                for actual, gradient, mobility in zip(model.rhs(), gradients, mobilities):
                    close(actual, -mobility * gradient)
                model.step(.0003)

    # With no hidden-to-hidden link, moments cannot alter depth-one dynamics.
    for activation in ('relu', 'gelu', 'selu', custom):
        for order in (1, 3):
            dense, closure = make(1, activation), make(1, activation, order)
            for _ in range(3):
                close(dense.predict(inputs), closure.predict(inputs))
                d, c = dense.rhs(), closure.rhs()
                close(d[0], c[0])
                close(d[1], c[1])
                close(c[-1], (closure.predict(inputs) - labels).square().mean().sqrt())
                dense.step(.0003)
                closure.step(.0003)
    # Configured initialization must preserve the same muP gradient equations.
    # Independent PyTorch activations cover deep models and arbitrary input dimension.
    phis={'relu':torch.relu,'gelu':torch.nn.functional.gelu,
          'selu':torch.nn.functional.selu,'tanh':torch.tanh,
          'sigmoid':torch.sigmoid,'silu':torch.nn.functional.silu}
    x3=torch.randn((8,3),generator=generator,dtype=torch.float64)
    for depth in (1,4,20):
        for activation,phi in phis.items():
            model=Flow(x3,labels,width=7,depth=depth,activation=activation,
                       hidden_gain='unit_moment',readout_std=1.,seed=773,
                       device='cpu',dtype=torch.float64)
            parameters=[v.detach().clone().requires_grad_(True) for v in model.state]
            h=phi(parameters[0]@x3.T)
            for matrix in parameters[1:-1]:h=phi(matrix@h)
            pred=parameters[-1]@h/model.n
            gradients=torch.autograd.grad((pred-labels).square().mean(),parameters)
            close(model.predict(x3),pred.detach())
            for actual,g,mobility in zip(model.rhs(),gradients,[model.n]+[1]*(depth-1)+[model.n]):
                close(actual,-mobility*g)
            for order in (1,2,3):
                closure=Flow(x3,labels,width=7,depth=depth,activation=activation,
                             order=order,hidden_gain='unit_moment',readout_std=1.,seed=773,
                             device='cpu',dtype=torch.float64)
                close(closure.predict(x3),model.predict(x3))
                for _ in range(2):closure.step(.00001)
                h=phi(closure.w@x3.T)
                for i,matrix in enumerate(closure.matrices):
                    A,B=closure.moments[2*i:2*i+2]
                    correction=sum((2*k+1)*(A[k]@B[k].T) for k in range(order))
                    W=matrix-2*correction/(closure.M*closure.n*(1+closure.s))
                    h=phi(W@h)
                close(closure.predict(x3),closure.c@h/closure.n)
    # Frozen coefficients use the Euclidean core gradient and muP outer gradients.
    for kind in ('gaussian', 'orthogonal'):
        for depth in (1, 2, 4):
            for activation, phi in phis.items():
                model = FrozenFlow(x3, labels, kind=kind, ranks=3, width=7, depth=depth,
                                   activation=activation, device='cpu', dtype=torch.float64)
                bases = [b.clone() for b in model.bases]
                for _ in range(3):
                    parameters = [v.clone().requires_grad_(True) for v in model.state]
                    h = phi(parameters[0]@x3.T)
                    for i, core in enumerate(parameters[1:-1]):
                        matrix = bases[i+1]@core@bases[i].T/model.n
                        h = phi(matrix@h)
                    pred = parameters[-1]@h/model.n
                    gradients = torch.autograd.grad((pred-labels).square().mean(), parameters)
                    close(model.predict(x3), pred.detach())
                    for actual, g, mobility in zip(model.rhs(), gradients, [model.n]+[1]*(depth-1)+[model.n]): close(actual, -mobility*g)
                    model.step(.0003)
                    for before, after in zip(bases, model.bases): close(after, before)
    print(f'PASS: {checks} CPU assertions; max absolute discrepancy {maximum:.3g}')
    return dict(assertions=checks, maximum_absolute_error=maximum)


def check_data():
    from quick_normalized_stress import data as old_stress
    from quick_sphere_flow import sphere_data
    maximum = 0.
    for kind in ('circle', 'sphere'):
        for support in ('full', 'patch'):
            spec = dict(kind=kind, name=kind+'_'+support)
            spec.update(dict(span_degrees=90 if support == 'patch' else 360) if kind == 'circle' else dict(z_min=.5 if support == 'patch' else -1.))
            new, _ = dataset(spec); old = old_stress(spec['name'])
            for k, value in zip(('inputs','labels','test_inputs','test_labels','region'), old):
                np.testing.assert_allclose(new[k], value, atol=2e-14, rtol=2e-14)
                if value.dtype != bool: maximum = max(maximum, float(np.max(np.abs(new[k]-value))))
    for target in ('xy', 'xyz'):
        new, _ = dataset(dict(kind='sphere', name=target, sampling='normal', seed=20260925, target=target, samples=16))
        for k, value in zip(('inputs','labels','test_inputs','test_labels'), sphere_data(target,16)):
            np.testing.assert_array_equal(new[k], value)
    # Reproduce the original frozen MNIST panel from its official raw files.
    cache = HERE.parents[1]/'data/generated/neural_response_memory_20260922/mnist_data01'
    mnist = 'unavailable'
    if (cache/'prepared.npz').exists():
        new, _ = dataset(dict(kind='mnist', name='mnist', cache=str(cache/'raw_cache'), samples_per_class=500))
        old = load_npz(cache/'prepared.npz')
        for k in ('inputs','labels','test_inputs','test_labels','train_ids'): np.testing.assert_array_equal(new[k],old[k])
        np.testing.assert_array_equal(new['test_ids'],old['validation_ids'])
        mnist = '1000 training and 1984 test rows: bitwise identical'
    print('PASS: dataset reproduction;', mnist)
    return dict(maximum_toy_difference=maximum, mnist=mnist)


def check_runner():
    import contextlib
    import io
    raw = dict(device='cpu', model=dict(width=12, depth=2, activation='tanh',dtype='float64'),
               optimizer=dict(step=.01,max_steps=3,block=2,max_seconds=10),
               methods=[dict(kind='dense')]+[dict(kind='closure',order=p) for p in (1,2,3)]
                       +[dict(kind=k,order=1) for k in ('dictionary_old','dictionary_flow','gaussian','orthogonal')],
               datasets=[dict(kind='circle',name='circle',case='quadrant_pairs',queries=32)])
    config = resolve(raw)
    with tempfile.TemporaryDirectory() as tmp, contextlib.redirect_stdout(io.StringIO()):
        root = Path(tmp)/'results'; run(config,root,HERE)
        rows = summarize(root); assert len(rows) == 8
        dense = np.load(root/'circle/dense.npz')['test_prediction']
        for row in rows:
            query = np.load(root/'circle'/(row['model']+'.npz'))['test_prediction']
            np.testing.assert_allclose(row['test_rms_vs_dense'],np.sqrt(np.mean((query-dense)**2)),rtol=1e-14)
        no_dense = {**raw, 'methods':[dict(kind='closure',order=1)]}
        run(resolve(no_dense),Path(tmp)/'no_dense',HERE)
        assert summarize(Path(tmp)/'no_dense')[0]['test_rms_vs_dense'] is None
        changed = root/'circle/dense.npz'; changed.write_bytes(changed.read_bytes()+b'changed')
        try: summarize(root)
        except ValueError: pass
        else: raise AssertionError('Changed predictions accepted')
        for override in (dict(model={'width':0}),dict(optimizer={'step':0}),dict(methods=[dict(kind='dictionary_old',order=2)]),dict(methods=[dict(kind='dense'),dict(kind='dense',id='duplicate')])):
            try: resolve({**raw,**override})
            except ValueError: pass
            else: raise AssertionError('Invalid configuration accepted')
        try: dataset(dict(kind='circle',name='bad',frequncy=7))
        except ValueError: pass
        else: raise AssertionError('Dataset typo accepted')
    print('PASS: runner, saved metrics, missing dense, corruption and config validation')


def check_gpu(device):
    # Compare captured Euler to eager updates, including a final partial block.
    torch.cuda.set_device(device); torch.backends.cuda.matmul.allow_tf32=False
    records=[]; x=np.array([[1.,0.],[0.,1.],[-1.,0.],[0.,-1.]]);y=np.array([1.,-1.,-1.,1.])
    cases=[dict(kind='dense')]+[dict(kind='closure',order=p) for p in (1,2,3)]
    cases += [dict(kind=k,order=3) for k in ('dictionary_old','dictionary_flow','gaussian','orthogonal')]
    for method in cases:
        config=resolve(dict(device=device,model=dict(width=2048,depth=2,activation='tanh'),methods=[method],datasets=[dict(name='circle',kind='circle')]))
        from run_compact_flow import construct
        data=dict(inputs=x,labels=y)
        model=construct(config,method,data); reference=construct(config,method,data)
        before=[b.clone() for b in model.bases] if isinstance(model,FrozenFlow) else []
        fit=model.fit(step=1/64,target_rms=1e-20,max_seconds=30,max_steps=19,block=8)
        assert fit['steps']==19
        for _ in range(19): reference.step(1/64)
        maximum=0.
        for a,b in zip(model.state,reference.state):
            torch.testing.assert_close(a,b,atol=2e-6,rtol=2e-6)
            maximum=max(maximum,float((a-b).abs().max()))
        for a,b in zip(before,getattr(model,'bases',[])): assert torch.equal(a,b)
        records.append(dict(method=method,fit=fit,maximum_state_difference=maximum))
        print('PASS GPU',method,'fit seconds',round(fit['seconds'],3),'difference',maximum,flush=True)
        del model,reference
    # Original builders use CUDA: compare every supported dictionary order.
    root=HERE.parents[1]
    sys.path.insert(0,str(root/'studies/random_dictionary_learned_circle_20260920'))
    sys.path.insert(0,str(root/'studies/gradient_flow_probe_dictionary_20260921'))
    import scaling_dictionary, new_dictionary, new_dictionary_p45, new_dictionary_p7
    from pde.observable_torch_p1 import TensorState, ClosureEngine
    from frozen_dictionary import frozen_bases, OLD_RANKS
    dense=Flow(x,y,width=2048,depth=2,activation='tanh',device=device,dtype=torch.float64)
    initial=TensorState(dense.w,dense.c,dense.matrices[0])
    legacy_checks=[]
    for kind,orders in [('dictionary_old',list(OLD_RANKS)),('dictionary_flow',list(range(1,8))),('gaussian',list(OLD_RANKS)),('orthogonal',list(OLD_RANKS))]:
        for order in orders:
            actual=frozen_bases(dense.w,dense.matrices,dense.c,kind,order)
            if kind=='dictionary_flow':
                builder=new_dictionary if order<=3 else new_dictionary_p45 if order<=5 else new_dictionary_p7
                engine,state,_=builder.build(initial,order)
                expected=[engine.b1,engine.b2]
            else: expected=scaling_dictionary.dictionaries(initial,order,'ours' if kind=='dictionary_old' else kind)
            for a,b in zip(actual,expected): torch.testing.assert_close(a,b,atol=2e-10,rtol=2e-10)
            discrepancy=max(float((a-b).abs().max()) for a,b in zip(actual,expected))
            # Legacy core flow equivalence from the actual original producer.
            core=expected[1].T@(initial.M@expected[0])/dense.n
            old=ClosureEngine(expected[0],initial.w,expected[1],core,device=device,dtype=torch.float64)
            state=old.state(initial.w,initial.c,core)
            data=old.prepare_data(x,y)
            model=FrozenFlow(x,y,kind=kind,order=order,width=2048,depth=2,activation='tanh',device=device,dtype=torch.float64)
            for _ in range(2):
                reference=old.rhs(state,data)
                for a,b in zip(model.rhs(),(reference.w,reference.M,reference.c)): torch.testing.assert_close(a,b,atol=2e-10,rtol=2e-10)
                model.step(.001)
                state=TensorState(state.w+.001*reference.w,state.c+.001*reference.c,state.M+.001*reference.M)
            del model,old
            legacy_checks.append(dict(kind=kind,order=order,maximum_basis_difference=discrepancy))
        print('PASS original bases and equations:',kind,'orders',orders,flush=True)
    return dict(cuda_graph=records,legacy_dictionaries=legacy_checks,gpu=torch.cuda.get_device_name(device))


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--gpu');parser.add_argument('--out',type=Path)
    args=parser.parse_args();start=time.perf_counter()
    result=dict(cpu=main(),datasets=check_data());check_runner()
    if args.gpu: result['gpu']=check_gpu(args.gpu)
    result['seconds']=time.perf_counter()-start
    result['source_sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [HERE/n for n in ('compact_flow.py','frozen_dictionary.py','run_compact_flow.py','check_compact_flow.py')]}
    if args.out:
        args.out.parent.mkdir(parents=True,exist_ok=True)
        with args.out.open('x') as f: json.dump(result,f,indent=2)
