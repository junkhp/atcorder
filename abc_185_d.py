# -*- coding: utf-8 -*-
from math import ceil
def main():
    n, m = map(int, input().split())
    if m == 0:
        print(1)
        return
    a = sorted(list(map(int, input().split())))
    min_space = float('inf')
    spaces = {}
    for i in range(-1, m):
        if i == m - 1:
            space = n - a[-1]
        elif i == -1:
            space = a[0] - 1
        else:
            space = a[i + 1] - a[i] - 1
        if space != 0:
            if space in spaces.keys():
                spaces[space] += 1
            else:
                spaces[space] = 1
            if min_space > space:
                min_space = space
        # print(spaces)

    ans = 0
    for key, value in spaces.items():
        ans += value * ceil(key / min_space)
    # print(spaces)
    print(ans)


if __name__ == "__main__":
    main()