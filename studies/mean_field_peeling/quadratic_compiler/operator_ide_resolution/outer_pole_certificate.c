#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

/* Exact outward-rounded fixed-point arithmetic.  All represented reals are
   nonnegative and have denominator D=2^K. */
typedef unsigned __int128 u128;
enum { K=48, BCELL=10, NSTAGE=13 };
static const u128 D=((u128)1)<<K;

static u128 ceildiv(u128 x,u128 y){ return x/y + (x%y != 0); }
static u128 prod(u128 x,u128 y){
  if(x && y>((u128)-1)/x){ fputs("128-bit overflow\n",stderr); exit(2); }
  return x*y;
}
static u128 mul_dn(u128 x,u128 y){ return prod(x,y)/D; }
static u128 mul_up(u128 x,u128 y){ return ceildiv(prod(x,y),D); }
static u128 div_dn(u128 x,u128 y){ return prod(x,D)/y; }
static u128 div_up(u128 x,u128 y){ return ceildiv(prod(x,D),y); }
static u128 rat_dn(uint64_t n,uint64_t d){ return ((u128)n*D)/d; }
static u128 rat_up(uint64_t n,uint64_t d){ return ceildiv((u128)n*D,d); }

static void print_u128(u128 x){
  char s[64]; int n=0;
  if(!x){ putchar('0'); return; }
  while(x){ s[n++]=(char)('0'+x%10); x/=10; }
  while(n) putchar(s[--n]);
}
static void print_fp(u128 x){
  u128 z=(x*1000000000000000ULL)/D;
  uint64_t zz=(uint64_t)z;
  printf("%llu.%015llu",(unsigned long long)(zz/1000000000000000ULL),
         (unsigned long long)(zz%1000000000000000ULL));
}

/* Enclose the solution at q=8192 for a in [al,au], b in [bl,bu].
   Inputs and outputs are fixed-point endpoints. */
static void enclose_p(u128 al,u128 au,u128 bl,u128 bu,unsigned p,unsigned nstage,
                    u128 *HL,u128 *HU,u128 *VL,u128 *VU){
  const u128 c3=rat_dn(3,8), c29=rat_dn(29,8);
  u128 hl=0,hu=0,vl=bl,vu=bu,q=D;
  for(unsigned k=0;k<nstage;k++){
    /* h=2^k/2^P and every q endpoint are exactly representable. */
    u128 h=D;
    if(k>=p) h <<= (k-p); else h >>= (p-k);
    for(unsigned j=0;j<(1u<<p);j++){
      u128 qn=q+h;
      /* upper H increment: 3 h/(8 q V), evaluated at left endpoint */
      u128 dhu=mul_up(c3,h);
      dhu=div_up(dhu,q); dhu=div_up(dhu,vl);
      u128 hun=hu+dhu;
      /* upper V increment: a h H(right)+29 a h/(8 V(left)) */
      u128 t1=mul_up(au,h); t1=mul_up(t1,hun);
      u128 t2=mul_up(c29,au); t2=mul_up(t2,h); t2=div_up(t2,vl);
      u128 vun=vu+t1+t2;
      /* lower V increment: a h H(left)+29 a h/(8 V(right)) */
      u128 s1=mul_dn(al,h); s1=mul_dn(s1,hl);
      u128 s2=mul_dn(c29,al); s2=mul_dn(s2,h); s2=div_dn(s2,vun);
      u128 vln=vl+s1+s2;
      /* lower H increment, evaluated at right endpoint */
      u128 dhl=mul_dn(c3,h);
      dhl=div_dn(dhl,qn); dhl=div_dn(dhl,vun);
      u128 hln=hl+dhl;
      hl=hln; hu=hun; vl=vln; vu=vun; q=qn;
    }
  }
  *HL=hl;*HU=hu;*VL=vl;*VU=vu;
}

static void enclose(u128 al,u128 au,u128 bl,u128 bu,
                    u128 *HL,u128 *HU,u128 *VL,u128 *VU){
  enclose_p(al,au,bl,bu,11,NSTAGE,HL,HU,VL,VU);
}

static void ellipse_a(u128 bl,u128 bu,u128 *al,u128 *au){
  u128 three=3*D;
  u128 b2u=mul_up(bu,bu), b2l=mul_dn(bl,bl);
  *al=2*D-div_up(b2u,three);
  *au=2*D-div_dn(b2l,three);
}

/* Branch-and-bound certificate for the sharper global endpoint
   H(infinity)>3*0.08389=25167/100000.  A finite-q lower enclosure is also
   a lower bound at infinity because H is increasing. */
static uint64_t refine_nodes=0, refine_leaves=0;
static unsigned refine_deepest=0;
static int certify_sharp_cell(uint64_t i,unsigned level){
  u128 bl=((u128)i*D)>>level;
  u128 bu=((u128)(i+1)*D)>>level;
  u128 al,au,hl,hu,vl,vu;
  unsigned p,ns;
  if(level<=12){ p=14; ns=16; }
  else if(level<=15){ p=16; ns=18; }
  else { p=18; ns=20; }
  ellipse_a(bl,bu,&al,&au);
  enclose_p(al,au,bl,bu,p,ns,&hl,&hu,&vl,&vu);
  refine_nodes++;
  if(hl*100000 > (u128)25167*D){
    refine_leaves++;
    return 1;
  }
  if(level>=18){
    printf("FAIL refined cell=[%llu/2^%u,%llu/2^%u] H_lower=",
           (unsigned long long)i,level,(unsigned long long)(i+1),level);
    print_fp(hl); putchar('\n');
    return 0;
  }
  if(level+1>refine_deepest) refine_deepest=level+1;
  return certify_sharp_cell(2*i,level+1)
      && certify_sharp_cell(2*i+1,level+1);
}

int main(void){
  /* [13/32,29/16], split into cells of width 2^-10. */
  const unsigned first=416, last=1856;
  u128 minhl=(u128)-1; unsigned arg=0;
  for(unsigned i=first;i<last;i++){
    u128 bl=((u128)i*D)>>BCELL;
    u128 bu=((u128)(i+1)*D)>>BCELL;
    u128 al,au,hl,hu,vl,vu;
    ellipse_a(bl,bu,&al,&au);
    enclose(al,au,bl,bu,&hl,&hu,&vl,&vu);
    if(hl<minhl){minhl=hl;arg=i;}
  }
  printf("central_cells=%u min_cell=[%u/1024,%u/1024]\n",last-first,arg,arg+1);
  printf("central_H_lower="); print_fp(minhl); printf("  exact_numerator=");
  print_u128(minhl); printf(" / 2^48\n");
  if(minhl*2000 <= (u128)501*D){ puts("FAIL central"); return 1; }

  /* Sharpen the global lower endpoint to 0.0838.  Every coarse cell already
     above 3*0.0838=1257/5000 is done.  Bisect each remaining cell and rerun
     with p=14 through q=16384. */
  u128 sharpmin=(u128)-1; unsigned sharp_arg=0, candidates=0;
  for(unsigned i=first;i<last;i++){
    u128 bl=((u128)i*D)>>BCELL;
    u128 bu=((u128)(i+1)*D)>>BCELL;
    u128 al,au,hl,hu,vl,vu;
    ellipse_a(bl,bu,&al,&au);
    enclose(al,au,bl,bu,&hl,&hu,&vl,&vu);
    if(hl*5000 > (u128)1257*D) continue;
    candidates++;
    for(unsigned half=0;half<2;half++){
      u128 sbl=((u128)(2*i+half)*D)>>(BCELL+1);
      u128 sbu=((u128)(2*i+half+1)*D)>>(BCELL+1);
      ellipse_a(sbl,sbu,&al,&au);
      enclose_p(al,au,sbl,sbu,14,14,&hl,&hu,&vl,&vu);
      if(hl<sharpmin){sharpmin=hl;sharp_arg=2*i+half;}
      if(hl*5000 <= (u128)1257*D){ puts("FAIL sharp central"); return 1; }
    }
  }
  printf("sharp_candidates=%u sharp_min_cell=[%u/2048,%u/2048]\n",
         candidates,sharp_arg,sharp_arg+1);
  printf("sharp_H_lower=");print_fp(sharpmin);printf("  exact_numerator=");
  print_u128(sharpmin);printf(" / 2^48\n");

  /* Low-b dominating seed (a,b)=(2,13/32). */
  u128 hl,hu,vl,vu;
  enclose(2*D,2*D,rat_dn(13,32),rat_up(13,32),&hl,&hu,&vl,&vu);
  printf("low_dominator_H_lower=");print_fp(hl);printf("  exact_numerator=");
  print_u128(hl);printf(" / 2^48\n");
  if(hl*5000 <= (u128)1257*D){ puts("FAIL low"); return 1; }
  if(hl*100000 <= (u128)25167*D){
    puts("FAIL sharp low dominator");
    return 1;
  }

  /* High-b dominating seed: a=2-(29/16)^2/3=2780/3072,
     b=5/2 dominates all ellipse seeds with b>=29/16. */
  enclose(rat_dn(2780,3072),rat_up(2780,3072),
          rat_dn(5,2),rat_up(5,2),&hl,&hu,&vl,&vu);
  printf("high_dominator_H_lower=");print_fp(hl);printf("  exact_numerator=");
  print_u128(hl);printf(" / 2^48\n");
  if(hl*5000 <= (u128)1257*D){ puts("FAIL high"); return 1; }
  if(hl*100000 <= (u128)25167*D){
    puts("FAIL sharp high dominator");
    return 1;
  }
  puts("PASS: every normalized outer seed has 3T > 1257/5000.");

  /* The coarse pass above is cheap enough to screen the full interval.
     Only cells whose coarse enclosure does not already prove the sharper
     endpoint are recursively refined. */
  for(unsigned i=first;i<last;i++){
    u128 bl=((u128)i*D)>>BCELL;
    u128 bu=((u128)(i+1)*D)>>BCELL;
    u128 al,au,hl0,hu0,vl0,vu0;
    ellipse_a(bl,bu,&al,&au);
    enclose(al,au,bl,bu,&hl0,&hu0,&vl0,&vu0);
    if(hl0*100000 > (u128)25167*D) continue;
    if(!certify_sharp_cell(i,BCELL)) return 1;
  }
  printf("refined_global_nodes=%llu leaves=%llu deepest=%u\n",
         (unsigned long long)refine_nodes,
         (unsigned long long)refine_leaves,refine_deepest);
  puts("PASS: every normalized outer seed has T > 0.08389.");

  /* Point upper certificate.  For U0=a*8192,
       H(infinity)-H(U0) <= 3/(8 H(U0) U0),
     because V(U)>=H(U0)U for U>=U0. */
  u128 aL=rat_dn(335,192),aU=rat_up(335,192);
  enclose_p(aL,aU,rat_dn(7,8),rat_up(7,8),12,NSTAGE,&hl,&hu,&vl,&vu);
  u128 tail=rat_up(3,8);
  tail=div_up(tail,hl); tail=div_up(tail,aL);
  tail=div_up(tail,8192*D);
  u128 hinf=hu+tail;
  printf("seed_(335/192,7/8)_Hinf_upper=");print_fp(hinf);
  printf("  exact_numerator=");print_u128(hinf);printf(" / 2^48\n");
  if(hinf*250 >= (u128)63*D){ puts("FAIL seed .084"); return 1; }

  /* A higher-resolution enclosure of the same point supplies the narrow
     upper endpoint needed for the low-density exposure window. */
  enclose_p(aL,aU,rat_dn(7,8),rat_up(7,8),18,20,
            &hl,&hu,&vl,&vu);
  tail=rat_up(3,8); tail=div_up(tail,hl); tail=div_up(tail,aL);
  tail=div_up(tail,((u128)1<<20)*D); hinf=hu+tail;
  printf("seed_highres_Hinf_upper=");print_fp(hinf);
  printf("  exact_numerator=");print_u128(hinf);printf(" / 2^48\n");
  if(hinf*10000 >= (u128)2517*D){
    puts("FAIL seed at T=0.0839");
    return 1;
  }
  puts("PASS: seed (335/192,7/8) has T<0.0839.");

  /* Rate 9/10 seed: b=5/6, a=2(9/10)-b^2/3=847/540. */
  aL=rat_dn(847,540);aU=rat_up(847,540);
  enclose(aL,aU,rat_dn(5,6),rat_up(5,6),&hl,&hu,&vl,&vu);
  tail=rat_up(3,8); tail=div_up(tail,hl); tail=div_up(tail,aL);
  tail=div_up(tail,8192*D); hinf=hu+tail;
  printf("rate_9/10_seed_Hinf_upper=");print_fp(hinf);
  printf("  exact_numerator=");print_u128(hinf);printf(" / 2^48\n");
  /* H_infinity=3T.  Since 3*0.088572=0.265716=66429/250000,
     this exact comparison certifies the strict seed bound used in the proof. */
  if(prod(hinf,250000) >= prod((u128)66429,D)){
    puts("FAIL rate .9 seed at T=0.088572");
    return 1;
  }
  puts("PASS: first point has T<0.084; rate-9/10 point has T<0.088572.");
  return 0;
}
