# -*- coding: utf-8 -*-
from itertools import groupby


def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    p_list_sorted = sorted(p_list)

    p_set = set()
    max_mun = 0
    min_num = 0
    for i in range(n):
        p_set.add(p_list[i])
        while (1):
            if not min_num in p_set:
                print(min_num)
                break
            else:
                min_num += 1


if __name__ == "__main__":
    main()
