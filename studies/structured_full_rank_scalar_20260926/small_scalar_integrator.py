"""Bounded ODE integration for small aggregate model comparisons."""
import time
import numpy as np
from scipy.optimize import brentq
from cubic_scalar_ode import _ScalarRK45


class NumericalGate(Exception):
    pass


def integrate(rhs,initial,residual,blocks,*,target=.001,rtol=1e-8,atol=1e-10,
              time_cap=3000.,wall_seconds=10.,max_step=10.):
    started=time.monotonic()
    state=np.asarray(initial,dtype=float).copy()
    at=0.
    mse=float(np.mean(residual(state)**2))
    history=[(at,mse)]
    steps=nfev=0
    maxrise=0.
    reason='target' if mse<=target else 'time_cap'
    detail=None

    def function(t,s):
        nonlocal nfev
        if time.monotonic()-started>wall_seconds:
            raise NumericalGate('wall_limit')
        nfev+=1
        result=rhs(t,s)
        if not np.all(np.isfinite(result)):
            raise NumericalGate('nonfinite_rhs')
        return result

    try:
        if mse>target:
            solver=_ScalarRK45(function,0.,state,time_cap,first_step=.01,
                max_step=max_step,rtol=rtol,atol=atol,block_slices=blocks)
            while solver.status=='running':
                oldat,oldmse=at,mse
                solver.step()
                if solver.status=='failed':
                    reason='solver_failed'
                    break
                candidate=solver.y
                candidate_mse=float(np.mean(residual(candidate)**2))
                if not np.isfinite(candidate_mse) or not np.all(np.isfinite(candidate)):
                    raise NumericalGate('nonfinite_state')
                maxrise=max(maxrise,candidate_mse-oldmse)
                at,state,mse=float(solver.t),candidate.copy(),candidate_mse
                steps+=1
                if mse<=target:
                    interp=solver.dense_output()
                    at=brentq(lambda t:np.mean(residual(interp(t))**2)-target,
                              oldat,at,xtol=1e-12,rtol=8*np.finfo(float).eps)
                    state=interp(at)
                    mse=float(np.mean(residual(state)**2))
                    history.append((at,mse))
                    reason='target'
                    break
                history.append((at,mse))
    except (NumericalGate,np.linalg.LinAlgError,FloatingPointError) as error:
        reason='numerical_gate'
        detail=str(error)
    info=dict(stop_reason=reason,detail=detail,fitted=mse<=target*(1+1e-7),
              train_mse=mse,physical_time=at,steps=steps,nfev=nfev,
              max_loss_rise=maxrise,training_seconds=time.monotonic()-started,
              rtol=rtol,atol=atol,wall_seconds=wall_seconds,time_cap=time_cap)
    return state,info,np.asarray(history)
