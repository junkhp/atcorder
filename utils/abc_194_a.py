# -*- coding: utf-8 -*-
from itertools import accumulate
def main():
    n = int(input())
    a_list = sorted(list(map(int, input().split())))

    ans = 0
    for i in range(n):
        ans += a_list[i] ** 2
    ans = ans * (n - 1)

    a_sum = sum(a_list)
    sub_sum = 0
    for i in range(n - 1):
        x = a_list.pop()
        a_sum -= x
        sub_sum += x * (a_sum)
    ans = ans - 2 * sub_sum
    print(ans)

if __name__ == '__main__':
    main()
