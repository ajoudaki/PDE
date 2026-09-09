#!/usr/bin/env python3
"""Exact rational unit-sphere search for failed full/frozen domination."""

from fractions import Fraction as Q
from random import Random

import quadratic_euler_jet as dag
from search_general_poly_comparison import raw_product_moment
from search_signfree_full_vs_frozen import difference_coefficients


def inner(a,b):
    # Polarization of the exact Gaussian L2 norm.
    return (raw_product_moment(tuple(x+y for x,y in zip(a,b)),(0,0))-
            raw_product_moment(a,(0,0))-raw_product_moment(b,(0,0)))/2


def unit_from(raw):
    base=(Q(1),)+(Q(0),)*(len(raw)-1)
    direction=tuple(x-y for x,y in zip(raw,base))
    dd=inner(direction,direction)
    bd=inner(base,direction)
    if not dd or not bd:return None
    lam=-2*bd/dd
    psi=tuple(x+lam*y for x,y in zip(base,direction))
    assert raw_product_moment(psi,(0,0))==1
    return psi


def main():
    dag.MAX_H=5
    rng=Random(20260825)
    for trial in range(80):
        degree=3 if trial<60 else 4
        raw=tuple(Q(rng.randint(-8,8)) for _ in range(degree+1))
        if not raw[-1]:continue
        psi=unit_from(raw)
        if psi is None or not (min(psi)<0<max(psi)):continue
        diff=difference_coefficients(psi)[2]
        if diff[3]<0 or diff[5]<0:
            print("FOUND",psi,"d3",diff[3],"d5",diff[5]);return
        print("PASS",trial,"d",degree,"d3",float(diff[3]),"d5",float(diff[5]))
    print("NO COUNTEREXAMPLE")


if __name__=="__main__":main()
