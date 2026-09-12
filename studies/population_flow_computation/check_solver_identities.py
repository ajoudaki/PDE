"""Independent finite algebra checks. No initialized training trajectory is run."""
import argparse
import copy
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import sys
import time
import uuid

import numpy as np
from numpy.testing import assert_allclose, assert_array_equal
from scipy.special import roots_hermitenorm

ROOT = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
HERE = args.output.resolve()
assert HERE.is_relative_to((ROOT/'data/generated/population_flow_computation').resolve())
HERE.mkdir(parents=True, exist_ok=False)
SOURCE = ROOT / 'studies/population_flow_computation/directional_solver.py'
EXPECTED = 'eef9c3b2d039d1911d036c068ef52708681f921961d21c73e2b5c999fc9dee23'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == EXPECTED
spec = importlib.util.spec_from_file_location('audit_directional_solver', SOURCE)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
records = {}


def check(name, actual, expected, atol=2e-12):
    assert_allclose(actual, expected, rtol=2e-12, atol=atol)
    records[name] = float(np.max(np.abs(np.asarray(actual)-np.asarray(expected)), initial=0))


def phi(x):
    return np.tanh(x)


def first(x):
    return 1-phi(x)**2


def second(x):
    return -2*phi(x)*first(x)


def polynomial_checks():
    # Degree <= 4 Gaussian expectations; order 5 is exact in each latent coordinate.
    x, wt = roots_hermitenorm(5)
    wt = wt/np.sqrt(2*np.pi)
    points = np.array(list(itertools.product(x, repeat=2)))
    weights = np.array([a*b for a,b in itertools.product(wt, repeat=2)])
    for name, transform in [('correlated', np.array([[1., 0.], [.4, .8]])),
                            ('singular', np.array([[1., 0.], [2., 0.]]))]:
        z = points @ transform.T
        a,b = z.T
        f = a*a*b+a*b*b+2*a
        jac = np.column_stack((2*a*b+b*b+2, a*a+2*a*b))
        covariance = transform @ transform.T
        check(name+'_stein', (weights[:,None]*z*f[:,None]).sum(0),
              covariance @ (weights[:,None]*jac).sum(0))
    # Wg=xi; u=xi^2+a xi; W*u=zeta+a g; h=(W*u)^2+b(W*u).
    # E[u']=a and E[partial_zeta h]=b. Reusing W gives W h=xi_h+b u.
    a,b = .6,-.7
    g,zeta = points[:,0], points[:,1]*np.sqrt(3+a*a)
    q = zeta+a*g
    h = q*q+b*q
    variance_q = 3+2*a*a
    check('reused_polynomial_forward_response', np.sum(weights*(2*q+b)), b)
    check('reused_polynomial_forward_cross', np.sum(weights*h*g), a*b)
    check('reused_polynomial_forward_variance', np.sum(weights*h*h),
          3*variance_q**2+b*b*variance_q)
    check('reused_polynomial_adjoint_response', np.sum(wt*(2*x+a)), a)


def frozen_tanh_checks():
    # Two old and two current sources per orientation: all 2^8 sign vectors.
    signs = np.array(list(itertools.product((-1.,1.), repeat=8)))
    repeat = len(signs)
    p = 3*repeat
    def expand(x):
        return np.repeat(np.asarray(x, dtype=float), repeat, axis=0)
    config = module.SolverConfig(p, .07, .13, 923, [[1.,0.],[1.,0.]], [.2,.8], [.4,-.3])
    solver = module.DirectionalSolver(config)
    omega = config.h*solver.weights
    probes = np.tile(signs, (3,1))/np.sqrt(np.tile(omega,4))
    rmold, rmnew, rpold, rpnew = np.split(probes, 4, axis=1)
    g = expand([[.2,-.1],[-.4,.3],[.7,.15]])
    c0 = expand([.3,-.2,.4])
    gamma0 = np.array([.035,-.024])
    hold = phi(g @ solver.u.T)
    lp = np.linalg.cholesky(hold.T@hold/p+config.noise**2*np.eye(2))
    ep = expand([[.1,-.4],[.5,.25],[-.3,.2]])
    bp = ep@lp.T
    dold = c0[:,None]*first(bp)
    lm = np.linalg.cholesky(dold.T@dold/p+config.noise**2*np.eye(2))
    em = expand([[.2,.1],[-.25,.3],[.4,-.15]])
    bm = em@lm.T
    b0 = np.diag(np.mean(c0[:,None]*second(bp),axis=0))
    q0 = bm+hold@b0
    w = g+((first(g@solver.u.T)*q0)*gamma0)@solver.u
    c = c0+phi(bp)@gamma0
    # Full source Jacobians, derived analytically from the supplied first graph.
    jw = first(g@solver.u.T)[:,:,None]*gamma0[None,:,None]*solver.u[None,:,:]
    jc = gamma0[None,:]*first(bp)
    jdold = np.zeros((p,2,2))
    jdold[:,0,0] = c0*second(bp[:,0])
    jdold[:,1,1] = c0*second(bp[:,1])
    solver.g, solver.w, solver.c = g,w,c
    solver.v_w = np.einsum('pk,pkd->pd',rmold,jw)
    solver.v_c = np.sum(rpold*jc,axis=1)
    solver.H,solver.D = hold,dold
    solver.Hdot = np.zeros_like(hold)
    solver.Ddot = np.einsum('pkl,pl->pk',jdold,rpold)
    solver.Rminus,solver.Rplus = rmold,rpold
    solver.Eminus,solver.Eplus = em,ep
    solver.Bminus,solver.Bplus = bm,bp
    solver.Lminus,solver.Lplus = lm,lp
    solver.gamma,solver.omega = gamma0,omega
    solver.steps = 1
    solver.call_times = np.zeros(2)
    solver.call_directions = solver.u.copy()
    solver.training_predictions = np.zeros((1,2))
    solver.training_residuals = -solver.labels[None,:].copy()
    solver.step_response_max = np.array([np.max(np.abs(b0))])
    solver.step_minimum_schur = np.full((1,2),config.noise**2)
    solver.step_floor_allowance = np.zeros((1,2))
    epnew = expand([[-.2,.15],[.4,-.35],[.25,.3]])
    emnew = expand([[.3,-.2],[-.1,.25],[.35,-.4]])
    solver._normal = lambda name: {'plus_gaussian':epnew,'minus_gaussian':emnew}[name].copy()
    solver._probe = lambda name: {'plus_probe':rpnew,'minus_probe':rmnew}[name].copy()
    # Pure proposed update on synthetic coordinates, never committed as a step.
    updated = solver._prepare_step()
    h = phi(w@solver.u.T)
    jh = first(w@solver.u.T)[:,:,None]*np.einsum('pkd,ad->pak',jw,solver.u)
    alpha = np.mean(jh,axis=0).T
    check('tanh_weighted_alpha', (omega[:,None]*rmold.T)@(first(w@solver.u.T)*(solver.v_w@solver.u.T))/p, alpha)
    fcoef = alpha+gamma0[:,None]*(hold.T@h/p)
    hall = np.hstack((hold,h))
    dense_lp = np.linalg.cholesky(hall.T@hall/p+config.noise**2*np.eye(4))
    bplus = np.hstack((ep,epnew))@dense_lp.T
    z = bplus[:,2:]+dold@fcoef
    jzold = np.einsum('pql,qa->pal',jdold,fcoef)
    d = c[:,None]*first(z)
    jd_old = first(z)[:,:,None]*jc[:,None,:]+c[:,None,None]*second(z)[:,:,None]*jzold
    beta = np.mean(jd_old,axis=0).T
    beta_now = np.diag(np.mean(c[:,None]*second(z),axis=0))
    bcoef = np.vstack((beta+gamma0[:,None]*(dold.T@d/p),beta_now))
    check('tanh_D_and_old_response', updated['D'][:,2:],d)
    actual_old_tangent = updated['Ddot'][:,2:]-c[:,None]*second(z)*rpnew
    check('tanh_weighted_old_beta', (omega[:,None]*rpold.T)@actual_old_tangent/p,beta)
    all_d = np.hstack((dold,d))
    dense_lm = np.linalg.cholesky(all_d.T@all_d/p+config.noise**2*np.eye(4))
    bminus = np.hstack((em,emnew))@dense_lm.T
    q = bminus[:,2:]+hall@bcoef
    prediction = np.mean(c[:,None]*phi(z),axis=0)
    gamma = -2*omega*(prediction-solver.labels)
    check('tanh_exact_model_gamma', updated['gamma'][2:],gamma)
    check('tanh_forward_source_reuse',updated['Bplus'],bplus)
    check('tanh_reverse_source_reuse',updated['Bminus'],bminus)
    check('tanh_model_w_update',updated['w'],w+((first(w@solver.u.T)*q)*gamma)@solver.u)
    check('tanh_model_c_update',updated['c'],c+phi(z)@gamma)
    zdot = rpnew+np.einsum('pal,pl->pa',jzold,rpold)
    hdot = np.einsum('pal,pl->pa',jh,rmold)
    qdot = rmnew+hdot@beta_now
    expected_vw = solver.v_w+((second(w@solver.u.T)*(solver.v_w@solver.u.T)*q+first(w@solver.u.T)*qdot)*gamma)@solver.u
    expected_vc = solver.v_c+(first(z)*zdot)@gamma
    check('tanh_full_source_jacobian_lower',updated['v_w'],expected_vw)
    check('tanh_full_source_jacobian_upper',updated['v_c'],expected_vc)
    # Independent complex-step evaluation of the entire two-call frozen graph.
    eps = 1e-30
    def frozen_graph():
        xip = bp.astype(complex)+1j*eps*rpold
        zetap = bm.astype(complex)+1j*eps*rmold
        old_d = c0[:,None]*first(xip)
        new_w = g+((first(g@solver.u.T)*(zetap+hold@b0))*gamma0)@solver.u
        new_c = c0+phi(xip)@gamma0
        new_h = phi(new_w@solver.u.T)
        new_z = bplus[:,2:]+1j*eps*rpnew+old_d@fcoef
        new_q = bminus[:,2:]+1j*eps*rmnew+np.hstack((hold,new_h))@bcoef
        return (new_w+((first(new_w@solver.u.T)*new_q)*gamma)@solver.u,
                new_c+phi(new_z)@gamma)
    complex_w,complex_c = frozen_graph()
    check('tanh_complex_step_lower',updated['v_w'],complex_w.imag/eps)
    check('tanh_complex_step_upper',updated['v_c'],complex_c.imag/eps)
    # Adversarially alias current plus signs to old ones. Pointwise removal
    # and the analytic current diagonal must leave the physical proposal fixed.
    original_probe = solver._probe
    aliased_plus = rpold[:,::-1]*np.sqrt(omega[::-1]/omega)
    solver._probe = lambda name: (aliased_plus if name=='plus_probe' else rmnew).copy()
    try:
        aliased_update = solver._prepare_step()
    finally:
        solver._probe = original_probe
    check('pointwise_current_source_removal_w',aliased_update['w'],updated['w'])
    check('pointwise_current_source_removal_c',aliased_update['c'],updated['c'])
    check('pointwise_current_source_removal_lower_tangent',aliased_update['v_w'],updated['v_w'])
    # Existing sources and factors are preserved byte-for-byte in the proposal.
    for name in ('H','D','Eplus','Eminus','Bplus','Bminus','Lplus','Lminus'):
        old = getattr(solver,name)
        assert_array_equal(updated[name][:old.shape[0],:old.shape[1]],old)
    records['prefix_array_checks'] = 8
    # Clean passive mean/covariance versus dense conditional-normal formulas.
    query = [[1.,0.],[1.,0.],[0.,1.]]
    qh,shift,mean,variance,_ = solver._passive_fields(query)
    cross = hold.T@qh/p
    old_cov = hold.T@hold/p+config.noise**2*np.eye(2)
    check('passive_clean_mean',mean,bp@np.linalg.solve(old_cov,cross))
    check('passive_clean_variance',variance,np.mean(qh*qh,axis=0)-np.sum(cross*np.linalg.solve(old_cov,cross),axis=0))
    before = {name:getattr(solver,name).copy() for name in solver.array_names}
    before_rng = solver.rng_state()
    pair = solver.paired_hidden_draws(query,draws=2,seed=812)
    all_fields = np.hstack((phi(g@np.asarray(query).T),qh))
    ccross = hold.T@all_fields/p
    check('passive_joint_clean_covariance',pair['conditional_covariance'],all_fields.T@all_fields/p-ccross.T@np.linalg.solve(old_cov,ccross))
    for name in ('initial_preactivation','current_preactivation','upper_D','lower_Q'):
        assert_array_equal(pair[name][:,:,0],pair[name][:,:,1])
    records['duplicate_passive_action_checks'] = 4
    for name in solver.array_names:
        assert_array_equal(getattr(solver,name),before[name])
    assert solver.rng_state() == before_rng
    # Control only the fresh query innovations to evaluate the reverse mean
    # exactly. The plus coordinates repeat across all signs for each fixed
    # source tuple; complete sign averaging then returns each old partial.
    factory = np.random.default_rng
    factories = []
    class QueryInnovations:
        def __init__(self, plus):
            self.plus = plus
        def standard_normal(self, shape):
            if not self.plus:
                return np.zeros(shape)
            ndraws,nrows,ncols = shape
            fixed = np.sin(np.arange(ndraws*3*ncols).reshape(ndraws,3,ncols)+.3)
            return np.repeat(fixed,repeat,axis=1)
    def query_factory(seed):
        factories.append(seed)
        return QueryInnovations(len(factories)==1)
    try:
        np.random.default_rng = query_factory
        controlled_pair = solver.paired_hidden_draws(query,draws=2,seed=814)
    finally:
        np.random.default_rng = factory
    query_u = np.asarray(query)
    query_jh = first(w@query_u.T)[:,:,None]*np.einsum('pkd,ad->pak',jw,query_u)
    query_f = np.mean(query_jh,axis=0).T+gamma0[:,None]*(hold.T@qh/p)
    query_jzold = np.einsum('pql,qa->pal',jdold,query_f)
    reverse_old_cov = dold.T@dold/p+config.noise**2*np.eye(2)
    for draw_index in range(2):
        query_z = controlled_pair['current_preactivation'][draw_index]
        query_d = c[:,None]*first(query_z)
        query_jd = first(query_z)[:,:,None]*jc[:,None,:]+c[:,None,None]*second(query_z)[:,:,None]*query_jzold
        query_beta = np.mean(query_jd,axis=0).T
        query_beta_current = np.mean(c[:,None]*second(query_z),axis=0)
        dcross = dold.T@query_d/p
        source_mean = bm@np.linalg.solve(reverse_old_cov,dcross)
        expected_q = source_mean+hold@(query_beta+gamma0[:,None]*dcross)+qh*query_beta_current
        check('passive_D_full_source_formula_'+str(draw_index),controlled_pair['upper_D'][draw_index],query_d)
        check('passive_Q_full_source_formula_'+str(draw_index),controlled_pair['lower_Q'][draw_index],expected_q)
    # Synthetic complete-state serialization, no new physical step on load.
    checkpoint = HERE/('synthetic_checkpoint_'+uuid.uuid4().hex[:12]+'.npz')
    solver.save(checkpoint)
    restored = module.DirectionalSolver.load(checkpoint)
    for name in solver.array_names:
        assert_array_equal(getattr(restored,name),getattr(solver,name))
    assert restored.rng_state() == before_rng
    for stream in solver.stream_names:
        assert_array_equal(restored.rngs[stream].standard_normal(7),solver.rngs[stream].standard_normal(7))
    records['checkpoint_array_checks'] = len(solver.array_names)
    records['checkpoint_rng_stream_checks'] = len(solver.stream_names)
    records['synthetic_checkpoint_bytes'] = checkpoint.stat().st_size
    records['synthetic_checkpoint_path'] = str(checkpoint)
    records['sign_vectors_enumerated'] = repeat
    records['fixed_source_tuples'] = 3
    records['maximum_representative_rows'] = p
    records['training_trajectories'] = 0


started = time.perf_counter()
polynomial_checks()
frozen_tanh_checks()
records.update(status='all_checks_passed',source_sha256=EXPECTED,wall_seconds=time.perf_counter()-started)
(HERE/'results.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records,indent=2))
