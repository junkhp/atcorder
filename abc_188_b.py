# -*- coding: utf-8 -*-
def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    ans = 0
    for a, b in zip(a_list, b_list):
        ans += a * b
    
    if ans == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
