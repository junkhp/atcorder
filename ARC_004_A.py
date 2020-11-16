# -*- coding: utf-8 -*-
import math
def dist(x, y):
    return math.sqrt((x[0]-y[0])*(x[0]-y[0]) + (x[1] - y[1])*(x[1] - y[1]))
def main():
    N = int(input())
    x = []
    for i in range(N):
        x.append(list(map(int, input().split())))
    max = 0
    for i in range(N-1):
        for j in range(i+1, N):
            d = dist(x[i], x[j])
            if d > max:
                max = d
    print(max)
if __name__ == '__main__':
    main()
