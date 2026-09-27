// Genuine fixed-grid Eulerian histogram for the folded k=1,H=1 one-input law.
// Build: g++ -O3 -std=c++17 -fPIC -shared -fopenmp histogram_one_input.cpp -o libhistogram_one_input.so
// Coordinates in C order: (g,x,a,c,b), with b fastest; a=-A, b=B/L.
// No moving representatives, sampled RHS, pruning, or variable grid are used.
#include <algorithm>
#include <chrono>
#include <cmath>
#include <cstddef>
#include <cstdio>
#include <cstring>
#include <limits>
#include <new>
#include <vector>

namespace {
using Clock = std::chrono::steady_clock;
constexpr double GMAX=5., XMAX=6., AMAX=3., CMAX=4.;

struct Summary {
    double f=0., rho=0., S=0., D=0., mass=0., minimum=0., cap=0.;
};

struct Histogram {
    int ng,nx,na,nc,nb,threads;
    std::size_t size,rows,sx,sa,sc;
    double hx,ha,hc,hb;
    std::vector<double> gs,xs,as,cs,bs,h1,phi1,tx,ta,tc;
    std::vector<double> h2,phi2,cmarg;

    static std::vector<double> axis(int n,double maximum) {
        std::vector<double> v(n);
        for(int i=0;i<n;++i) v[i]=maximum*i/(n-1);
        return v;
    }
    static std::vector<double> taper(int n) {
        std::vector<double> v(n);
        for(int i=0;i<n;++i)
            v[i]=std::max(0.,std::min(1.,5.*(1.-double(i)/(n-1))));
        return v;
    }
    Histogram(int ng_,int nx_,int na_,int nc_,int nb_,int nt)
        : ng(ng_),nx(nx_),na(na_),nc(nc_),nb(nb_),threads(std::max(1,nt)),
          size(std::size_t(ng)*nx*na*nc*nb),rows(std::size_t(ng)*nx*na),
          sx(std::size_t(na)*nc*nb),sa(std::size_t(nc)*nb),sc(nb),
          hx(XMAX/(nx-1)),ha(AMAX/(na-1)),hc(CMAX/(nc-1)),hb(1./(nb-1)),
          gs(axis(ng,GMAX)),xs(axis(nx,XMAX)),as(axis(na,AMAX)),
          cs(axis(nc,CMAX)),bs(axis(nb,1.)),h1(nx),phi1(nx),
          tx(taper(nx)),ta(taper(na)),tc(taper(nc)),h2(rows),phi2(rows),cmarg(rows) {
        for(int i=0;i<nx;++i) {
            h1[i]=std::tanh(xs[i]);
            phi1[i]=1.-h1[i]*h1[i];
        }
    }

    Summary evaluate(const double* p,double label) {
        double S=0.,mass=0.,minimum=std::numeric_limits<double>::infinity(),cap=0.;
        #pragma omp parallel for num_threads(threads) schedule(static) reduction(+:S,mass,cap) reduction(min:minimum)
        for(std::size_t row=0;row<rows;++row) {
            const int ia=int(row%na), ix=int((row/na)%nx);
            const bool fixedcap=double(ix)/(nx-1)>=.8 || double(ia)/(na-1)>=.8;
            double csum=0.,bsum=0.;
            const std::size_t base=row*sa;
            for(int ic=0;ic<nc;++ic) {
                const bool incap=fixedcap || double(ic)/(nc-1)>=.8;
                double c_row_mass=0.;
                for(int ib=0;ib<nb;++ib) {
                    const double v=p[base+std::size_t(ic)*nb+ib];
                    c_row_mass+=v;
                    bsum+=bs[ib]*v;
                    mass+=v;
                    minimum=std::min(minimum,v);
                    if(incap) cap+=v;
                }
                csum+=cs[ic]*c_row_mass;
            }
            cmarg[row]=csum;
            S+=h1[ix]*bsum;
        }
        double f=0.,D=0.;
        #pragma omp parallel for num_threads(threads) schedule(static) reduction(+:f,D)
        for(std::size_t row=0;row<rows;++row) {
            const int ia=int(row%na),ix=int((row/na)%nx),ig=int(row/(std::size_t(na)*nx));
            const double value=std::tanh(gs[ig]*h1[ix]+2.*as[ia]*S);
            h2[row]=value;
            phi2[row]=std::max(0.,1.-value*value);
            f+=cmarg[row]*value;
            D+=as[ia]*cmarg[row]*phi2[row];
        }
        return {f,std::abs(f-label),S,D,mass,minimum,cap};
    }

    // Positive drift is tapered only in the artificial x,a,c cutoff zones.
    static double limited(double velocity,double tap) {
        return velocity>0. ? velocity*tap : velocity;
    }

    Summary rhs(const double* p,double L,double label,double* dp,double* stats) {
        const Summary s=evaluate(p,label);
        const double factor=-2.*(s.f-label),bfactor=s.rho/L;
        const double ihx=1./hx,iha=1./ha,ihc=1./hc,ihb=1./hb;
        double maxexit=0.,blocked=0.;
        #pragma omp parallel for num_threads(threads) schedule(static) reduction(max:maxexit) reduction(+:blocked)
        for(std::size_t row=0;row<rows;++row) {
            const int ia=int(row%na),ix=int((row/na)%nx),ig=int(row/(std::size_t(na)*nx));
            const std::size_t base=row*sa;
            const double g=gs[ig],ph=phi2[row],ht=h2[row];
            for(int ic=0;ic<nc;++ic) {
                const double c=cs[ic];
                for(int ib=0;ib<nb;++ib) {
                    const std::size_t i=base+std::size_t(ic)*nb+ib;
                    const double b=bs[ib],mass=p[i];
                    const double rawx=factor*phi1[ix]*(g*c*ph+2.*b*s.D);
                    const double rawa=.5*factor*c*ph,rawc=factor*ht;
                    const double vx=limited(rawx,tx[ix]);
                    const double va=limited(rawa,ta[ia]);
                    const double vc=limited(rawc,tc[ic]);
                    const double vb=bfactor*(h1[ix]-b);
                    double exit=0.,value=0.,lost=0.;
                    // Neighbor fluxes are gathered; no concurrent writes to dp.
                    if(ix+1<nx) {
                        if(vx>0.) exit+=vx*ihx;
                        const double vn=limited(factor*phi1[ix+1]*(g*c*phi2[row+na]+2.*b*s.D),tx[ix+1]);
                        if(vn<0.) value-=p[i+sx]*vn*ihx;
                    } else if(vx>0.) lost+=vx*ihx;
                    if(ix>0) {
                        if(vx<0.) exit-=vx*ihx;
                        const double vn=limited(factor*phi1[ix-1]*(g*c*phi2[row-na]+2.*b*s.D),tx[ix-1]);
                        if(vn>0.) value+=p[i-sx]*vn*ihx;
                    } else if(vx<0.) lost-=vx*ihx;
                    if(ia+1<na) {
                        if(va>0.) exit+=va*iha;
                        const double vn=limited(.5*factor*c*phi2[row+1],ta[ia+1]);
                        if(vn<0.) value-=p[i+sa]*vn*iha;
                    } else if(va>0.) lost+=va*iha;
                    if(ia>0) {
                        if(va<0.) exit-=va*iha;
                        const double vn=limited(.5*factor*c*phi2[row-1],ta[ia-1]);
                        if(vn>0.) value+=p[i-sa]*vn*iha;
                    } else if(va<0.) lost-=va*iha;
                    if(ic+1<nc) {
                        if(vc>0.) exit+=vc*ihc;
                        const double vn=limited(rawc,tc[ic+1]);
                        if(vn<0.) value-=p[i+sc]*vn*ihc;
                    } else if(vc>0.) lost+=vc*ihc;
                    if(ic>0) {
                        if(vc<0.) exit-=vc*ihc;
                        const double vn=limited(rawc,tc[ic-1]);
                        if(vn>0.) value+=p[i-sc]*vn*ihc;
                    } else if(vc<0.) lost-=vc*ihc;
                    if(ib+1<nb) {
                        if(vb>0.) exit+=vb*ihb;
                        const double vn=bfactor*(h1[ix]-bs[ib+1]);
                        if(vn<0.) value-=p[i+1]*vn*ihb;
                    } else if(vb>0.) lost+=vb*ihb;
                    if(ib>0) {
                        if(vb<0.) exit-=vb*ihb;
                        const double vn=bfactor*(h1[ix]-bs[ib-1]);
                        if(vn>0.) value+=p[i-1]*vn*ihb;
                    } else if(vb<0.) lost-=vb*ihb;
                    lost+=(std::max(0.,rawx)-std::max(0.,vx))*ihx;
                    lost+=(std::max(0.,rawa)-std::max(0.,va))*iha;
                    lost+=(std::max(0.,rawc)-std::max(0.,vc))*ihc;
                    dp[i]=value-mass*exit;
                    maxexit=std::max(maxexit,exit);
                    blocked+=mass*lost;
                }
            }
        }
        if(stats) {
            stats[0]=s.f; stats[1]=s.rho; stats[2]=s.S; stats[3]=s.D;
            stats[4]=maxexit; stats[5]=s.cap; stats[6]=blocked; stats[7]=s.mass;
        }
        return s;
    }

    double mixed_prediction(const std::vector<double>& oldc,double oldS,
                            double newS,double alpha) const {
        const double S=(1.-alpha)*oldS+alpha*newS;
        double f=0.;
        for(std::size_t row=0;row<rows;++row) {
            const int ia=int(row%na),ix=int((row/na)%nx),ig=int(row/(std::size_t(na)*nx));
            f+=((1.-alpha)*oldc[row]+alpha*cmarg[row])*
               std::tanh(gs[ig]*h1[ix]+2.*as[ia]*S);
        }
        return f;
    }
};

double elapsed(Clock::time_point start) {
    return std::chrono::duration<double>(Clock::now()-start).count();
}
}

extern "C" {

// Each grid length must be >=2. Return null on invalid input/allocation failure.
void* hist_create(int ng,int nx,int na,int nc,int nb,int threads) {
    if(std::min({ng,nx,na,nc,nb})<2) return nullptr;
    std::size_t count=1;
    for(int n:{ng,nx,na,nc,nb}) {
        if(count>std::numeric_limits<std::size_t>::max()/std::size_t(n)) return nullptr;
        count*=std::size_t(n);
    }
    if(count>std::numeric_limits<std::size_t>::max()/sizeof(double)) return nullptr;
    try { return new Histogram(ng,nx,na,nc,nb,threads); }
    catch(...) { return nullptr; }
}

void hist_free(void* handle) { delete static_cast<Histogram*>(handle); }
std::size_t hist_size(void* handle) {
    return handle ? static_cast<Histogram*>(handle)->size : 0;
}

// stats[8]: f,rho,S,D,max_exit_rate,cap_zone_mass,blocked_flux_rate,total_mass.
// blocked_flux_rate is sum p*(removed rate), including taper and absent neighbors.
void hist_rhs(void* handle,const double* p,double L,double label,double* dp,double* stats) {
    if(!handle || !p || !dp || !(L>0.)) return;
    static_cast<Histogram*>(handle)->rhs(p,L,label,dp,stats);
}

// SSP-RK2, with the CFL condition checked at both Euler stages.
// p and *L hold only accepted states, including if the deadline interrupts a trial.
// stats[12]: reason (0 fitted,1 deadline,2 time_cap,3 numerical_failure),
// physical_time,MSE,accepted_steps,wall_seconds,total_mass,min_mass,
// max_accepted_cap_zone_mass,max_accepted_loss_rise,max_exit_rate,
// full_crossing_step_dt (0 absent),final_L.
// Endpoint refinement interpolates masses and clock within the first accepted
// step crossing the target; it is a numerical event approximation, not an exact
// continuous-flow hitting time. Deadlines include all work inside this function.
void hist_integrate(void* handle,double* p,double* L,double label,double target,
                    double cfl,double max_training_seconds,double time_cap,double* stats) {
    const auto start=Clock::now();
    if(stats) std::fill(stats,stats+12,std::numeric_limits<double>::quiet_NaN());
    if(!handle || !p || !L || !stats || !(*L>0.) || !(label>0.) ||
       !(target>=0.) || !(cfl>0. && cfl<1.) || !(max_training_seconds>0.) || !(time_cap>=0.)) {
        if(stats) stats[0]=3.;
        return;
    }
    Histogram& h=*static_cast<Histogram*>(handle);
    double t=0.,steps=0.,maxcap=0.,maxrise=0.,maxexit=0.,crossdt=0.;
    int reason=2;
    Summary accepted=h.evaluate(p,label);
    double mse=(accepted.f-label)*(accepted.f-label);
    maxcap=accepted.cap;
    try {
        std::vector<double> dp0(h.size),dp1(h.size),stage(h.size),candidate(h.size),oldc(h.rows);
        double last_progress=0.;
        while(mse>target && t<time_cap) {
            if(elapsed(start)>=max_training_seconds) { reason=1; break; }
            double stat0[8],stat1[8];
            const Summary initial=h.rhs(p,*L,label,dp0.data(),stat0);
            oldc=h.cmarg;
            maxexit=std::max(maxexit,stat0[4]);
            if(!std::isfinite(stat0[4]) || !std::isfinite(initial.f) || initial.minimum< -1.e-14) { reason=3; break; }
            if(elapsed(start)>=max_training_seconds) { reason=1; break; }
            double dt=std::min(time_cap-t,stat0[4]>0. ? cfl/stat0[4] : time_cap-t);
            if(!(dt>0.) || !std::isfinite(dt)) { reason=3; break; }
            double stageL=*L;
            Summary firststage;
            bool valid=false;
            for(int retry=0;retry<20;++retry) {
                #pragma omp parallel for num_threads(h.threads) schedule(static)
                for(std::size_t i=0;i<h.size;++i) stage[i]=p[i]+dt*dp0[i];
                stageL=*L+dt*initial.rho;
                firststage=h.rhs(stage.data(),stageL,label,dp1.data(),stat1);
                maxexit=std::max(maxexit,stat1[4]);
                if(elapsed(start)>=max_training_seconds) { reason=1; break; }
                if(!std::isfinite(firststage.f) || !std::isfinite(stat1[4]) || firststage.minimum< -1.e-14) { reason=3; break; }
                if(dt*stat1[4]<=cfl*(1.+1.e-12)) { valid=true; break; }
                dt*=.95*cfl/(dt*stat1[4]);
            }
            if(!valid) { if(reason!=1) reason=3; break; }
            #pragma omp parallel for num_threads(h.threads) schedule(static)
            for(std::size_t i=0;i<h.size;++i) candidate[i]=.5*p[i]+.5*(stage[i]+dt*dp1[i]);
            const double candidateL=.5*(*L)+.5*(stageL+dt*firststage.rho);
            const Summary next=h.evaluate(candidate.data(),label);
            const double nextmse=(next.f-label)*(next.f-label);
            if(!std::isfinite(nextmse) || next.minimum< -1.e-14 || !std::isfinite(next.mass)) { reason=3; break; }
            if(elapsed(start)>=max_training_seconds) { reason=1; break; }
            if(nextmse<=target) {
                double lo=0.,hi=1.;
                for(int iteration=0;iteration<48;++iteration) {
                    const double mid=.5*(lo+hi);
                    const double value=h.mixed_prediction(oldc,initial.S,next.S,mid)-label;
                    if(value*value<=target) hi=mid; else lo=mid;
                }
                #pragma omp parallel for num_threads(h.threads) schedule(static)
                for(std::size_t i=0;i<h.size;++i) p[i]=(1.-hi)*p[i]+hi*candidate[i];
                *L=(1.-hi)*(*L)+hi*candidateL;
                t+=hi*dt; crossdt=dt; ++steps;
                accepted=h.evaluate(p,label);
                const double finalmse=(accepted.f-label)*(accepted.f-label);
                maxrise=std::max(maxrise,finalmse-mse);
                mse=finalmse; maxcap=std::max(maxcap,accepted.cap);
                reason=0; break;
            }
            std::memcpy(p,candidate.data(),h.size*sizeof(double));
            *L=candidateL; t+=dt; ++steps;
            maxrise=std::max(maxrise,nextmse-mse);
            mse=nextmse; accepted=next; maxcap=std::max(maxcap,next.cap);
            const double now=elapsed(start);
            if(now-last_progress>=8.) {
                std::printf("histogram states=%zu steps=%.0f MSE=%.8g t=%.6g seconds=%.1f\n",h.size,steps,mse,t,now);
                std::fflush(stdout); last_progress=now;
            }
        }
        if(mse<=target) reason=0;
    } catch(...) { reason=3; }
    // No extra full RHS is needed on deadline: accepted refers to the checkpoint.
    stats[0]=reason; stats[1]=t; stats[2]=mse; stats[3]=steps;
    stats[4]=elapsed(start); stats[5]=accepted.mass; stats[6]=accepted.minimum;
    stats[7]=maxcap; stats[8]=maxrise; stats[9]=maxexit;
    stats[10]=crossdt; stats[11]=*L;
}

// Fixed eta quadrature must represent N(0,1), with weights summing to one.
// It is used for passive new-input evaluation only, never evolved as particles.
// L is accepted for a uniform API; normalized b makes the query formula L-free.
void hist_predict(void* handle,const double* p,double L,const double* angles,int count,
                  const double* eta_nodes,const double* eta_weights,int eta_count,double* out) {
    if(!handle || !p || !angles || !eta_nodes || !eta_weights || !out || count<0 || eta_count<1) return;
    (void)L;
    Histogram& h=*static_cast<Histogram*>(handle);
    std::vector<double> weighted_b(h.nx,0.);
    // Build W(g,x,a)=sum_{c,b} c*p and Q(x)=sum_{g,a,c,b} b*p once.
    #pragma omp parallel for num_threads(h.threads) schedule(static)
    for(int ix=0;ix<h.nx;++ix) {
        double bsum=0.;
        for(int ig=0;ig<h.ng;++ig) for(int ia=0;ia<h.na;++ia) {
            const std::size_t row=(std::size_t(ig)*h.nx+ix)*h.na+ia;
            double csum=0.;
            for(int ic=0;ic<h.nc;++ic) for(int ib=0;ib<h.nb;++ib) {
                const double mass=p[row*h.sa+std::size_t(ic)*h.nb+ib];
                bsum+=h.bs[ib]*mass;
                csum+=h.cs[ic]*mass;
            }
            h.cmarg[row]=csum;
        }
        weighted_b[ix]=bsum;
    }
    #pragma omp parallel for num_threads(h.threads) schedule(static)
    for(int it=0;it<count;++it) {
        const double co=std::cos(angles[it]),si=std::sin(angles[it]);
        std::vector<double> htheta(std::size_t(h.nx)*eta_count);
        double S=0.;
        for(int ix=0;ix<h.nx;++ix) {
            double average=0.;
            for(int ie=0;ie<eta_count;++ie) {
                const double value=std::tanh(h.xs[ix]*co+eta_nodes[ie]*si);
                htheta[std::size_t(ix)*eta_count+ie]=value;
                average+=eta_weights[ie]*value;
            }
            S+=weighted_b[ix]*average;
        }
        double f=0.;
        for(int ig=0;ig<h.ng;++ig) for(int ix=0;ix<h.nx;++ix) for(int ia=0;ia<h.na;++ia) {
            const std::size_t row=(std::size_t(ig)*h.nx+ix)*h.na+ia;
            const double weight=h.cmarg[row];
            if(weight==0.) continue;
            const double correction=2.*h.as[ia]*S;
            double average=0.;
            for(int ie=0;ie<eta_count;++ie)
                average+=eta_weights[ie]*std::tanh(h.gs[ig]*htheta[std::size_t(ix)*eta_count+ie]+correction);
            f+=weight*average;
        }
        out[it]=f;
    }
}
}
