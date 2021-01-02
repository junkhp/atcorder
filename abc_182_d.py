# -*- coding: utf-8 -*-
from itertools import accumulate


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    p_list = list(accumulate(a_list))
    q_list = []

    q_max = 0
    for i in range(n):
        if q_max < p_list[i]:
            q_max = p_list[i]
        q_list.append(q_max)
    ans = 0
    place = 0
    for i in range(n):
        ans = max(ans, place + q_list[i])
        place += p_list[i]
    
    print(ans)


if __name__ == "__main__":
    main()
