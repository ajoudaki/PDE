#include <algorithm>
#include <atomic>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif

using i128=__int128_t;
static std::string show(i128 x){if(!x)return"0";bool n=x<0;if(n)x=-x;std::string s;while(x){s.push_back(char('0'+x%10));x/=10;}if(n)s.push_back('-');std::reverse(s.begin(),s.end());return s;}
static i128 odddf(int q){i128 z=1;for(int j=q;j>0;j-=2)z*=j;return z;}

struct Component { std::vector<int>a,h,m; int rows{},cols{},edges{}; };

struct TypeCounter {
  const int P,target;
  std::unordered_map<std::string,i128> memo;
  explicit TypeCounter(const Component&c):P(c.edges/2),target(P+1){}

  static std::string key(const std::vector<int>&a,const std::vector<int>&h,const std::vector<int>&m){
    std::string s; s.reserve(3+a.size()+h.size()+m.size());
    s.push_back(char(a.size()));s.push_back(char(h.size()));
    for(int z:a)s.push_back(char(z));for(int z:h)s.push_back(char(z));for(int z:m)s.push_back(char(z));return s;
  }
  static void merge_rows(int x,int y,std::vector<int>&a,std::vector<int>&m,int cols){
    if(x==y)return;if(x>y)std::swap(x,y);a[x]+=a[y];
    for(int j=0;j<cols;++j)m[x*cols+j]+=m[y*cols+j];
    a.erase(a.begin()+y);m.erase(m.begin()+y*cols,m.begin()+(y+1)*cols);
  }
  static void merge_cols(int x,int y,std::vector<int>&h,std::vector<int>&m,int rows,int cols){
    if(x==y)return;if(x>y)std::swap(x,y);h[x]+=h[y];
    for(int i=0;i<rows;++i)m[i*cols+x]+=m[i*cols+y];
    std::vector<int> z;z.reserve(rows*(cols-1));
    for(int i=0;i<rows;++i)for(int j=0;j<cols;++j)if(j!=y)z.push_back(m[i*cols+j]);
    h.erase(h.begin()+y);m.swap(z);
  }
  i128 rec(const std::vector<int>&a,const std::vector<int>&h,const std::vector<int>&m,int rem){
    int V=a.size()+h.size(),pairs=rem/2;
    if(V<target || V-2*pairs>target)return 0;
    if(!rem){if(V!=target)return 0;i128 z=1;for(int q:a){if(q&1)return 0;z*=odddf(q-1);}for(int q:h){if(q&1)return 0;z*=odddf(q-1);}return z;}
    std::string k=key(a,h,m);auto it=memo.find(k);if(it!=memo.end())return it->second;
    int rows=a.size(),cols=h.size(),q0=-1;for(int q=0;q<int(m.size());++q)if(m[q]){q0=q;break;}
    int u0=q0/cols,v0=q0%cols;auto first=m;--first[q0];i128 ans=0;
    for(int q1=0;q1<int(first.size());++q1){int mult=first[q1];if(!mult)continue;int u1=q1/cols,v1=q1%cols;
      auto aa=a,hh=h,mm=first;--mm[q1];
      merge_rows(u0,u1,aa,mm,cols);int rows2=aa.size();
      merge_cols(v0,v1,hh,mm,rows2,cols);
      ans += i128(mult)*rec(aa,hh,mm,rem-2);
    }
    memo.emplace(std::move(k),ans);return ans;
  }
  i128 run(const Component&c){if(c.edges&1)return 0;return rec(c.a,c.h,c.m,c.edges);}
};

struct Term{i128 coef;int power,nt,nb;std::vector<int>a,h,m;};
static std::vector<Component> components(const Term&t){
 int N=t.nt+t.nb;std::vector<std::vector<int>>adj(N);for(int i=0;i<t.nt;++i)for(int j=0;j<t.nb;++j)if(t.m[i*t.nb+j]){adj[i].push_back(t.nt+j);adj[t.nt+j].push_back(i);}std::vector<int>seen(N),local(N);std::vector<Component>out;
 for(int st=0;st<N;++st)if(!seen[st]){std::vector<int>v{st};seen[st]=1;for(size_t q=0;q<v.size();++q)for(int w:adj[v[q]])if(!seen[w]){seen[w]=1;v.push_back(w);}std::vector<int>rv,cv;for(int x:v)(x<t.nt?rv:cv).push_back(x);Component c;c.rows=rv.size();c.cols=cv.size();for(int x:rv)c.a.push_back(t.a[x]);for(int x:cv)c.h.push_back(t.h[x-t.nt]);c.m.assign(c.rows*c.cols,0);for(int i=0;i<c.rows;++i)for(int j=0;j<c.cols;++j){c.m[i*c.cols+j]=t.m[rv[i]*t.nb+(cv[j]-t.nt)];c.edges+=c.m[i*c.cols+j];}if(c.edges+1!=c.rows+c.cols)throw std::runtime_error("not tree");out.push_back(std::move(c));}
 if(int(out.size())!=t.power)throw std::runtime_error("component count");return out;
}
int main(int argc,char**argv){if(argc<2||argc>3)return 2;int req=argc==3?std::stoi(argv[2]):-1;std::ifstream in(argv[1]);int n;in>>n;std::vector<Term>T(n);for(auto&t:T){long long c;in>>c>>t.power>>t.nt>>t.nb;t.coef=c;t.a.resize(t.nt);t.h.resize(t.nb);t.m.resize(t.nt*t.nb);for(int&x:t.a)in>>x;for(int&x:t.h)in>>x;for(int&x:t.m)in>>x;}
 std::vector<i128>val(n);std::atomic<int>done{0};
#pragma omp parallel for schedule(dynamic,1)
 for(int i=0;i<n;++i){int E=std::accumulate(T[i].m.begin(),T[i].m.end(),0);if(req>=0&&E/2!=req)continue;i128 z=1;for(auto&c:components(T[i])){i128 q=TypeCounter(c).run(c);if(!q){z=0;break;}z*=q;}val[i]=z;int d=++done;if(d%10000==0){
#pragma omp critical
 std::cerr<<"done "<<d<<"\n";}}
 std::vector<i128>by(32);i128 total=0;int surv=0;for(int i=0;i<n;++i)if(val[i]){++surv;int E=std::accumulate(T[i].m.begin(),T[i].m.end(),0);i128 z=T[i].coef*val[i];by[E/2]+=z;total+=z;}std::cout<<"surviving "<<surv<<"/"<<n<<"\n";for(int i=0;i<32;++i)if(by[i])std::cout<<"p"<<i<<" "<<show(by[i])<<"\n";std::cout<<"total "<<show(total)<<"\n";
}
