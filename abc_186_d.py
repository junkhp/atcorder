# -*- coding: utf-8 -*-
from itertools import accumulate


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list = sorted(a_list)
    # print(a_list)
    cumsum = list(accumulate(a_list))
    ans = 0
    for i in range(n - 1):
        ans += cumsum[-1] - cumsum[i] - (n - 1 - i) * a_list[i]
    print(ans)


if __name__ == "__main__":
    main()