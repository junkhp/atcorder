# -*- coding: utf-8 -*-
def g1(x):
    return int(''.join(list(map(int, sorted(str(x)))))


def g2(x):
    return int(''.join(list(map(int, sorted(str(x), reverse=True)))))


def f(x):
    return g1(x) + g2(x)


def main():
    n, k = map(int, input().split())
    for i in range(10):

if __name__ == '__main__':

    main()
