# -*- coding: utf-8 -*-
from operator import mul
from functools import reduce


def cmb(n , r):
    r = min(n-r,r)
    if r == 0 : return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

def main():
    length = int(input())
    print(cmb(length - 1 , 11))
if __name__ == "__main__":
    main()