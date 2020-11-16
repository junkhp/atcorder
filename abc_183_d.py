# -*- coding: utf-8 -*-

def main():
    n, w = map(int, input().split())
    max_t = 2*(10**5) + 10
    imosu = [0] * max_t
    for i in range(n):
        s, t, p = map(int, input().split())
        imosu[s] += p
        imosu[t] -= p 
    sum_water = 0
    for i in imosu:
        sum_water += i
        if sum_water > w:
            print('No')
            return
    print('Yes')

    
if __name__ == '__main__':
    main()