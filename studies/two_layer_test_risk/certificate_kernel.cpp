// Deterministic scalar quadrature for the fixed two-hidden-layer coefficient.
// No network training and no libm exp/tanh calls. See CERTIFICATION_ENGINE.md.
// Compile: g++ -O3 -std=c++17 -fno-fast-math -ffp-contract=off SOURCE -o OUTPUT
#include <array>
#include <cfloat>
#include <cfenv>
#include <cmath>
#include <cstdint>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>

static_assert(FLT_RADIX == 2 && DBL_MANT_DIG == 53, "binary64 required");
static_assert(LDBL_MANT_DIG >= 64, "64-bit-or-better long-double significand required");
static_assert(sizeof(double) == sizeof(std::uint64_t), "binary64 size required");

namespace {
using Vec = std::vector<double>;
using Sums = std::vector<long double>;
std::vector<double> received;
std::uint64_t bits(double x) {
  std::uint64_t u;
  std::memcpy(&u, &x, sizeof u);
  return u;
}
double read_double() {
  double v;
  if (!(std::cin >> v) || !std::isfinite(v)) throw std::runtime_error("invalid real input");
  received.push_back(v);
  return v;
}
int read_int() {
  int v;
  if (!(std::cin >> v)) throw std::runtime_error("invalid integer input");
  return v;
}

// For 0 <= r <= 64: relative error <= 2e-12, including the degree-12 tail.
// Division by 256 is exact; coefficients have relative errors at most 2^-53.
double exp_negative(double r) {
  if (!(r >= 0.0 && r <= 64.0)) throw std::runtime_error("exponential argument out of contract");
  const double s = -r / 256.0;
  constexpr double c[] = {1.0, 1.0, 1.0/2.0, 1.0/6.0, 1.0/24.0,
    1.0/120.0, 1.0/720.0, 1.0/5040.0, 1.0/40320.0,
    1.0/362880.0, 1.0/3628800.0, 1.0/39916800.0, 1.0/479001600.0};
  double v = c[12];
  for (int k = 11; k >= 0; --k) v = c[k] + s*v;
  for (int k = 0; k < 8; ++k) v = v*v;
  return v;
}
double bounded_tanh(double z) {
  const double a = std::fabs(z);
  if (a > 16.0) return z < 0.0 ? -1.0 : 1.0;
  const double r = exp_negative(2.0*a);
  double v = (1.0-r)/(1.0+r);
  // Projection onto [-1,1] cannot enlarge error to true tanh.
  if (v < 0.0) v = 0.0;
  if (v > 1.0) v = 1.0;
  return z < 0.0 ? -v : v;
}
struct Grid {
  int m;
  double step;
  Vec x, w;
  Grid(int count, double spacing, double normal) : m(count), step(spacing) {
    if (m < 0 || m > 200 || !(step >= 0 && step <= 1.0))
      throw std::runtime_error("grid out of contract");
    if (m == 0) {
      if (step != 0.0) throw std::runtime_error("zero-count axis must have zero step");
      x = {0.0}; w = {1.0}; return;
    }
    if (!(step > 0.0 && m*step <= 9.0)) throw std::runtime_error("grid radius out of contract");
    for (int k = -m; k <= m; ++k) {
      const double v = k*step;
      x.push_back(v);
      w.push_back(step*normal*exp_negative((v*v)/2.0));
    }
  }
};
void emit_array(const char* key, const Sums& a, bool comma=true) {
  std::cout << '"' << key << "\":[";
  for (std::size_t i=0; i<a.size(); ++i) {
    if (i) std::cout << ',';
    const double v = static_cast<double>(a[i]);
    if (!std::isfinite(v)) throw std::runtime_error("nonfinite sum");
    std::cout << bits(v);
  }
  std::cout << ']';
  if (comma) std::cout << ',';
}
void emit_meta(const std::vector<Grid>& grids, std::uint64_t outer, std::uint64_t total) {
  std::cout << "\"parsed_input_bits\":[";
  for (std::size_t i=0; i<received.size(); ++i) {
    if (i) std::cout << ',';
    std::cout << bits(received[i]);
  }
  std::cout << "],\"outer_points\":" << outer << ",\"total_points\":" << total
            << ",\"long_double_mantissa_bits\":" << LDBL_MANT_DIG
            << ",\"grid_mass_bits\":[";
  for (std::size_t i=0; i<grids.size(); ++i) {
    if (i) std::cout << ',';
    long double mass = 0;
    for (double w : grids[i].w) mass += w;
    std::cout << bits(static_cast<double>(mass));
  }
  std::cout << "]}" << std::endl;
}
void lower() {
  const int m0=read_int(), m1=read_int();
  const double h0=read_double(), h1=read_double(), normal=read_double();
  if (!(normal > 0.398 && normal < 0.400)) throw std::runtime_error("normal constant out of contract");
  std::array<std::array<double,2>,4> u;
  for (auto& row : u) for (double& v : row) {
    v=read_double(); if (std::fabs(v)>2) throw std::runtime_error("direction out of contract");
  }
  const std::vector<Grid> g={Grid(m0,h0,normal),Grid(m1,h1,normal)};
  if (!m0 || !m1) throw std::runtime_error("lower roots cannot be omitted");
  Sums Q(16), E(16), T(256);
  for (std::size_t i=0; i<g[0].x.size(); ++i) for (std::size_t j=0; j<g[1].x.size(); ++j) {
    const double weight=g[0].w[i]*g[1].w[j];
    std::array<double,4> h,e;
    for (int a=0;a<4;++a) {
      h[a]=bounded_tanh(u[a][0]*g[0].x[i]+u[a][1]*g[1].x[j]);
      e[a]=1.0-h[a]*h[a];
    }
    for (int a=0;a<4;++a) for(int b=0;b<4;++b) {
      const int ab=a*4+b;
      const double ee=e[a]*e[b];
      Q[ab]+=weight*(h[a]*h[b]);
      E[ab]+=weight*ee;
      for(int c=0;c<4;++c) for(int d=0;d<4;++d)
        T[ab*16+c*4+d]+=weight*(ee*(h[c]*h[d]));
    }
  }
  std::cout << "{\"mode\":\"lower\",";
  emit_array("Q_bits",Q); emit_array("L_bits",E); emit_array("T_bits",T);
  const std::uint64_t total=g[0].x.size()*g[1].x.size();
  emit_meta(g,total,total);
}
void upper() {
  std::array<int,4> m;
  for(int& v:m) v=read_int();
  std::array<double,4> steps;
  for(double& v:steps) v=read_double();
  const double normal=read_double();
  if (!(normal > 0.398 && normal < 0.400)) throw std::runtime_error("normal constant out of contract");
  std::array<std::array<double,4>,4> L;
  for(auto& row:L) for(double& v:row) {
    v=read_double(); if(std::fabs(v)>2) throw std::runtime_error("factor out of contract");
  }
  for(int a=0;a<3;++a) if(L[a][3]!=0.0) throw std::runtime_error("training coordinates depend on passive root");
  std::array<double,3> p;
  double P=0;
  for(double& v:p) {v=read_double();P+=std::fabs(v);}
  if(P>1.0) throw std::runtime_error("label norm out of contract");
  std::vector<Grid> g;
  for(int j=0;j<4;++j) g.emplace_back(m[j],steps[j],normal);
  for(int j=0;j<3;++j) if(!m[j]) throw std::runtime_error("training root cannot be omitted");
  if(!m[3] && L[3][3]!=0.0) throw std::runtime_error("nonzero passive root omitted");
  Sums ES2(1),V(9),ddgram(9),ESdd(3),dynV(3),dynC(9),dynD(3),dynSC(1),dynHdd(3),dynSH(1);
  for(std::size_t i=0;i<g[0].x.size();++i)
  for(std::size_t j=0;j<g[1].x.size();++j)
  for(std::size_t k=0;k<g[2].x.size();++k) {
    const std::array<double,3> x={g[0].x[i],g[1].x[j],g[2].x[k]};
    const double weight=(g[0].w[i]*g[1].w[j])*g[2].w[k];
    std::array<double,3> H,d,dd;
    double S=0;
    for(int a=0;a<3;++a) {
      const double z=(L[a][0]*x[0]+L[a][1]*x[1])+L[a][2]*x[2];
      H[a]=bounded_tanh(z); d[a]=1.0-H[a]*H[a]; dd[a]=(-2.0*H[a])*d[a];
      S+=p[a]*H[a];
    }
    const double mean=(L[3][0]*x[0]+L[3][1]*x[1])+L[3][2]*x[2];
    long double A=0,B=0,C=0;
    for(std::size_t l=0;l<g[3].x.size();++l) {
      const double Hx=bounded_tanh(mean+L[3][3]*g[3].x[l]);
      const double dx=1.0-Hx*Hx;
      A+=g[3].w[l]*Hx;
      B+=g[3].w[l]*dx;
      C+=g[3].w[l]*((-2.0*Hx)*dx);
    }
    const long double sw=static_cast<long double>(weight)*S;
    const long double ssw=sw*S;
    ES2[0]+=ssw;
    dynSC[0]+=sw*C; dynSH[0]+=sw*A;
    for(int a=0;a<3;++a) {
      ESdd[a]+=sw*dd[a];
      dynV[a]+=ssw*B*d[a];
      dynD[a]+=static_cast<long double>(weight)*B*d[a];
      dynHdd[a]+=static_cast<long double>(weight)*A*dd[a];
      for(int b=0;b<3;++b) {
        const double dab=d[a]*d[b];
        V[a*3+b]+=ssw*dab;
        ddgram[a*3+b]+=static_cast<long double>(weight)*dab;
        dynC[a*3+b]+=sw*A*dab;
      }
    }
  }
  std::cout << "{\"mode\":\"upper\",";
  emit_array("ES2_bits",ES2);emit_array("V_bits",V);emit_array("ddgram_bits",ddgram);emit_array("ESdd_bits",ESdd);
  emit_array("dynamic_V_bits",dynV);emit_array("dynamic_C_bits",dynC);
  emit_array("dynamic_dd_bits",dynD);emit_array("dynamic_ESdd_bits",dynSC);
  emit_array("dynamic_Hdd_bits",dynHdd);emit_array("dynamic_SH_bits",dynSH);
  const std::uint64_t outer=g[0].x.size()*g[1].x.size()*g[2].x.size();
  emit_meta(g,outer,outer*g[3].x.size());
}
void primitives() {
  const int n=read_int();
  if(n<1 || n>10000) throw std::runtime_error("primitive count out of contract");
  Sums h,e;
  for(int i=0;i<n;++i) {
    const double v=read_double(); h.push_back(bounded_tanh(v));
    e.push_back(v>=0 && v<=64 ? exp_negative(v) : 0.0);
  }
  std::cout << "{\"mode\":\"primitives\",";
  emit_array("tanh_bits",h);emit_array("exp_negative_bits",e);
  emit_meta({},n,n);
}
} // namespace
int main() {
  try {
    if(std::fegetround()!=FE_TONEAREST) throw std::runtime_error("round-to-nearest required");
    std::string mode;
    if(!(std::cin>>mode)) throw std::runtime_error("missing mode");
    if(mode=="lower") lower(); else if(mode=="upper") upper();
    else if(mode=="primitives") primitives(); else throw std::runtime_error("unknown mode");
    return 0;
  } catch(const std::exception& e) {
    std::cerr << e.what() << std::endl;
    return 1;
  }
}
