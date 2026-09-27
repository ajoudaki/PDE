// Fixed-grid conservative Eulerian k=1,H=1 histogram; no evolved particles.
// Build with g++ -O3 -std=c++17 -fPIC -shared -fopenmp.
// C-order coordinates: g,wx,wy,c,A[0:m],b[0:m]; b=B/L, g folded >=0.
#include <algorithm>
#include <chrono>
#include <cmath>
#include <cstddef>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <limits>
#include <vector>

namespace {
using Clock=std::chrono::steady_clock;
struct Summary {
    double mse=0.,rho=0.,mass=0.,minimum=0.,cap=0.;
    double S[9]{},T[9]{},f[3]{};
};
struct Multi {
    int m,d,threads;
    std::size_t N,NA,NB,NW,rows;
    std::vector<int> shape;
    std::vector<std::size_t> stride;
    std::vector<double> bound,u,step;
    std::vector<std::vector<double>> axis,taper;
    std::vector<double> av,bv,h,phi1,H,phi2,W,rates;
    std::vector<int> ai,bi;
    std::vector<std::uint32_t> edges;
    std::vector<unsigned char> acap;
    Multi(int mm,const int* nn,const double* bb,const double* uu,int nt):
        m(mm),d(4+2*mm),threads(std::max(1,nt)),N(1),NA(1),NB(1),NW(0),rows(0),
        shape(nn,nn+d),stride(d),bound(bb,bb+d),u(uu,uu+2*m),step(d),axis(d),taper(d) {
        for(int j=d-1;j>=0;--j) { stride[j]=N; N*=shape[j]; }
        for(int j=0;j<d;++j) {
            axis[j].resize(shape[j]); taper[j].resize(shape[j]);
            step[j]=(j==0 ? bound[j] : 2.*bound[j])/(shape[j]-1);
            for(int i=0;i<shape[j];++i) {
                axis[j][i]=(j==0 ? 0. : -bound[j])+step[j]*i;
                taper[j][i]=std::max(0.,std::min(1.,5.*(1.-std::abs(axis[j][i])/bound[j])));
            }
        }
        for(int j=0;j<m;++j) { NA*=shape[4+j]; NB*=shape[4+m+j]; }
        NW=std::size_t(shape[1])*shape[2]; rows=std::size_t(shape[0])*NW*NA;
        av.resize(NA*m); bv.resize(NB*m); ai.resize(NA*m); bi.resize(NB*m); acap.resize(NA);
        for(std::size_t a=0;a<NA;++a) {
            std::size_t v=a;
            for(int j=m-1;j>=0;--j) {
                const int index=v%shape[4+j]; v/=shape[4+j];
                ai[a*m+j]=index;
                av[a*m+j]=axis[4+j][index];
                if(std::abs(av[a*m+j])>=.8*bound[4+j]) acap[a]=1;
            }
        }
        for(std::size_t b=0;b<NB;++b) {
            std::size_t v=b;
            for(int j=m-1;j>=0;--j) {
                bi[b*m+j]=v%shape[4+m+j]; bv[b*m+j]=axis[4+m+j][bi[b*m+j]]; v/=shape[4+m+j];
            }
        }
        h.resize(NW*m); phi1.resize(NW*m);
        for(std::size_t w=0;w<NW;++w) for(int j=0;j<m;++j) {
            const double z=axis[1][w/shape[2]]*u[2*j]+axis[2][w%shape[2]]*u[2*j+1];
            h[w*m+j]=std::tanh(z); phi1[w*m+j]=1.-h[w*m+j]*h[w*m+j];
        }
        H.resize(rows*m); phi2.resize(rows*m); W.resize(rows); rates.resize(N*(d-1));
        // Fixed neighbor-existence bits remove integer division from every flux RHS.
        edges.resize(N);
        #pragma omp parallel for num_threads(threads) schedule(static)
        for(std::size_t index=0;index<N;++index) {
            std::uint32_t mask=0;
            for(int j=1;j<d;++j) {
                const int k=(index/stride[j])%shape[j];
                if(k>0) mask|=std::uint32_t(1)<<(2*(j-1));
                if(k+1<shape[j]) mask|=std::uint32_t(1)<<(2*(j-1)+1);
            }
            edges[index]=mask;
        }
    }

    Summary evaluate(const double* p,const double* labels) {
        Summary out; out.minimum=std::numeric_limits<double>::infinity();
        #pragma omp parallel num_threads(threads)
        {
            double localS[9]{},mass=0.,minimum=std::numeric_limits<double>::infinity(),cap=0.;
            #pragma omp for schedule(static)
            for(std::size_t row=0;row<rows;++row) {
                const std::size_t a=row%NA,gw=row/NA,w=gw%NW;
                const int ix=w/shape[2],iy=w%shape[2];
                const bool fixedcap=acap[a] || std::abs(axis[1][ix])>=.8*bound[1] || std::abs(axis[2][iy])>=.8*bound[2];
                double csum=0.,bsum[3]{};
                for(int ic=0;ic<shape[3];++ic) {
                    const bool incap=fixedcap || std::abs(axis[3][ic])>=.8*bound[3];
                    const std::size_t base=(gw*shape[3]+ic)*NA*NB+a*NB;
                    double psum=0.;
                    for(std::size_t b=0;b<NB;++b) {
                        const double v=p[base+b]; psum+=v; mass+=v;
                        minimum=std::min(minimum,v); if(incap) cap+=v;
                        for(int j=0;j<m;++j) bsum[j]+=bv[b*m+j]*v;
                    }
                    csum+=axis[3][ic]*psum;
                }
                W[row]=csum;
                for(int j=0;j<m;++j) for(int i=0;i<m;++i) localS[j*m+i]+=bsum[j]*h[w*m+i];
            }
            #pragma omp critical
            {
                out.mass+=mass; out.minimum=std::min(out.minimum,minimum); out.cap+=cap;
                for(int j=0;j<m*m;++j) out.S[j]+=localS[j];
            }
        }
        #pragma omp parallel num_threads(threads)
        {
            double f[3]{},T[9]{};
            #pragma omp for schedule(static)
            for(std::size_t row=0;row<rows;++row) {
                const std::size_t a=row%NA,gw=row/NA,w=gw%NW,g=gw/NW;
                for(int i=0;i<m;++i) {
                    double z=axis[0][g]*h[w*m+i];
                    for(int j=0;j<m;++j) z-=2./m*av[a*m+j]*out.S[j*m+i];
                    const double value=std::tanh(z),ph=std::max(0.,1.-value*value);
                    H[row*m+i]=value; phi2[row*m+i]=ph; f[i]+=W[row]*value;
                    for(int j=0;j<m;++j) T[j*m+i]+=av[a*m+j]*W[row]*ph;
                }
            }
            #pragma omp critical
            {
                for(int i=0;i<m;++i) out.f[i]+=f[i];
                for(int j=0;j<m*m;++j) out.T[j]+=T[j];
            }
        }
        for(int i=0;i<m;++i) out.mse+=(out.f[i]-labels[i])*(out.f[i]-labels[i])/m;
        out.rho=std::sqrt(out.mse); return out;
    }

    Summary rhs(const double* p,double L,const double* labels,double* dp,double* stats) {
        const Summary s=evaluate(p,labels);
        double residual[3]{}; for(int i=0;i<m;++i) residual[i]=s.f[i]-labels[i];
        double maxexit=0.,blocked=0.;
        #pragma omp parallel for num_threads(threads) schedule(static) reduction(max:maxexit) reduction(+:blocked)
        for(std::size_t row=0;row<rows;++row) {
            const std::size_t a=row%NA,gw=row/NA,w=gw%NW,g=gw/NW;
            int coordinate[10]{};
            coordinate[1]=w/shape[2]; coordinate[2]=w%shape[2];
            for(int j=0;j<m;++j) coordinate[4+j]=ai[a*m+j];
            for(int ic=0;ic<shape[3];++ic) {
                coordinate[3]=ic;
                const double c=axis[3][ic];
                const std::size_t base=(gw*shape[3]+ic)*NA*NB+a*NB;
                for(std::size_t b=0;b<NB;++b) {
                    for(int j=0;j<m;++j) coordinate[4+m+j]=bi[b*m+j];
                    const std::size_t index=base+b;
                    double v[10]{};
                    for(int i=0;i<m;++i) {
                        const double delta=c*phi2[row*m+i];
                        double backward=axis[0][g]*delta;
                        for(int j=0;j<m;++j) backward-=2./m*bv[b*m+j]*s.T[j*m+i];
                        const double back=-2./m*residual[i]*phi1[w*m+i]*backward;
                        v[1]+=back*u[2*i]; v[2]+=back*u[2*i+1];
                        v[3]-=2./m*residual[i]*H[row*m+i];
                        v[4+i]=residual[i]*delta;
                        v[4+m+i]=s.rho/L*(h[w*m+i]-bv[b*m+i]);
                    }
                    double exit=0.,lost=0.;
                    for(int j=1;j<d;++j) {
                        const int k=coordinate[j];
                        double value=v[j];
                        if(j<4+m && value*axis[j][k]>0.) value*=taper[j][k];
                        if((k==0 && value<0.) || (k==shape[j]-1 && value>0.)) value=0.;
                        lost+=(std::abs(v[j])-std::abs(value))/step[j];
                        const double rate=value/step[j]; rates[std::size_t(j-1)*N+index]=rate;
                        exit+=std::abs(rate);
                    }
                    maxexit=std::max(maxexit,exit); blocked+=p[index]*lost;
                }
            }
        }
        #pragma omp parallel for num_threads(threads) schedule(static)
        for(std::size_t index=0;index<N;++index) {
            double value=0.;
            for(int j=1;j<d;++j) {
                const std::size_t ratebase=std::size_t(j-1)*N,shift=stride[j];
                value-=p[index]*std::abs(rates[ratebase+index]);
                if(edges[index]&(std::uint32_t(1)<<(2*(j-1)))) value+=p[index-shift]*std::max(0.,rates[ratebase+index-shift]);
                if(edges[index]&(std::uint32_t(1)<<(2*(j-1)+1))) value+=p[index+shift]*std::max(0.,-rates[ratebase+index+shift]);
            }
            dp[index]=value;
        }
        if(stats) {
            std::fill(stats,stats+16,0.);
            stats[0]=s.mse; stats[1]=s.rho; stats[2]=maxexit; stats[3]=s.cap;
            stats[4]=blocked; stats[5]=s.mass; stats[6]=s.minimum;
            for(int i=0;i<m;++i) stats[7+i]=s.f[i];
        }
        return s;
    }

    double mixture_mse(const std::vector<double>& oldW,const Summary& old,
                       const Summary& next,const double* labels,double alpha) const {
        double S[9]{},f[3]{};
        for(int j=0;j<m*m;++j) S[j]=(1.-alpha)*old.S[j]+alpha*next.S[j];
        for(std::size_t row=0;row<rows;++row) {
            const std::size_t a=row%NA,gw=row/NA,w=gw%NW,g=gw/NW;
            const double weight=(1.-alpha)*oldW[row]+alpha*W[row];
            for(int i=0;i<m;++i) {
                double z=axis[0][g]*h[w*m+i];
                for(int j=0;j<m;++j) z-=2./m*av[a*m+j]*S[j*m+i];
                f[i]+=weight*std::tanh(z);
            }
        }
        double mse=0.; for(int i=0;i<m;++i) mse+=(f[i]-labels[i])*(f[i]-labels[i])/m;
        return mse;
    }
};
double elapsed(Clock::time_point start) { return std::chrono::duration<double>(Clock::now()-start).count(); }
}

extern "C" {
// shape,bounds lengths=4+2m; u is row-major(m,2). All shapes >=2, all bounds>0.
// b bounds must equal1. Shapes of signed axes should be odd to include zero.
void* hist_multi_create(int m,const int* shape,const double* bounds,const double* u,int threads) {
    if((m!=2 && m!=3) || !shape || !bounds || !u) return nullptr;
    std::size_t count=1;
    for(int j=0;j<4+2*m;++j) {
        if(shape[j]<2 || !(bounds[j]>0.) || !std::isfinite(bounds[j])) return nullptr;
        if(j>=4+m && bounds[j]!=1.) return nullptr;
        if(count>std::numeric_limits<std::size_t>::max()/std::size_t(shape[j])) return nullptr;
        count*=shape[j];
    }
    if(count>std::numeric_limits<std::size_t>::max()/(sizeof(double)*(3+2*m))) return nullptr;
    for(int j=0;j<2*m;++j) if(!std::isfinite(u[j])) return nullptr;
    try { return new Multi(m,shape,bounds,u,threads); } catch(...) { return nullptr; }
}
void hist_multi_free(void* handle) { delete static_cast<Multi*>(handle); }
std::size_t hist_multi_size(void* handle) { return handle ? static_cast<Multi*>(handle)->N : 0; }
// stats[16]: MSE,rho,max_exit,cap_mass,blocked_rate,mass,min_mass,f[0:m],zeros.
void hist_multi_rhs(void* handle,const double* p,double L,const double* labels,double* dp,double* stats) {
    if(handle && p && labels && dp && L>0.) static_cast<Multi*>(handle)->rhs(p,L,labels,dp,stats);
}
// stats[12]: reason0fit/1deadline/2timecap/3numerical,t,MSE,steps,seconds,
// mass,min_mass,max_cap_mass,max_loss_rise,max_exit,full_crossing_dt,final_L.
// State updates are SSP-RK2 with both-stage CFL checks. Terminal interpolation
// is a convex interpolation of the first accepted step crossing target MSE.
void hist_multi_integrate(void* handle,double* p,double* L,const double* labels,double target,
                          double cfl,double seconds,double timecap,double* stats) {
    const auto start=Clock::now();
    if(stats) std::fill(stats,stats+12,std::numeric_limits<double>::quiet_NaN());
    if(!handle || !p || !L || !labels || !stats || !(*L>0.) || !(target>=0.) ||
       !(cfl>0. && cfl<1.) || !(seconds>0.) || !(timecap>=0.)) { if(stats) stats[0]=3.; return; }
    Multi& h=*static_cast<Multi*>(handle);
    double t=0.,steps=0.,maxcap=0.,maxrise=0.,maxexit=0.,crossdt=0.; int reason=2;
    Summary accepted=h.evaluate(p,labels); maxcap=accepted.cap;
    try {
        std::vector<double> dp0(h.N),dp1(h.N),stage(h.N),candidate(h.N),oldW(h.rows);
        double lastprogress=0.;
        while(accepted.mse>target && t<timecap) {
            if(elapsed(start)>=seconds) { reason=1; break; }
            double stat0[16],stat1[16];
            const Summary initial=h.rhs(p,*L,labels,dp0.data(),stat0); oldW=h.W;
            maxexit=std::max(maxexit,stat0[2]);
            if(!std::isfinite(initial.mse) || !std::isfinite(stat0[2]) || initial.minimum< -1.e-14) { reason=3; break; }
            if(elapsed(start)>=seconds) { reason=1; break; }
            double dt=std::min(timecap-t,stat0[2]>0. ? cfl/stat0[2] : timecap-t);
            if(!(dt>0.) || !std::isfinite(dt)) { reason=3; break; }
            double stageL=*L; Summary first; bool valid=false;
            for(int retry=0;retry<20;++retry) {
                #pragma omp parallel for num_threads(h.threads) schedule(static)
                for(std::size_t i=0;i<h.N;++i) stage[i]=p[i]+dt*dp0[i];
                stageL=*L+dt*initial.rho;
                first=h.rhs(stage.data(),stageL,labels,dp1.data(),stat1); maxexit=std::max(maxexit,stat1[2]);
                if(elapsed(start)>=seconds) { reason=1; break; }
                if(!std::isfinite(first.mse) || !std::isfinite(stat1[2]) || first.minimum< -1.e-14) { reason=3; break; }
                if(dt*stat1[2]<=cfl*(1.+1.e-12)) { valid=true; break; }
                dt*=.95*cfl/(dt*stat1[2]);
            }
            if(!valid) { if(reason!=1) reason=3; break; }
            #pragma omp parallel for num_threads(h.threads) schedule(static)
            for(std::size_t i=0;i<h.N;++i) candidate[i]=.5*p[i]+.5*(stage[i]+dt*dp1[i]);
            const double nextL=.5*(*L)+.5*(stageL+dt*first.rho);
            const Summary next=h.evaluate(candidate.data(),labels);
            if(!std::isfinite(next.mse) || !std::isfinite(next.mass) || next.minimum< -1.e-14) { reason=3; break; }
            if(elapsed(start)>=seconds) { reason=1; break; }
            if(next.mse<=target) {
                double lo=0.,hi=1.;
                for(int iteration=0;iteration<40;++iteration) {
                    const double mid=.5*(lo+hi);
                    if(h.mixture_mse(oldW,initial,next,labels,mid)<=target) hi=mid; else lo=mid;
                }
                #pragma omp parallel for num_threads(h.threads) schedule(static)
                for(std::size_t i=0;i<h.N;++i) p[i]=(1.-hi)*p[i]+hi*candidate[i];
                *L=(1.-hi)*(*L)+hi*nextL; t+=hi*dt; crossdt=dt; ++steps;
                const Summary final=h.evaluate(p,labels);
                maxrise=std::max(maxrise,final.mse-accepted.mse); accepted=final;
                maxcap=std::max(maxcap,accepted.cap); reason=0; break;
            }
            std::memcpy(p,candidate.data(),h.N*sizeof(double)); *L=nextL; t+=dt; ++steps;
            maxrise=std::max(maxrise,next.mse-accepted.mse); accepted=next; maxcap=std::max(maxcap,next.cap);
            const double now=elapsed(start);
            if(now-lastprogress>=8.) {
                std::printf("multi histogram m=%d states=%zu steps=%.0f MSE=%.8g t=%.6g seconds=%.1f\n",h.m,h.N,steps,accepted.mse,t,now);
                std::fflush(stdout); lastprogress=now;
            }
        }
        if(accepted.mse<=target) reason=0;
    } catch(...) { reason=3; }
    stats[0]=reason; stats[1]=t; stats[2]=accepted.mse; stats[3]=steps; stats[4]=elapsed(start);
    stats[5]=accepted.mass; stats[6]=accepted.minimum; stats[7]=maxcap; stats[8]=maxrise;
    stats[9]=maxexit; stats[10]=crossdt; stats[11]=*L;
}

// Exact b,c marginalization; arbitrary circle directions require no extra state.
void hist_multi_predict(void* handle,const double* p,double L,const double* angles,int count,double* out) {
    if(!handle || !p || !angles || !out || count<0) return;
    (void)L; Multi& h=*static_cast<Multi*>(handle);
    std::vector<double> Q(h.NW*h.m,0.);
    #pragma omp parallel for num_threads(h.threads) schedule(static)
    for(std::size_t w=0;w<h.NW;++w) {
        double bsum[3]{};
        for(int g=0;g<h.shape[0];++g) for(std::size_t a=0;a<h.NA;++a) {
            const std::size_t gw=std::size_t(g)*h.NW+w,row=gw*h.NA+a;
            double csum=0.;
            for(int ic=0;ic<h.shape[3];++ic) for(std::size_t b=0;b<h.NB;++b) {
                const double mass=p[(gw*h.shape[3]+ic)*h.NA*h.NB+a*h.NB+b];
                csum+=h.axis[3][ic]*mass;
                for(int j=0;j<h.m;++j) bsum[j]+=h.bv[b*h.m+j]*mass;
            }
            h.W[row]=csum;
        }
        for(int j=0;j<h.m;++j) Q[w*h.m+j]=bsum[j];
    }
    #pragma omp parallel for num_threads(h.threads) schedule(static)
    for(int it=0;it<count;++it) {
        const double co=std::cos(angles[it]),si=std::sin(angles[it]);
        std::vector<double> ht(h.NW); double S[3]{};
        for(std::size_t w=0;w<h.NW;++w) {
            ht[w]=std::tanh(h.axis[1][w/h.shape[2]]*co+h.axis[2][w%h.shape[2]]*si);
            for(int j=0;j<h.m;++j) S[j]+=Q[w*h.m+j]*ht[w];
        }
        double f=0.;
        for(std::size_t row=0;row<h.rows;++row) {
            const std::size_t a=row%h.NA,gw=row/h.NA,w=gw%h.NW,g=gw/h.NW;
            double z=h.axis[0][g]*ht[w];
            for(int j=0;j<h.m;++j) z-=2./h.m*h.av[a*h.m+j]*S[j];
            f+=h.W[row]*std::tanh(z);
        }
        out[it]=f;
    }
}
}
