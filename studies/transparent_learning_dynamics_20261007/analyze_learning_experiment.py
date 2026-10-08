"""Analyze preregistered dense runs and an initialization-only cubic clock."""
from pathlib import Path
import hashlib
import json

import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.integrate import cumulative_trapezoid, solve_ivp

from dense_learning_experiment import initialize, fields, rhs, observe, quadrature_constants


ROOT = Path('data/generated/transparent_learning_dynamics_20261007/beyond_initialization_v1')
SEEDS = (101, 202, 303, 404)


def constants(order=160):
    c = quadrature_constants(order)
    x,w = hermgauss(order)
    x,w = np.sqrt(2)*x,w/np.sqrt(np.pi)
    h = np.tanh(x); g=1-h*h
    tx = w @ (h*h*g*g)
    h = np.tanh(np.sqrt(c['sigma2'])*x); g=1-h*h
    tau=w @ (h*h*g*g)
    r0=3*c['beta']-2*c['alpha']
    c['kappa'] = float(2/3*((c['sigma2']+c['qx'])*(tau+c['nu']*c['beta'])
                              +r0*r0*tx+c['alpha']**4*c['qx']*c['sigma2']))
    c['tau'],c['tau_x'],c['r0'] = float(tau),float(tx),float(r0)
    return c


def cubic_clock(amplitude, time, c):
    sol=solve_ivp(lambda t,u:amplitude-c['nu']*u-c['kappa']*u**3,
                  (0,float(time[-1])),[0.],t_eval=time,rtol=1e-12,atol=1e-14)
    assert sol.success
    return sol.y[0]


def load_group(template):
    return [dict(np.load(ROOT/template.format(seed=s)/'trajectory.npz')) for s in SEEDS]


def vector(r):
    return np.column_stack((r['c1'][:,0,1]-r['c1'][0,0,1],
                            r['c2'][:,0,1]-r['c2'][0,0,1],r['f'][:,2]))


def additional_checks():
    state=initialize(19,987)
    state=state[:2]+(np.linspace(-.5,.3,19),)
    y=np.array([.6,-.6])
    v=rhs(state,y)
    o=observe(state,initialize(19,987),y,'full',None)
    # Metric gradient velocity is -D grad(loss), D=(n,1,n).
    energy=-(np.sum(v[0]**2)/19+np.sum(v[1]**2)+np.sum(v[2]**2)/19)
    eps=1e-6
    lp=np.mean((fields(tuple(a+eps*b for a,b in zip(state,v)))['f'][:2]-y)**2)
    lm=np.mean((fields(tuple(a-eps*b for a,b in zip(state,v)))['f'][:2]-y)**2)
    direct=(lp-lm)/(2*eps)
    energy_error=abs(energy-o['loss_derivative'])
    directional_error=abs(direct-o['loss_derivative'])
    assert energy_error<1e-12 and directional_error<1e-8
    for mode in ('frozen_middle','frozen_features'):
        vv=rhs(state,y,mode)
        assert np.all(vv[1]==0)
        if mode=='frozen_features':assert np.all(vv[0]==0)
    neg=state[:2]+(-state[2],)
    nv=rhs(neg,-y)
    sign_error=max(np.max(abs(nv[0]-v[0])),np.max(abs(nv[1]-v[1])),np.max(abs(nv[2]+v[2])))
    assert sign_error<1e-12
    # Readout-only trajectory versus its exact finite-width matrix exponential.
    rf=dict(np.load(ROOT/'frozen_features_n512_s101_a06'/'trajectory.npz'))
    k=rf['c2'][0,:2,:2]; lam,u=np.linalg.eigh(k)
    residual=(u @ (np.exp(-rf['time'][:,None]*lam)*(u.T@y)).T).T
    readout_error=np.max(abs(rf['f'][:,:2]-(y-residual)))
    assert readout_error<1e-8
    qdiff=max(abs(constants(100)[k]-constants(160)[k]) for k in constants(160))
    assert qdiff<1e-8
    return dict(energy_error=energy_error,directional_error=directional_error,
                sign_error=float(sign_error),readout_exact_error=float(readout_error),
                quadrature_100_160_max_difference=float(qdiff))


def main():
    output=ROOT/'analysis_v2'
    output.mkdir(exist_ok=False)
    c=constants()
    summary={'constants':c,'checks':additional_checks(),'dense':{},'clock':{},'refinement':{}}
    for tag in ('0075','015','06'):
        a=float({'0075':.075,'015':.15,'06':.6}[tag])
        runs=load_group(f'dense_n512_s{{seed}}_a{tag}')
        data=np.array([vector(r) for r in runs])
        time=runs[0]['time']; mean=data.mean(0); sem=data.std(0,ddof=1)/2
        u=cubic_clock(a,time,c)
        frozen=a*(1-np.exp(-c['nu']*time))/c['nu']
        pred=np.column_stack((-c['b1']*u*u,-c['b2']*u*u))
        naive=np.column_stack((-c['b1']*frozen*frozen,-c['b2']*frozen*frozen))
        measured=[]
        for r in runs:
            residual=a-(r['f'][:,0]-r['f'][:,1])/2
            clock=cumulative_trapezoid(residual,time,initial=0)
            measured.append(clock)
        measured=np.array(measured)
        endpoint_ratios=np.column_stack((data[:,-1,0]/(-c['b1']*measured[:,-1]**2),
                                          data[:,-1,1]/(-c['b2']*measured[:,-1]**2)))
        summary['dense'][tag]=dict(final_mean=mean[-1].tolist(),final_sem=sem[-1].tolist(),
                                  maximum_final_loss=float(max(r['loss'][-1] for r in runs)),
                                  passive_motion_rms=np.sqrt(np.mean([[r['motion1'][-1,2],r['motion2'][-1,2]] for r in runs],axis=0)).tolist(),
                                  gate_motion_bins=np.mean([r['gate_motion'][-1] for r in runs],axis=0).tolist())
        summary['clock'][tag]=dict(predicted_endpoint=pred[-1].tolist(),
                                  frozen_clock_endpoint=naive[-1].tolist(),
                                  max_abs_error=np.max(abs(pred-mean[:,:2]),axis=0).tolist(),
                                  max_error_over_final_change=(np.max(abs(pred-mean[:,:2]),axis=0)/abs(mean[-1,:2])).tolist(),
                                  frozen_max_error_over_final_change=(np.max(abs(naive-mean[:,:2]),axis=0)/abs(mean[-1,:2])).tolist(),
                                  measured_clock_endpoint_mean=float(measured[:,-1].mean()),
                                  predicted_clock_endpoint=float(u[-1]),
                                  measured_clock_feature_ratio_mean=endpoint_ratios.mean(0).tolist())
        if tag in ('015','06'):
            base=runs[0];fine=dict(np.load(ROOT/f'refine_n512_s101_a{tag}'/'trajectory.npz'))
            summary['refinement'][tag]={key:float(np.max(abs(base[key]-fine[key][::2]))) for key in ('f','c1','c2','kernel_blocks','motion1','motion2')}
    for mode in ('frozen_middle','frozen_features','affine_gates'):
        runs=load_group(f'{mode}_n512_s{{seed}}_a06')
        base=load_group('dense_n512_s{seed}_a06')
        endpoint=np.array([vector(r)[-1] for r in runs])
        diff=endpoint-np.array([vector(r)[-1] for r in base])
        summary['dense'][mode]=dict(final_mean=endpoint.mean(0).tolist(),
                                   final_sem=(endpoint.std(0,ddof=1)/2).tolist(),
                                   paired_difference_mean=diff.mean(0).tolist(),
                                   paired_difference_sem=(diff.std(0,ddof=1)/2).tolist())
    same=np.array([vector(r)[-1] for r in load_group('dense_n512_s{seed}_a06_same')])
    summary['dense']['same_labels']=dict(final_mean=same.mean(0).tolist(),final_sem=(same.std(0,ddof=1)/2).tolist())
    summary['provenance']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),Path(__file__).with_name('dense_learning_experiment.py'))}
    records=[json.loads(p.read_text()) for p in ROOT.glob('*/record.json')]
    summary['run_count']=len(records)
    summary['numerical_wall_seconds']=sum(r['wall_seconds'] for r in records)
    summary['maximum_peak_rss_kib']=max(r['peak_rss_kib'] for r in records)
    (output/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    make_plot(output,c)
    print(json.dumps(summary,indent=2))


def make_plot(output,c):
    # Pillow draws this data plot; matplotlib is unavailable in the environment.
    from PIL import Image, ImageDraw, ImageFont
    canvas=Image.new('RGB',(1600,1100),'white');draw=ImageDraw.Draw(canvas)
    fontpath='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
    font=ImageFont.truetype(fontpath,18);small=ImageFont.truetype(fontpath,15)
    titlefont=ImageFont.truetype(fontpath,21)
    panels=[[],[],[],[]]
    for tag,a,col in (('0075',.075,'#2674ac'),('015',.15,'#c15a25'),('06',.6,'#56833b')):
        runs=load_group(f'dense_n512_s{{seed}}_a{tag}')
        t=runs[0]['time']; d=np.array([vector(r) for r in runs]);mean=d.mean(0)
        u=cubic_clock(a,t,c)
        panels[0].append((t,-mean[:,0],col,f'dense Y={a:g}',False))
        panels[0].append((t,c['b1']*u*u,col,'',True))
        measured=[]
        for r in runs:
            measured.append(cumulative_trapezoid(a-(r['f'][:,0]-r['f'][:,1])/2,t,initial=0))
        panels[1].append((np.mean(np.array(measured)**2,axis=0),-mean[:,0],col,f'Y={a:g}',False))
    xx=np.linspace(0,1.55,200)
    panels[1].append((xx,c['b1']*xx,'#333333','initial Gaussian coefficient',True))
    for (mode,label),col in zip((('dense','Full tanh'),('frozen_middle','Middle frozen'),('frozen_features','Readout only'),('affine_gates','Local-affine control')),('#2674ac','#c15a25','#888888','#56833b')):
        runs=load_group(f'{mode}_n512_s{{seed}}_a06')
        panels[2].append((runs[0]['time'],np.mean([r['f'][:,2] for r in runs],0),col,label,False))
    runs=load_group('dense_n512_s{seed}_a06')
    k=np.mean([r['kernel_blocks'] for r in runs],0)
    for b,(label,col) in enumerate(zip(('Readout features','Middle-weight learning','First-layer learning'),('#2674ac','#c15a25','#56833b'))):
        eig=(k[:,b,0,0]+k[:,b,1,1]-2*k[:,b,0,1])/2
        panels[3].append((runs[0]['time'],eig,col,label,False))
    titles=('Cubic-clock approximation: dashed, no trajectory fit',
            'Diagnostic collapse using the measured residual clock',
            'Passive input: no validation label used',
            'Contributions to fitting the opposite-label mode')
    ylabels=('Minus first-layer cross-feature change',)*2+('Passive prediction, Y=0.6','Tangent-kernel contribution')
    xlabels=('Training time','Squared accumulated signed residual','Training time','Training time')
    for idx,curves in enumerate(panels):
        ox,oy=(idx%2)*800,(idx//2)*550
        left,right,top,bottom=ox+95,ox+755,oy+100,oy+410
        xmax=max(float(np.max(xx)) for xx,_,_,_,_ in curves)
        ymax=max(float(np.max(yy)) for _,yy,_,_,_ in curves)*1.08
        draw.text((ox+40,oy+18),titles[idx],fill='#222222',font=titlefont)
        draw.text((left,oy+58),ylabels[idx],fill='#444444',font=font)
        for j in range(5):
            xv=j*xmax/4;yv=j*ymax/4
            px=left+(right-left)*j/4;py=bottom-(bottom-top)*j/4
            draw.line((px,top,px,bottom),fill='#e8e8e8',width=1)
            draw.line((left,py,right,py),fill='#e8e8e8',width=1)
            draw.text((px-12,bottom+10),f'{xv:.3g}',font=small,fill='#444444')
            draw.text((ox+30,py-8),f'{yv:.3g}',font=small,fill='#444444')
        draw.line((left,top,left,bottom,right,bottom),fill='#555555',width=2)
        legend=0
        for xx,yy,col,label,dashed in curves:
            points=[(left+(right-left)*x/xmax,bottom-(bottom-top)*y/ymax) for x,y in zip(xx,yy)]
            if dashed:
                for j in range(0,len(points)-1,6):draw.line(points[j:j+4],fill=col,width=3)
            else:draw.line(points,fill=col,width=3)
            if label:
                lx=left+(legend%2)*330;ly=oy+465+(legend//2)*28
                draw.line((lx,ly+9,lx+25,ly+9),fill=col,width=3)
                draw.text((lx+33,ly),label,font=small,fill='#333333');legend+=1
        draw.text((left+190,bottom+36),xlabels[idx],font=font,fill='#333333')
    draw.text((50,1070),'Four dense seeds, width 512. Curves are empirical means, not error certificates.',font=small,fill='#555555')
    canvas.save(output/'learning_mechanisms.png')


if __name__=='__main__':main()
